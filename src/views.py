from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import BlogPost, Category, GalleryItem, HeroSlide, Product
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



def _absolute_media_url(request, url):
    """Return absolute URLs for uploaded media while leaving external URLs unchanged."""
    if not url:
        return ""
    if url.startswith(('http://', 'https://')):
        return url
    return request.build_absolute_uri(url)


def _product_to_dict(product, request):
    image_url = _absolute_media_url(request, product.get_image_url())
    return {
        'id': product.id,
        'name': product.name,
        'title': product.name,
        'slug': product.slug,
        'price': float(product.price),
        'currency': 'ETB',
        'description': product.description,
        'short_description': product.get_short_description(),
        'image': image_url,
        'images': [image_url] if image_url else [],
        'category': product.category.slug,
        'category_name': product.category.name,
        'subcategory': product.subcategory.slug if product.subcategory else 'all',
        'subcategory_name': product.subcategory.name if product.subcategory else '',
        'brand': 'Hulegeb',
        'sku': f'HLG-{product.id:04d}',
        'inventory': 0,
        'default_variant': 'default',
        'variants': [
            {
                'slug': 'default',
                'name': 'Default',
                'price': float(product.price),
                'inventory': 0,
                'images': ['front'],
            }
        ],
        'attributes': {
            'category': product.category.name,
            'subcategory': product.subcategory.name if product.subcategory else '',
        },
    }


def api_products(request):
    products = (
        Product.objects.filter(is_active=True, category__is_active=True)
        .select_related('category', 'subcategory')
    )
    data = [_product_to_dict(product, request) for product in products]
    return JsonResponse({'products': data})


def api_product_detail(request, product_id):
    product = get_object_or_404(
        Product.objects.select_related('category', 'subcategory'),
        pk=product_id,
        is_active=True,
        category__is_active=True,
    )
    return JsonResponse(_product_to_dict(product, request))


def api_categories(request):
    categories = Category.objects.filter(is_active=True).prefetch_related('subcategories')
    data = []
    for category in categories:
        data.append({
            'id': category.id,
            'name': category.name,
            'slug': category.slug,
            'subcategories': [
                {
                    'id': subcategory.id,
                    'name': subcategory.name,
                    'slug': subcategory.slug,
                }
                for subcategory in category.subcategories.all()
                if subcategory.is_active
            ],
        })
    return JsonResponse({'categories': data})
