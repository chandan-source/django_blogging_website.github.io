"""Blogging URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from blog.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('foods/<int:cid>/', foods, name='foods'),
    path('lifestyle/<int:cid>/', lifestyle, name='lifestyle'),
    path('fashion/<int:cid>/', fashion, name='fashion'),
    path('signup', signup, name='signup'),
    path('login', login_user, name='login'),
    path('logout', logout_user, name='logout'),
    path('add_blog', user_blog_form, name='add_blog'),
    path('add_category', admin_category_form, name='add_category'),
    path('blog_detail/<int:bid>/',blog_detail,name='blog_detail'),
    path('comment/<int:bid>/', blog_detail, name='comment'),
    path('like/<int:bid>/', blog_like, name='blog_like'),
    path('dashboard/<str:type>/', user_dashboard, name='dashboard'),
    path('edit_blog/<int:bid>/', edit_blog, name='edit_blog'),
    path('delete_blog/<int:bid>/', delete_blog, name='delete_blog'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
