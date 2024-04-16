from django.test import TestCase
from django.contrib.auth.models import User

from .models import Post


class PostTest(TestCase):
    def setUp(self) -> None:
        fake_user = User.objects.create_user(username='testuser', password='12345')
        Post.objects.create(author=fake_user, title="title 1", text="simple text 1")
        Post.objects.create(author=fake_user, title="title 2", text="simple text 2")

    def test_animals_quantity(self):
        posts_quantity = Post.objects.count()
        self.assertEqual(posts_quantity, 2)

    def test_posts_list(self):
        response = self.client.get('/posts/')
        self.assertEqual(200, response.status_code)
