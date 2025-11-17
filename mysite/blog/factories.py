import factory
from django.contrib.auth.models import User
from blog.post import Post


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f"user{n}")


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    author = factory.SubFactory(UserFactory)
    title = "default title"
    content = "default content"
