from django.contrib import admin
from django.utils.html import format_html
from .models import (
    BankAccount,
    BlogPost,
    Category,
    DonationPurpose,
    GalleryItem,
    HeroSlide,
    Product,
    Programme,
    SubCategory,
    TeamMember,
)

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





class SubCategoryInline(admin.TabularInline):
    model = SubCategory
    extra = 1
    fields = ('name', 'slug', 'order', 'is_active')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'order', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'slug')
    list_editable = ('order', 'is_active')
    prepopulated_fields = {'slug': ('name',)}
    inlines = (SubCategoryInline,)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'slug', 'order', 'is_active', 'created_at')
    list_filter = ('category', 'is_active', 'created_at')
    search_fields = ('name', 'slug', 'category__name')
    list_editable = ('order', 'is_active')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_preview', 'name', 'category', 'subcategory', 'price', 'order', 'is_active', 'created_at')
    list_filter = ('category', 'subcategory', 'is_active', 'created_at')
    search_fields = ('name', 'description', 'short_description')
    list_editable = ('price', 'order', 'is_active')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('product_preview_large',)
    fieldsets = (
        ('Product Information', {
            'fields': ('name', 'slug', 'category', 'subcategory', 'price', 'short_description', 'description')
        }),
        ('Product Image', {
            'fields': ('product_preview_large', 'image', 'image_url'),
            'description': 'Upload a product image OR provide an external URL.'
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active')
        }),
    )

    def product_preview(self, obj):
        img_url = obj.get_image_url()
        if img_url:
            return format_html(
                '<img src="{}" style="width: 60px; height: 60px; object-fit: cover; border-radius: 4px;" />',
                img_url,
            )
        return '-'
    product_preview.short_description = 'Preview'

    def product_preview_large(self, obj):
        img_url = obj.get_image_url()
        if img_url:
            return format_html(
                '<img src="{}" style="max-width: 400px; max-height: 300px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);" />',
                img_url,
            )
        return 'No product image yet'
    product_preview_large.short_description = 'Current Product Image'


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('image_preview', 'name', 'role', 'phone', 'email', 'order', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'role', 'phone', 'email')
    list_editable = ('order', 'is_active')
    ordering = ('order', 'name')
    readonly_fields = ('image_preview_large',)
    fieldsets = (
        ('Team Member Information', {
            'fields': ('name', 'role', 'phone', 'email')
        }),
        ('Image Source (Choose One)', {
            'fields': ('image_preview_large', 'image', 'image_url'),
            'description': 'Upload a team member image OR provide an external URL. At least one is required.'
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active')
        }),
    )

    def image_preview(self, obj):
        img_url = obj.get_image_url()
        if img_url:
            return format_html(
                '<img src="{}" style="width: 60px; height: 60px; object-fit: cover; border-radius: 4px;" />',
                img_url,
            )
        return '-'
    image_preview.short_description = 'Preview'

    def image_preview_large(self, obj):
        img_url = obj.get_image_url()
        if img_url:
            return format_html(
                '<img src="{}" style="max-width: 400px; max-height: 300px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);" />',
                img_url,
            )
        return 'No team member image yet'
    image_preview_large.short_description = 'Current Team Member Image'


@admin.register(Programme)
class ProgrammeAdmin(admin.ModelAdmin):
    list_display = ('image_preview', 'title', 'order', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title', 'description')
    list_editable = ('order', 'is_active')
    ordering = ('order', 'title')
    readonly_fields = ('image_preview_large',)
    fieldsets = (
        ('Programme Information', {
            'fields': ('title', 'description')
        }),
        ('Image Source (Choose One)', {
            'fields': ('image_preview_large', 'image', 'image_url'),
            'description': 'Upload a programme image OR provide an external URL. At least one is required.'
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active')
        }),
    )

    def image_preview(self, obj):
        img_url = obj.get_image_url()
        if img_url:
            return format_html(
                '<img src="{}" style="width: 80px; height: 50px; object-fit: cover; border-radius: 4px;" />',
                img_url,
            )
        return '-'
    image_preview.short_description = 'Preview'

    def image_preview_large(self, obj):
        img_url = obj.get_image_url()
        if img_url:
            return format_html(
                '<img src="{}" style="max-width: 500px; max-height: 300px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);" />',
                img_url,
            )
        return 'No programme image yet'
    image_preview_large.short_description = 'Current Programme Image'


class BankAccountInline(admin.TabularInline):
    model = BankAccount
    extra = 1
    fields = ('bank_name', 'account_number', 'account_holder', 'order', 'is_active')


@admin.register(DonationPurpose)
class DonationPurposeAdmin(admin.ModelAdmin):
    list_display = ('label', 'order', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('label',)
    list_editable = ('order', 'is_active')
    ordering = ('order', 'label')
    inlines = (BankAccountInline,)


@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('bank_name', 'account_number', 'account_holder', 'purpose', 'order', 'is_active', 'created_at')
    list_filter = ('purpose', 'is_active', 'created_at')
    search_fields = ('bank_name', 'account_number', 'account_holder', 'purpose__label')
    list_editable = ('order', 'is_active')
    ordering = ('order', 'bank_name', 'account_number')

