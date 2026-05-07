from django.shortcuts import render, get_object_or_404
from .models import HeroSlide, GalleryItem, BlogPost
from django.core.paginator import Paginator


def index(request):
    hero_slides = HeroSlide.objects.filter(is_active=True)
    return render(request, 'index.html', {'hero_slides': hero_slides})


def about(request):
    return render(request, 'about.html')


def products(request):
    return render(request, 'products.html')


def services(request):
    return render(request, 'services.html')


def blog(request):
    blog_posts = BlogPost.objects.filter(is_published=True)
    paginator = Paginator(blog_posts, 9)  # 9 posts per page
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'blog.html', {'page_obj': page_obj})


def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, is_published=True)
    return render(request, 'blog-detail.html', {'post': post})


def contact(request):
    return render(request, 'contact.html')


def team(request):
    return render(request, 'team.html')


def programmes(request):
    return render(request, 'programmes.html')


def video_gallery(request):
    return render(request, 'video-gallery.html')


def image_gallery(request):
    gallery_items = GalleryItem.objects.filter(is_active=True)
    paginator = Paginator(gallery_items, 12)  # 12 items per page
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'image-gallery.html', {'page_obj': page_obj})


def donation(request):
    return render(request, 'donation.html')


def ourhistory(request):
    return render(request, 'ourhistory.html')


def store(request):
    return render(request, 'store.html')


def page_404(request, exception=None):
    return render(request, '404.html', status=404)

