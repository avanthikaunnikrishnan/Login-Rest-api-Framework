from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apis import views
  
urlpatterns = [
    path('login',views.UserViewSet.as_view()),
]
  
urlpatterns = format_suffix_patterns(urlpatterns)