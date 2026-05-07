from django.contrib import admin
from django.utils.html import format_html
from .models import HeroSlide, GalleryItem, BlogPost

# Customize admin site header and title
admin.site.site_header = 'Hulegeb Training & Rehabilitation'
admin.site.site_title = 'Hulegeb Admin'
admin.site.index_title = 'Content Management'


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('image_preview', 'title', 'author', 'published_date', 'is_published', 'is_featured', 'created_at')
    list_filter = ('is_published', 'is_featured', 'published_date', 'created_at')
    search_fields = ('title', 'excerpt', 'content', 'author')
    list_editable = ('is_published', 'is_featured')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_date'
    ordering = ('-published_date', '-created_at')
    readonly_fields = ('image_preview_large',)
    
    fieldsets = (
        ('Content', {
            'fields': ('title', 'slug', 'excerpt', 'content', 'author')
        }),
        ('Featured Image (Choose One)', {
            'fields': ('image_preview_large', 'featured_image', 'featured_image_url', 'image_alt'),
            'description': 'Upload an image file OR provide an external URL. At least one is required.'
        }),
        ('Publishing', {
            'fields': ('published_date', 'is_published', 'is_featured')
        }),
        ('SEO', {
            'fields': ('meta_description',),
            'classes': ('collapse',)
        }),
    )
    
    def image_preview(self, obj):
        """Small thumbnail for list view"""
        img_url = obj.get_featured_image_url()
        if img_url:
            return format_html(
                '<img src="{}" style="width: 60px; height: 60px; object-fit: cover; border-radius: 4px;" />',
                img_url
            )
        return '-'
    image_preview.short_description = 'Preview'
    
    def image_preview_large(self, obj):
        """Large preview for detail view"""
        img_url = obj.get_featured_image_url()
        if img_url:
            return format_html(
                '<img src="{}" style="max-width: 400px; max-height: 300px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);" />',
                img_url
            )
        return 'No image uploaded yet'
    image_preview_large.short_description = 'Current Image'


@admin.register(GalleryItem)
class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ('media_preview', 'title', 'media_type', 'order', 'is_active', 'has_uploaded_media', 'created_at')
    list_filter = ('media_type', 'is_active', 'created_at')
    search_fields = ('title', 'alt_text')
    list_editable = ('order', 'is_active')
    ordering = ('order', '-created_at')
    readonly_fields = ('media_preview_large',)
    
    fieldsets = (
        ('Media Information', {
            'fields': ('title', 'media_type', 'alt_text')
        }),
        ('Current Media', {
            'fields': ('media_preview_large',),
            'description': 'Preview of current media'
        }),
        ('Image Source (for Image type)', {
            'fields': ('image', 'image_url'),
            'description': 'Upload an image file OR provide an external URL.'
        }),
        ('Video Source (for Video type)', {
            'fields': ('video', 'video_url', 'video_thumbnail'),
            'description': 'Upload a video file OR provide an external URL (YouTube, Vimeo, etc.). Optionally add a thumbnail.'
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active')
        }),
    )
    
    def media_preview(self, obj):
        """Small thumbnail for list view"""
        if obj.media_type == 'image':
            img_url = obj.get_media_url()
            if img_url:
                return format_html(
                    '<img src="{}" style="width: 60px; height: 60px; object-fit: cover; border-radius: 4px;" />',
                    img_url
                )
        elif obj.media_type == 'video':
            thumbnail_url = obj.get_thumbnail_url()
            if thumbnail_url:
                return format_html(
                    '<div style="position: relative; width: 60px; height: 60px;">'
                    '<img src="{}" style="width: 60px; height: 60px; object-fit: cover; border-radius: 4px;" />'
                    '<span style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: white; font-size: 20px;">▶</span>'
                    '</div>',
                    thumbnail_url
                )
            else:
                return format_html(
                    '<div style="width: 60px; height: 60px; background: #333; border-radius: 4px; display: flex; align-items: center; justify-content: center; color: white; font-size: 20px;">▶</div>'
                )
        return '-'
    media_preview.short_description = 'Preview'
    
    def media_preview_large(self, obj):
        """Large preview for detail view"""
        if obj.media_type == 'image':
            img_url = obj.get_media_url()
            if img_url:
                return format_html(
                    '<img src="{}" style="max-width: 400px; max-height: 300px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);" />',
                    img_url
                )
        elif obj.media_type == 'video':
            thumbnail_url = obj.get_thumbnail_url()
            video_url = obj.get_media_url()
            
            if obj.is_youtube_video():
                embed_url = obj.get_youtube_embed_url()
                if embed_url:
                    return format_html(
                        '<div style="max-width: 400px;">'
                        '<iframe width="400" height="225" src="{}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 8px;"></iframe>'
                        '</div>',
                        embed_url
                    )
            elif thumbnail_url:
                return format_html(
                    '<div style="position: relative; max-width: 400px;">'
                    '<img src="{}" style="max-width: 400px; max-height: 300px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);" />'
                    '<div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); background: rgba(0,0,0,0.7); width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 24px;">▶</div>'
                    '</div>',
                    thumbnail_url
                )
            elif video_url:
                return format_html(
                    '<video width="400" controls style="max-height: 300px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">'
                    '<source src="{}" type="video/mp4">'
                    'Your browser does not support the video tag.'
                    '</video>',
                    video_url
                )
        return 'No media uploaded yet'
    media_preview_large.short_description = 'Current Media'
    
    def has_uploaded_media(self, obj):
        if obj.media_type == 'image':
            return bool(obj.image)
        elif obj.media_type == 'video':
            return bool(obj.video)
        return False
    has_uploaded_media.boolean = True
    has_uploaded_media.short_description = 'Uploaded'


@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    list_display = ('image_preview', 'title', 'heading_part1', 'heading_part2', 'order', 'is_active', 'has_uploaded_image', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title', 'heading_part1', 'heading_part2', 'description')
    list_editable = ('order', 'is_active')
    ordering = ('order', '-created_at')
    readonly_fields = ('image_preview_large',)
    
    fieldsets = (
        ('Content', {
            'fields': ('title', 'heading_part1', 'heading_part2', 'heading_part3', 'description')
        }),
        ('Image Source (Choose One)', {
            'fields': ('image_preview_large', 'image', 'image_url', 'image_alt'),
            'description': 'Upload an image file OR provide an external URL. At least one is required.'
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active')
        }),
    )
    
    def image_preview(self, obj):
        """Small thumbnail for list view"""
        img_url = obj.get_image_url()
        if img_url:
            return format_html(
                '<img src="{}" style="width: 80px; height: 50px; object-fit: cover; border-radius: 4px;" />',
                img_url
            )
        return '-'
    image_preview.short_description = 'Preview'
    
    def image_preview_large(self, obj):
        """Large preview for detail view"""
        img_url = obj.get_image_url()
        if img_url:
            return format_html(
                '<img src="{}" style="max-width: 600px; max-height: 300px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);" />',
                img_url
            )
        return 'No image uploaded yet'
    image_preview_large.short_description = 'Current Image'
    
    def has_uploaded_image(self, obj):
        return bool(obj.image)
    has_uploaded_image.boolean = True
    has_uploaded_image.short_description = 'Uploaded'



