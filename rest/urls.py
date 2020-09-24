
from django.urls import path
from .views import PropertyView,PropertytDestroyAPIView,PropertyUpdateAPIView,PropertyCreateAPIView
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
  # path('api/search/',UserPropertyListView.as_view(), name = 'user-projects'),
  path('api/properties/', views.PropertyView.as_view()),
  path('api/properties/update>', views.PropertyUpdateAPIView.as_view()),
  path('api/properties/create', views.PropertyCreateAPIView.as_view()), 
  path('api/properties/delete', views.PropertytDestroyAPIView.as_view())
  
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)