from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Post
from .serializers import PostSerializer

@api_view(['GET','POST'])
def list_and_create(request):

    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        new_post = request.data
        serializer = PostSerializer(data=new_post)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def get_update_delete(request,id):

    try:
        post = Post.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializar = PostSerializer(post)
        return Response(serializar.data)
    
    if request.method == 'PUT':
        serializar = PostSerializer(post, data=request.data)
        if serializar.is_valid():
            serializar.save()
            return Response(serializar.data, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':    
        try:
            post.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)



    
