"""myblog URL Configuration


"""
from django.contrib import admin
from django.urls import path, include
from blog import views as blog_view
from blog import views
urlpatterns = [
    path('site/', views.sites, name='site'),
    path('', blog_view.Index.as_view()),
    path('search/', blog_view.Search.as_view(), name='search'),
    path('comment/', blog_view.pub_comment, name='comment'),
    path('category/<int:category>', blog_view.CategoryList.as_view(), name='category'),
    path('detail/<int:pk>', blog_view.ArticleDetail.as_view(), name='detail'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),

]
