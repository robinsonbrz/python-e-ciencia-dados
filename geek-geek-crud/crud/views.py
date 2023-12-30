from django.shortcuts import render
from .models import Books
def home_view(request):
    livros = Books.objects.all()
    context={}
    context["livros"]=livros
    return render(request, 'crud/home.html', context)

def delete_book_view(request, id):
    book = Books.objects.get(id=id)
    book.delete()
    return home_view(request)
