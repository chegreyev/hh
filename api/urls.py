from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('task' , TaskViewSet , basename='tasks')
router.register('tag' , TagViewSet , basename='tags')
router.register('register' , UserViewSet , basename= 'register')
urlpatterns = router.urls