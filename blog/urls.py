from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from post import views
from post.views import (
    index,
    home,
    blog,
    post,
    search,
    category_search,
    post_create,
    post_update,
    post_delete,
    )



urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('', home),
    path('blog/', blog, name= 'post-list'),
    path('post/<id>', post, name= 'post-detail'),
    path('create/', post_create, name= 'post-create'),
    path('post/<id>/update/', post_update, name= 'post-update'),
    path('post/<id>/delete/', post_delete, name= 'post-delete'),
    path('search/', search, name='search'),
    path('category_search/', category_search, name='category-search'),
    #path('tinymce/', include('tinymce.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
