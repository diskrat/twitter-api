from django.urls import path, include
from rest_framework.routers import DefaultRouter

from posts import views

router = DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'register',views.RegistrationViewSet,basename='register')


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)), 
    path('api-auth/', include('rest_framework.urls')),
    
]