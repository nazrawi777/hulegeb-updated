from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('products/', views.products, name='products'),
    path('services/', views.services, name='services'),
    path('blog/', views.blog, name='blog'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('contact/', views.contact, name='contact'),
    path('team/', views.team, name='team'),
    path('programmes/', views.programmes, name='programmes'),
    path('video-gallery/', views.image_gallery, name='video_gallery'),
    path('image-gallery/', views.image_gallery, name='image_gallery'),
    path('donation/', views.donation, name='donation'),
    path('ourhistory/', views.ourhistory, name='ourhistory'),
    path('store/', views.store, name='store'),
]
