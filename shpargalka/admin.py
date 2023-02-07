from django.contrib import admin
from django import forms
from .models import Article, CategoryArticle, CategoryTreeArticle, ArticleTree
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin


class ArticleAdminForm(forms.ModelForm):
    anons = forms.CharField(widget=CKEditorUploadingWidget())
    full_text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Article
        fields = '__all__'

# Дерево категорий с сортировкой перетаскиванием (Draggable)
@admin.register(CategoryTreeArticle)
class CategoryArticleTreeAdmin(DraggableMPTTAdmin):
    mptt_indent_field = 'name_cat'
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug_cat': ('name_cat',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = CategoryTreeArticle.objects.add_related_count(
                qs,
                ArticleTree,
                'category_article',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = CategoryTreeArticle.objects.add_related_count(qs,
                 ArticleTree,
                 'category_article',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Products in category'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Products in tree'


# Статьи для дерева категории (сортировка по полю number_post)
@admin.register(ArticleTree)
class ArticleTreeAdmin(admin.ModelAdmin):
    list_display = [
        'number_post', 'title', 'slug_article', 'category_article', 'draft',
        'created', 'updated', 'id',
    ]
    prepopulated_fields = {'slug_article': ('title',)}
    list_filter = [
        'title', 'category_article', 'created', 'updated'
    ]
    list_editable = ['number_post', 'draft']

    list_display_links = ['id', 'title', 'category_article']

    fields = [
        'title', 'slug_article', 'number_post', 'category_article', 'anons', 'full_text', 'image_article', 'draft',
        'created', 'updated'
    ]
    form = ArticleAdminForm
    readonly_fields = ['created', 'updated']





@admin.register(CategoryArticle)
class CategoryArticleAdmin(admin.ModelAdmin):
    list_display = ['name_cat', 'slug_cat', 'description_cat']
    # Поле 'slug' заполняетя автоматически на основе поля 'name'
    prepopulated_fields = {'slug_cat': ('name_cat',)}
    fields = ['name_cat', 'slug_cat', 'description_cat']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        'number_post', 'title', 'slug_article', 'category_article', 'draft',
        'created', 'updated', 'id',
    ]
    prepopulated_fields = {'slug_article': ('title',)}
    list_filter = [
        'title', 'category_article', 'created', 'updated'
    ]
    list_editable = ['number_post', 'draft']

    list_display_links = ['id', 'title', 'category_article']

    fields = [
        'title', 'slug_article', 'number_post', 'category_article', 'anons', 'full_text', 'image_article', 'draft',
        'created', 'updated'
    ]
    form = ArticleAdminForm
    readonly_fields = ['created', 'updated']


