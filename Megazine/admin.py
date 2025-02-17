from django.contrib import admin
from Megazine.models import Article, ArticleSection, ArticleImage, Category, Tag, Comment

# Register your models here.


class ArticleSectionInline(admin.TabularInline):
    model = ArticleSection
    extra = 1

class ArticleImageInline(admin.TabularInline):
    model = ArticleImage
    extra = 1

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'is_published', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ArticleSectionInline, ArticleImageInline]
    filter_horizontal = ('tags',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'article', 'created_at')
