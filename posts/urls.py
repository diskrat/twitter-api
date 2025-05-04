from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rest_framework_nested.routers import NestedDefaultRouter
from posts import views

router = DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'register',views.RegistrationViewSet,basename='register')

posts_router = NestedDefaultRouter(router,r'posts',lookup='post')
posts_router.register(r'likes',views.LikeViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('',include(posts_router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    
]