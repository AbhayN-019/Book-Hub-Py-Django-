"""
URL configuration for book_hub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from bookhub_app.views import book_view,book_list,single_book_view,update_book_view,delete_book,welcome

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',welcome,name='home_page'),
    path('book_post/',book_view,name='add_book'),
    path('book_list/',book_list,name='book_list'),
    path('single_book/<int:id>/',single_book_view,name='solo_book'),
    path('update_book/<int:id>/',update_book_view,name='update_book'),
    path('delete_book/<int:id>/',delete_book,name='delete_book'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
