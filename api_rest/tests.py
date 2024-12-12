from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Post

class PostTests(APITestCase):
    def setUp(self):

        self.url = reverse('post-list')  
        self.create_url = reverse('post-list') 
        self.post_data = {
            'username': 'testuser',
            'title': 'Test Post',
            'content': 'This is a test post content.',
        }
        self.post = Post.objects.create(**self.post_data)

    def test_create_post(self):

        response = self.client.post(self.create_url, self.post_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 2)  
        self.assertEqual(Post.objects.latest('id').title, 'Test Post')  

    def test_list_posts(self):

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  
    def test_retrieve_post(self):
        
        url = reverse('post-detail', args=[self.post.id])  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Post')  

    def test_update_post(self):
        
        url = reverse('post-detail', args=[self.post.id])  
        updated_data = {
            'title': 'Updated Test Post',
            'content': 'Updated content for the test post.',
        }
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.post.refresh_from_db()  
        self.assertEqual(self.post.title, 'Updated Test Post')  

    def test_partial_update_post(self):

        url = reverse('post-detail', args=[self.post.id])
        partial_data = {
            'title': 'Partially Updated Test Post',
        }
        response = self.client.patch(url, partial_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Partially Updated Test Post')  

    def test_delete_post(self):

        url = reverse('post-detail', args=[self.post.id])  
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 0)  

    def test_create_post_missing_fields(self):
        incomplete_data = {
            'username': 'testuser',  
        }
        response = self.client.post(self.create_url, incomplete_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('title', response.data)  
        self.assertIn('content', response.data)  

    def test_list_multiple_posts(self):
        post_data2 = {
            'username': 'anotheruser',
            'title': 'Another Test Post',
            'content': 'This is another test post content.',
        }
        Post.objects.create(**post_data2)  
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  

    def test_retrieve_nonexistent_post(self):
        url = reverse('post-detail', args=[99999])  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_post_invalid_data(self):
        url = reverse('post-detail', args=[self.post.id])  
        invalid_data = {
            'title': '',  
            'content': 'Updated content for the test post.',
        }
        response = self.client.put(url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('title', response.data)  

    def test_delete_nonexistent_post(self):
        url = reverse('post-detail', args=[99999])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
