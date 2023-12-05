
Organizar os templates na pasta nome-app/template/nome-app
Dentro do template 


Configurando uma pasta onde serão inseridos arquivos base

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


Neste arquivo base já preparamos um block para receber texto
Abaixo configuro o template pai com um bloco **texto** com um valor padrão
Esse valor padrão sera sobrescrito caso o template filho (que extends coloque um 'block' com o mesmo nome)
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

Isso é um template tag Django 
```python
{% block texto %} {% endblock texto %}
```



Este é o index.html que extends base html
E injeta um bloco texto, substituindo o valor padrão do template pai
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

Podemos também criar trechos html para ser incluídos em outros templates
Muito útil para organizar head, footer, e divs que podem ser reutilizadas

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
### Enviando variaveis para o contexto {{ variavel }}



```python

def exemplo(request):
    print('exemplo')

    context = {
        'text': 'Olá exemplo',
        'title': 'Essa é uma página de exemplo - ',
    }

    return render(
        request,
        'blog/exemplo.html',
        context
    )

```



Recebendo no template
```html
    <title>{{ title }}</title>
    <h1>{{ text }}</h1>

```

### Reverse name urls



base/global/base.html
```
{% include 'global/partials/menu.html' %}
```

base/global/partials/menu.html
```html
<nav>
  <ul>
    <li>
      <a href="{% url 'home:home' %}">Home</a>
    </li>
    <li>
      <a href="{% url 'blog:home' %}">Blog</a>
    </li>
    <li>
      <a href="{% url 'blog:exemplo' %}">Exemplo</a>
    </li>
  </ul>
</nav>
```

blog/urls.py
```python
from blog import views
from django.urls import path

app_name = 'blog'

# blog/
urlpatterns = [
    path('', views.blog),
    path('exemplo/', views.exemplo),
    path('', views.blog, name='home'),
    path('exemplo/', views.exemplo, name='exemplo'),
]

```
### Include block de posts


base/global/base.html

```html

<h1>{% block texto %}{% endblock texto %}</h1>

<main class="posts">
  {% include 'global/partials/postblock.html' %}
</main>

</body>
</html>

```

base/global/partials/postblock.html

```html
<article class="post">
  <header>
    <h2 class="post__title">Lorem ipsum dolor sit amet.</h2>
  </header>
  <div class="post__body">
    Lorem ipsum dolor sit amet consectetur, adipisicing elit. Aperiam doloremque
    praesentium nam mollitia, recusandae asperiores in corporis ut eius
    architecto rerum quae adipisci. Animi, repudiandae aut alias neque ab nemo
    quasi perspiciatis natus odio ad aliquid eos. Illum incidunt perspiciatis
    autem dolorum maxime, repellat facere, quae assumenda adipisci iure
    officiis.
  </div>
</article>
```
base/static/global/css/style.css

```css
/* Reset */
*,
*:after,
*:before {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  font-size: 62.5%;
}

body {
  font-size: 1.6rem;
  background: #f1f1f1;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto,
    Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}

```



### Carregando dados de um json com loop for no template

jsonplaceholder
moca uma api


blog/views.py
```python
from blog.data import posts
from django.shortcuts import render


def blog(request):
    print('blog')

    context = {
        'text': 'Olá blog',
        'posts': posts
    }

    return render(
        request,
        'blog/index.html',
        context
    )
```


blog/data.py
```python
posts = [
    {
        "userId": 1,
        "id": 1,
        "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
        "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
    },
    {
        "userId": 1,
        "id": 2,
        "title": "qui est esse",
        "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
    },
    {
        "userId": 1,
        "id": 3,
        "title": "ea molestias quasi exercitationem repellat qui ipsa sit aut",
        "body": "et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut"
    },
    {
        "userId": 1,
        "id": 4,
        "title": "eum et est occaecati",
        "body": "ullam et saepe reiciendis voluptatem adipisci\nsit amet autem assumenda provident rerum culpa\nquis hic commodi nesciunt rem tenetur doloremque ipsam iure\nquis sunt voluptatem rerum illo velit"
    },
    {
        "userId": 1,
        "id": 5,
        "title": "nesciunt quas odio",
        "body": "repudiandae veniam quaerat sunt sed\nalias aut fugiat sit autem sed est\nvoluptatem omnis possimus esse voluptatibus quis\nest aut tenetur dolor neque"
        }
]
```

blog/templates/blog/index.html
```python
{% extends 'global/base.html' %}

{% block texto %} {{ text }} {% endblock texto %}

{% block posts %}
  {% for post in posts %}
    {% include 'global/partials/postblock.html' %}
  {% endfor %}
{% endblock posts %}
```


base/global/partials/postblock.html
```html
<article class="post">
  <header>
    <h2 class="post__title">{{ post.title }}</h2>
  </header>
  <div class="post__body">{{ post.body }}</div>
</article>

```
### if template

```python
{% if text %}
  <h1>{% block texto %}{% endblock texto %}</h1>
{% endif %}
```

### URL com id

blog/views.py

```python
def post(request, id):
    print('post', id)

    context = {
        # 'text': 'Olá blog',
        'posts': posts
    }

    return render(
        request,
        'blog/index.html',
        context
    )
```

blog/urls.py
```python
app_name = 'blog'

# blog/
# Django URLs:
# https://docs.djangoproject.com/en/4.2/topics/http/urls/
urlpatterns = [
    path('', views.blog, name='home'),
    path('post/<int:id>', views.post, name='post'),
    path('exemplo/', views.exemplo, name='exemplo'),
]
```

base/global/partials/postblock.html
```html
      <a href="{% url 'blog:post' post.id %}">
```

# Post Detalhe


blog/views.py
```python
from typing import Any

from blog.data import posts
from django.http import HttpRequest
from django.shortcuts import render


def post(request: HttpRequest, post_id: int):
    found_post: dict[str, Any] | None = None

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break

    if found_post is None:
        raise Exception('Post não existe.')

    context = {
        # 'text': 'Olá blog',
        'post': found_post,
        'title': found_post['title'] + ' - ',
    }

    return render(
        request,
        'blog/post.html',
        context
    )

```

Novo template
blog/templates/blog/post.html

```html
{% extends 'global/base.html' %}

{% block texto %} {{ text }} {% endblock texto %}

{% block posts %}
  <article class="post single-post">
    <header>
      <h1 class="post__title">
        <a href="{% url 'blog:post' post.id %}">
          {{ post.title }}
        </a>
      </h1>
    </header>
    <div class="post__body">{{ post.body }}</div>
  </article>
{% endblock posts %}
```

### Erro 404

Dispara uma exceção 404

```python
from django.http import Http404, HttpRequest

def post(request: HttpRequest, post_id: int):
    found_post: dict[str, Any] | None = None

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break

    if found_post is None:
        raise Http404('Post não existe.')

```

### STATIC_ROOT E collectstatic

Em settings STATIC_ROOT é a pasta que vai receber os estáticos de todo o projeto

STATIC_ROOT = BASE_DIR / "static_files"

Ela será utilizada pelo servidor quando DEBUG = False

Ela deve estar no .gitignore

É possível utilizar o white noise, para servir arquivos estáticos com DEBUG = False
(lembrar de coletar os estáticos)


