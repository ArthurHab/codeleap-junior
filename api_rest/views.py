from rest_framework.viewsets import ModelViewSet
from .models import Post
from .serializers import PostCreateSerializer, PostEditSerializer, PostListSerializer

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()

    def get_serializer_class(self):

        if self.action == 'create':
            return PostCreateSerializer  
        elif self.action in ['update', 'partial_update']:
            return PostEditSerializer 
        elif self.action == 'list' or self.action == 'retrieve':
            return PostListSerializer  
        return super().get_serializer_class()