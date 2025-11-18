from django.contrib import admin
from .post import Post  # ponto = relativo à pasta blog

admin.site.register(Post)
