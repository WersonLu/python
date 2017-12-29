from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Post


# 定制管理详情页面
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')

    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')

    # 自动填充plug(构建文章的url)
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']


admin.site.register(Post, PostAdmin)
