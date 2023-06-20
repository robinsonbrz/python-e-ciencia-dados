import json
import logging

import pytest
from django.urls import reverse

from companies.models import Company

companies_url = reverse("companies-list")
# The bellow line substitutes @pytest.mark.djangodb on every function in this file
pytestmark = pytest.mark.django_db


def test_zero_companies_should_return_empty_list(client) -> None:
    response = client.get(companies_url)
    assert response.status_code == 200
    assert json.loads(response.content) == []


def test_one_company_exists_should_return_one_company(client) -> None:
    test_company = Company.objects.create(name="amazon")
    response = client.get(companies_url)
    response_content = json.loads(response.content)[0]
    assert response.status_code == 200
    assert response_content.get("name") == test_company.name
    assert response_content.get("status") == "Hiring"
    assert response_content.get("application_link") == ""
    assert response_content.get("notes") == ""
    test_company.delete()

    #     # b"" stream of bytes


# ----------------------- Test Post Companies -----------------------


def test_create_company_without_arguments_should_fail(client) -> None:
    response = client.post(path=companies_url)
    assert response.status_code == 400
    assert json.loads(response.content) == {"name": ["This field is required."]}


def test_create_existing_company_should_fail(client) -> None:
    test_company = Company.objects.create(name="amazon")
    response = client.post(path=companies_url, data={"name": "amazon"})
    assert response.status_code == 400
    assert json.loads(response.content) == {
        "name": ["company with this name already exists."]
    }
    test_company.delete()


def test_create_company_with_only_name_should_be_default(client) -> None:
    response = client.post(path=companies_url, data={"name": "test company name"})
    assert response.status_code == 201
    response_content = json.loads(response.content)
    assert response_content.get("name") == "test company name"
    assert response_content.get("status") == "Hiring"
    assert response_content.get("application_link") == ""
    assert response_content.get("notes") == ""


def test_create_company_with_layoffs_status_should_succeed(client) -> None:
    response = client.post(
        path=companies_url,
        data={"name": "test company name", "status": "Layoffs"},
    )
    assert response.status_code == 201
    response_content = json.loads(response.content)
    assert response_content.get("status") == "Layoffs"


def test_create_company_with_wrong_status_should_fail(client) -> None:
    response = client.post(
        path=companies_url,
        data={"name": "test company name", "status": "WrongStatus"},
    )
    assert response.status_code == 400
    response_content = json.loads(response.content)
    assert "status" in str(response_content)


def raise_covid19_exception() -> None:
    raise ValueError("CoronaVirus Exception")


def test_raise_covid19_exception_should_pass() -> None:
    with pytest.raises(ValueError) as e:
        raise_covid19_exception()
    assert "CoronaVirus Exception" == str(e.value)


logger = logging.getLogger("CORONA_LOGS")


def function_that_logs_something() -> None:
    try:
        raise ValueError("CoronaVirus Exception")
    except ValueError as e:
        logger.warning(f"I am logging {str(e)}")


def test_logged_warning_level(caplog) -> None:
    # just warning levels and above
    function_that_logs_something()
    assert "I am logging CoronaVirus Exception" in caplog.text


def test_logged_info_level(caplog) -> None:
    # this way we can capture info level logs
    with caplog.at_level(logging.INFO):
        logger.info("I am logging info level")
        assert "I am logging info level" in caplog.text
