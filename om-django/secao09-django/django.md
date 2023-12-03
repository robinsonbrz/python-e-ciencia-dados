
Organizar os templates na pasta nome-app/template/nome-app
Dentro do template 


Configurando uma pasta onde ser'ao inseridos arquivos base

```ptyhon
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'base'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

Conforme configurado acima temos uma pasta 'base' de templates


Neste  arquivo base ja preparamos um block para receber texto
Abaixo configuro o template pai com um bloco **texto** com um valor padrao
Esse valor padrao sera sobrescrito caso o template filho (que extends coloque um 'block' com o mesmo nome)
base/global/base.html
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <h1>{% block texto %} Valor padrao caso o filho nao insira nada {% endblock texto %}</h1>
  </body>
</html>
```

Isso e um template tag Django 
```python
{% block texto %} {% endblock texto %}
```



Este e o index.html que extends base html
E injeta um bloco texto, substituindo o valor padrao do template pai
home/templates/home/index.html
```python
{% extends 'global/base.html' %}

{% block texto %} MUDAR O TEXTO {% endblock texto %}
```

A view chama render template index.html que extends base.html
home/views.py
```python
from django.shortcuts import render


def home(request):
    print('home')

    return render(
        request,
        'home/index.html'
    )
```