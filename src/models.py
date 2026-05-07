from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify


class BlogPost(models.Model):
    """Blog post model"""
    title = models.CharField(max_length=300, help_text="Blog post title")
    slug = models.SlugField(max_length=300, unique=True, blank=True, help_text="URL-friendly version of title")
    excerpt = models.TextField(max_length=500, help_text="Short description/summary")
    content = models.TextField(help_text="Full blog post content")
    
    # Featured image
    featured_image = models.ImageField(upload_to='blog/', blank=True, null=True, help_text="Upload featured image")
    featured_image_url = models.URLField(max_length=500, blank=True, help_text="Or provide external image URL")
    image_alt = models.CharField(max_length=200, default="Blog post image")
    
    # Metadata
    author = models.CharField(max_length=100, default="Hulegeb Team")
    published_date = models.DateField(help_text="Publication date")
    is_published = models.BooleanField(default=True, help_text="Show on website")
    is_featured = models.BooleanField(default=False, help_text="Feature on homepage")
    
    # SEO
    meta_description = models.CharField(max_length=160, blank=True, help_text="SEO meta description")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_date', '-created_at']
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def clean(self):
        """Validate that either featured_image or featured_image_url is provided"""
        if not self.featured_image and not self.featured_image_url:
            raise ValidationError('You must provide either an uploaded image or an image URL.')
        
    def get_featured_image_url(self):
        """Return featured image URL"""
        if self.featured_image:
            return self.featured_image.url
        return self.featured_image_url or ""
    
    def get_absolute_url(self):
        """Return URL for blog post detail page"""
        from django.urls import reverse
        return reverse('blog_detail', kwargs={'slug': self.slug})


class GalleryItem(models.Model):
    """Gallery item supporting both images and videos"""
    MEDIA_TYPE_CHOICES = [
        ('image', 'Image'),
        ('video', 'Video'),
    ]
    
    title = models.CharField(max_length=200, help_text="Media title or caption")
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPE_CHOICES, default='image', help_text="Type of media")
    
    # Image fields
    image = models.ImageField(upload_to='gallery/images/', blank=True, null=True, help_text="Upload an image file")
    image_url = models.URLField(max_length=500, blank=True, help_text="Or provide an external image URL")
    
    # Video fields
    video = models.FileField(upload_to='gallery/videos/', blank=True, null=True, help_text="Upload a video file (MP4, WebM)")
    video_url = models.URLField(max_length=500, blank=True, help_text="Or provide an external video URL (YouTube, Vimeo, etc.)")
    video_thumbnail = models.ImageField(upload_to='gallery/thumbnails/', blank=True, null=True, help_text="Thumbnail for video")
    
    alt_text = models.CharField(max_length=200, default="Gallery media")
    order = models.IntegerField(default=0, help_text="Display order (lower numbers first)")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = "Gallery Item"
        verbose_name_plural = "Gallery Items"

    def __str__(self):
        return f"{self.title} ({self.get_media_type_display()})"

    def clean(self):
        """Validate that appropriate media is provided based on type"""
        if self.media_type == 'image':
            if not self.image and not self.image_url:
                raise ValidationError('You must provide either an uploaded image or an image URL for image type.')
        elif self.media_type == 'video':
            if not self.video and not self.video_url:
                raise ValidationError('You must provide either an uploaded video or a video URL for video type.')
        
    def get_media_url(self):
        """Return media URL based on type"""
        if self.media_type == 'image':
            if self.image:
                return self.image.url
            return self.image_url or ""
        elif self.media_type == 'video':
            if self.video:
                return self.video.url
            return self.video_url or ""
        return ""
    
    def get_thumbnail_url(self):
        """Return thumbnail URL for videos"""
        if self.media_type == 'video' and self.video_thumbnail:
            return self.video_thumbnail.url
        return None
    
    def is_youtube_video(self):
        """Check if video URL is from YouTube"""
        if self.video_url:
            return 'youtube.com' in self.video_url or 'youtu.be' in self.video_url
        return False
    
    def get_youtube_embed_url(self):
        """Convert YouTube URL to embed URL"""
        if not self.is_youtube_video():
            return None
        
        video_url = self.video_url
        if 'youtu.be/' in video_url:
            video_id = video_url.split('youtu.be/')[-1].split('?')[0]
        elif 'watch?v=' in video_url:
            video_id = video_url.split('watch?v=')[-1].split('&')[0]
        else:
            return None
        
        return f"https://www.youtube.com/embed/{video_id}"


class HeroSlide(models.Model):
    """Hero slider content manageable through admin"""
    title = models.CharField(max_length=200, default="Hulegeb")
    heading_part1 = models.CharField(max_length=200, default="Weaving")
    heading_part2 = models.CharField(max_length=200, default="Dignity")
    heading_part3 = models.CharField(max_length=200, default=", Crafting Independence")
    description = models.TextField(
        default="For over 70 years, Hulegeb has been led by and for Ethiopia's blind and physically disabled community — turning skill into steady, dignified livelihoods."
    )
    image = models.ImageField(upload_to='hero_slides/', blank=True, null=True, help_text="Upload an image file")
    image_url = models.URLField(
        max_length=500,
        blank=True,
        help_text="Or provide an external image URL"
    )
    image_alt = models.CharField(max_length=200, default="Hulegeb artisans at work")
    order = models.IntegerField(default=0, help_text="Display order (lower numbers first)")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = "Hero Slide"
        verbose_name_plural = "Hero Slides"

    def __str__(self):
        return f"{self.title} - {self.heading_part1} {self.heading_part2}"

    def clean(self):
        """Validate that either image or image_url is provided"""
        if not self.image and not self.image_url:
            raise ValidationError('You must provide either an uploaded image or an image URL.')

    def get_image_url(self):
        """Return image URL - either uploaded file or external URL"""
        if self.image:
            return self.image.url
        return self.image_url or "https://i.postimg.cc/VvQRbrh9/L2A6687.jpg"


class Category(models.Model):
    """Product category shown on the store filter bar."""
    name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=140, unique=True, blank=True)
    order = models.PositiveIntegerField(default=0, help_text="Display order (lower numbers first)")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class SubCategory(models.Model):
    """Product subcategory nested under a category."""
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=140, blank=True)
    order = models.PositiveIntegerField(default=0, help_text="Display order (lower numbers first)")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'name']
        unique_together = ('category', 'slug')
        verbose_name = "Product Subcategory"
        verbose_name_plural = "Product Subcategories"

    def __str__(self):
        return f"{self.category.name} - {self.name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Product(models.Model):
    """Store product manageable through Django admin."""
    category = models.ForeignKey(Category, related_name='products', on_delete=models.PROTECT)
    subcategory = models.ForeignKey(
        SubCategory,
        related_name='products',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    short_description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True, help_text="Upload a product image")
    image_url = models.URLField(max_length=500, blank=True, help_text="Or provide an external image URL")
    is_active = models.BooleanField(default=True, help_text="Show product on website")
    order = models.PositiveIntegerField(default=0, help_text="Display order (lower numbers first)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def clean(self):
        if self.subcategory and self.subcategory.category_id != self.category_id:
            raise ValidationError('Selected subcategory must belong to the selected category.')

    def get_image_url(self):
        if self.image:
            return self.image.url
        return self.image_url or ""

    def get_short_description(self):
        if self.short_description:
            return self.short_description
        return self.description[:180]
