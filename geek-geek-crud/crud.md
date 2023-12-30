


### adicionando dados
>>> book = Books(title="Titulo 3", description="description 3")
>>> book.save


data = {"title": "My Book", "description": "A book description"}
book = Books(**data)
book.save()


books_data = [
  {"title": "Book 1", "description": "Desc 1"}, 
  {"title": "Book 2", "description": "Desc 2"}
]

for data in books_data:
  book = Books(**data)
  book.save()

books = [Books(**data) for data in books_data]
Books.objects.bulk_create(books)

