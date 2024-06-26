
from django.contrib import admin
from django.urls import path

from api_view import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Bu APIVIEW uchun
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    # mixin
    path('snippets/', views.SnippetListMixin.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetailMixin.as_view()),

]
