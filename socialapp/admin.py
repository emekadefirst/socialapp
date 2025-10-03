from django.contrib import admin
from .models import Post, Comment, Like


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'caption', 'created_at', 'like_count', 'comment_count']
    search_fields = ['caption']
    list_filter = ['created_at', 'updated_at']
    readonly_fields = ['id', 'created_at', 'updated_at', 'like_count', 'comment_count']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'text', 'created_at']
    search_fields = ['text', 'post__caption']
    list_filter = ['created_at']
    readonly_fields = ['id', 'created_at']

class LikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'like', 'created_at']
    search_fields = ['post__caption']
    list_filter = ['created_at', 'like']
    readonly_fields = ['id', 'created_at']


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like, LikeAdmin)