from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Post

class PostViewTests(APITestCase):

    def setUp(self):
        self.url = reverse('list_and_create') 
        self.post1 = Post.objects.create(username='Username 1',title='Post 1', content='Content for post 1')
        self.post2 = Post.objects.create(username='Username 2',title='Post 2', content='Content for post 2')

    def test_get_posts(self):

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  
        self.assertEqual(response.data[0]['title'], self.post1.title)
        self.assertEqual(response.data[1]['title'], self.post2.title)
        self.assertEqual(response.data[0]['content'], self.post1.content)
        self.assertEqual(response.data[1]['content'], self.post2.content)
    
    def test_post_create(self):

        new_post_data = {
            'username': 'Username 3',
            'title': 'Post 3',
            'content': 'Content for post 3'
        }

        response = self.client.post(self.url, new_post_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(response.data['username'], new_post_data['username'])
        self.assertEqual(response.data['title'], new_post_data['title'])
        self.assertEqual(response.data['content'], new_post_data['content'])

        post = Post.objects.get(id=response.data['id'])
        self.assertEqual(post.username, new_post_data['username'])
        self.assertEqual(post.title, new_post_data['title'])
        self.assertEqual(post.content, new_post_data['content'])

    def test_post_create_invalid_data(self):

        invalid_post_data = {
            'username': 'Username 3',
        }

        response = self.client.post(self.url, invalid_post_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_create_blank_data(self):
        invalid_post_data = {
            'username': '',
            'title': '',
            'content': ''
        }
        response = self.client.post(self.url, invalid_post_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_post(self):
        urlWithId = reverse('get_update_delete', kwargs={'id': self.post1.id})
        response = self.client.get(urlWithId)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.post1.username)
        self.assertEqual(response.data['title'], self.post1.title)
        self.assertEqual(response.data['content'], self.post1.content)

    def test_get_invalid_post(self):

        urlWithId = reverse('get_update_delete', kwargs={'id': 100})
        response = self.client.get(urlWithId)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    