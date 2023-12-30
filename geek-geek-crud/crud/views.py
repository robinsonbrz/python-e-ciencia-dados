from django.shortcuts import (get_object_or_404, render,
                            HttpResponseRedirect)
from .models import Books
from .forms import BooksForm


def home_view(request):
    livros = Books.objects.all()
    context={}
    context["livros"]=livros
    return render(request, 'crud/home.html', context)

def delete_book_view(request, id):
    book = Books.objects.get(id=id)
    book.delete()
    return home_view(request)

def update_book_view(request, id):
    context = {}

    obj = get_object_or_404(Books, id = id)
    form = BooksForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(""+id)
    context["form"] = form

    return render(request, "crud/update_book_view.html", context)
