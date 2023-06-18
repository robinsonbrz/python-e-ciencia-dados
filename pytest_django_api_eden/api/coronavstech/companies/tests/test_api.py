import json
from unittest import TestCase

import pytest
from django.test import Client
from django.urls import reverse

from companies.models import Company


@pytest.mark.django_db   # from pytest.django
class BasicCompanyApiTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.companies_url = reverse("companies-list")
    
    def tearDown(self) -> None:
        pass

class TestGetCompanies(BasicCompanyApiTestCase):
    def test_zero_companies_should_return_empty_list(self) -> None:
        response = self.client.get(self.companies_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), [])

    def test_one_company_exists_should_return_one_company(self) -> None:
        test_company = Company.objects.create(name="amazon")
        response = self.client.get(self.companies_url)
        response_content = json.loads(response.content)[0]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_content.get("name"), test_company.name)
        self.assertEqual(response_content.get("status"), "Hiring")
        self.assertEqual(response_content.get("application_link"), "")
        self.assertEqual(response_content.get("notes"), "")
        test_company.delete()
        
    #     # b"" stream of bytes



class TestPostCompanies(BasicCompanyApiTestCase):

    def test_create_company_without_arguments_should_fail(self) -> None:
        response = self.client.post(path=self.companies_url)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            json.loads(response.content), {"name": ["This field is required."]}
        )

    def test_create_existing_company_should_fail(self) -> None:
        test_company = Company.objects.create(name="amazon")
        response = self.client.post(path=self.companies_url, data={"name": "amazon"})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            json.loads(response.content), {"name": ["company with this name already exists."]}
        )
        test_company.delete()

    def test_create_company_with_only_name_should_be_default(self) -> None:
        response = self.client.post(path=self.companies_url, data={"name": "test company name"})
        self.assertEqual(response.status_code, 201)
        response_content = json.loads(response.content)
        self.assertEqual(response_content.get("name"), "test company name")
        self.assertEqual(response_content.get("status"), "Hiring")
        self.assertEqual(response_content.get("application_link"), "")
        self.assertEqual(response_content.get("notes"), "")
    
    def test_create_company_with_layoffs_status_should_succeed(self) -> None:
        response = self.client.post(path=self.companies_url, data={"name": "test company name", "status": "Layoffs"})
        self.assertEqual(response.status_code, 201)
        response_content = json.loads(response.content)
        self.assertEqual(response_content.get("status"), "Layoffs")

    def test_create_company_with_wrong_status_should_fail(self) -> None:
        response = self.client.post(path=self.companies_url, data={"name": "test company name", "status": "WrongStatus"})
        self.assertEqual(response.status_code, 400)
        response_content = json.loads(response.content)
        self.assertIn("status", response_content)



def raise_covid19_exception() -> None:
    raise ValueError('CoronaVirus Exception')

def test_raise_covid19_exception_should_pass() -> None:
    with pytest.raises(ValueError) as e:
        raise_covid19_exception()
    assert 'CoronaVirus Exception' == str(e.value)


