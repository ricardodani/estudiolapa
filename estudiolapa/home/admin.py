from django.conf import settings
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, CategoryPhoto, Background, Work, WorkPhoto


class ThumbAdminMixin(object):

    THUMB_SETTINGS = {
        'size': getattr(settings, 'THUMBNAIL_ADMIN_SIZE', '100x80'),
        'crop': getattr(settings, 'THUMBNAIL_ADMIN_CROP', 'center')
    }

    def _get_thumbnail(self, instance):
        thumb = instance._get_thumbnail(
            self.THUMB_SETTINGS['size'], crop=self.THUMB_SETTINGS['crop']
        )
        if thumb:
            return mark_safe('<img src="{}" />'.format(thumb.url))
    _get_thumbnail.short_description = u'Thumb'


class CategoryPhotoInline(admin.TabularInline):
    model = CategoryPhoto
    extra = 1


class CategoryAdmin(admin.ModelAdmin, ThumbAdminMixin):
    inlines = (CategoryPhotoInline,)
    list_display = ['title', '_get_thumbnail', 'image']
    list_editable = ['image']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['title']


class WorkPhotoInline(admin.TabularInline):
    model = WorkPhoto
    extra = 1


class WorkAdmin(admin.ModelAdmin, ThumbAdminMixin):
    inlines = (WorkPhotoInline,)
    list_display = ['title', 'category', '_get_thumbnail', 'image']
    list_editable = ['image']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['title']


class BackgroundAdmin(admin.ModelAdmin, ThumbAdminMixin):
    list_display = ['title', 'place', '_get_thumbnail', 'image']
    list_editable = ['image']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['title']


class WorkPhotoAdmin(admin.ModelAdmin, ThumbAdminMixin):
    list_display = ['title', 'work', '_get_thumbnail', 'image']
    list_editable = ['image']
    list_filter = ['created_at', 'updated_at', 'work']
    search_fields = ['title']


class CategoryPhotoAdmin(admin.ModelAdmin, ThumbAdminMixin):
    list_display = ['title', 'category', '_get_thumbnail', 'image']
    list_editable = ['image']
    list_filter = ['created_at', 'updated_at', 'category']
    search_fields = ['title']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Work, WorkAdmin)
admin.site.register(Background, BackgroundAdmin)
admin.site.register(WorkPhoto, WorkPhotoAdmin)
admin.site.register(CategoryPhoto, CategoryPhotoAdmin)
admin.site.site_title = 'EstudioLapa.com - Admin'
admin.site.site_header = 'Estudio Lapa Admin'
admin.site.index_title = 'Bem vindo, Rodrigo e Clau, aqui editas o site!'
