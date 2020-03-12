from rest_framework.permissions import IsAdminUser , IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from .permissions import *

class TaskViewSet(ModelViewSet):
    model = Task
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [
        IsAuthorOrReadOnly,
    ]
    def list(self , request , *args , **kwargs):
        tasks = Task.objects.filter(user = request.user.id)
        context = {'request' : request}
        serializer = TaskSerializer(tasks , many=True , context = context)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

class TagViewSet(ModelViewSet):
    model = Tag
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [
        IsAuthenticated,
    ]

class UserViewSet(ModelViewSet):
    model = get_user_model()
    queryset = model.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [
    #     IsAdminUser,
    # ]

    def create(self, request, *args, **kwargs):
        if request.method == 'POST':
            serializer = UserSerializer(data = request.data)
            data = {}
            if serializer.is_valid():
                user = serializer.save()
                data['response'] = 'Succesfully registered a new user'
                data['username'] = user.username
                token = Token.objects.get(user = user).key
                data['token'] = token
            else :
                data = serializer.errors

            return Response(data)
