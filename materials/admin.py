from django.contrib import admin

from .models import Folder, Material


@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon_class')

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'folder', 'icon_class')
    search_fields = ('title', 'folder__title')