
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

### Uso do Include

Podemos tambem criar trechos html para ser incluidos em outros templates
Muito util para organizar head, footer, e divs que podem ser reutilizadas

Primeiro criar o arquivo html a ser inserido
em: base/global/partials/head.html
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
```

Esse trecho isere o conteudo de head.html na mesma linha em que for digitado no template
```html
{% include 'global/partials/head.html' %}
```

em: base/global/base.html
```html
{% include 'global/partials/head.html' %}

<h1>{% block texto %}{% endblock texto %}</h1>

</body>
</html>
```

### Static files
Podemos criar pastas chamadas `static` dentro de cada app que por padrao o Django reconhece

Adicionando outros diretorios em uma lista STATICFILES_DIRS
settings.py
```python
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'base' / 'static'
]
```

Criando uma pasta static global

base/static/global/css/red.css
```css
body {
  background: red;
}
```


Criando uma pasta static na propria app, padrao Django

home/static/home/css/blue.css
```css
body {
  background: blue;
}
```

No template apontar para pastas estaticas
```python
{% load static %}
<link rel="stylesheet" href="{% static 'home/css/blue.css' %}">
<link rel="stylesheet" href="{% static 'global/css/red.css' %}">
```


