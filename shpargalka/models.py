from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
import mptt
from django.utils import timezone
from mptt.models import MPTTModel, TreeForeignKey


class CategoryTreeArticle(MPTTModel):
    #  Дерево категорий
    name_cat = models.CharField('Категория статьи', max_length=150)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', verbose_name='РОДИТЕЛЬСКИЙ класс',
                            on_delete=models.CASCADE)
    slug_cat = models.SlugField(max_length=160, unique=True)
    description_cat = models.TextField('Описание категории', blank=True)

    def __str__(self):
        return self.name_cat

    class Meta:
        verbose_name = '-Категория (Tree)'
        verbose_name_plural = '-- Категории (Tree)'
        db_table = 'category_tree'
        ordering = ('tree_id', 'level')

    class MPTTMeta:
        order_insertion_by = ['name_cat']

    def get_absolute_url(self, ):
        return reverse('category_product', args=[self.id, self.slug_cat])


mptt.register(CategoryTreeArticle, order_insertion_by=['name_cat'])


class CategoryArticle(models.Model):
    #  Категория статьи
    name_cat = models.CharField('Категория статьи', max_length=150)
    slug_cat = models.SlugField(max_length=160, unique=True)
    description_cat = models.TextField('Описание категории', blank=True)

    def __str__(self):
        return self.name_cat

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('article_by_category', args=[self.slug_cat])


# class CategoryPost(MPTTModel):
#     #  Категория статьи
#     name_cat = models.CharField('Категория поста', max_length=150)
#     slug_cat = models.SlugField(max_length=160, unique=True)
#     description_cat = models.TextField('Описание категории', blank=True)
#
#     def __str__(self):
#         return self.name_cat
#
#     class Meta:
#         verbose_name = 'Категория'
#         verbose_name_plural = 'Категории'
#
#     def get_absolute_url(self):
#         return reverse('article_by_category', args=[self.slug_cat])


class Article(models.Model):
    title = models.CharField('Название статьи', max_length=200)
    slug_article = models.SlugField(max_length=100, unique=True, null=True)
    number_post = models.PositiveIntegerField(verbose_name='Нумерация', null=True, blank=True)
    anons = models.TextField('Анонс', blank=True)
    full_text = models.TextField('Статья', blank=True)
    category_article = models.ForeignKey(CategoryArticle, verbose_name='Категория статьи', on_delete=models.SET_NULL, null=True)
    image_article = models.ImageField('Изображение', upload_to='article_images/', null=True, blank=True)
    draft = models.BooleanField('Черновик', default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ('category_article', 'number_post',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[self.slug_article])


class ArticleTree(models.Model):
    title = models.CharField('Название статьи', max_length=200)
    slug_article = models.SlugField(max_length=100, unique=True, null=True)
    number_post = models.PositiveIntegerField(verbose_name='Нумерация', null=True, blank=True)
    anons = models.TextField('Анонс', blank=True)
    full_text = models.TextField('Статья', blank=True)
    category_article = TreeForeignKey(CategoryTreeArticle, verbose_name='Категория статьи tree',
                                      related_name='cat_tree', null=True, on_delete=models.CASCADE)
    image_article = models.ImageField('Изображение', upload_to='article_images/', null=True, blank=True)
    draft = models.BooleanField('Черновик', default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = '-Статья (Tree)'
        verbose_name_plural = '-- Статьи (Tree)'
        ordering = ('category_article', 'number_post',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[self.slug_article])


class ArticlesTreeStatistic(models.Model):
    class Meta:
        verbose_name = '-- Статистика (Tree)'
        verbose_name_plural = '-- Статистика (Tree)'
        db_table = 'ArticleTreeStatictic'

    article = models.ForeignKey(ArticleTree, on_delete=models.CASCADE)
    date = models.DateField('Дата', default=timezone.now)
    views = models.IntegerField('Просмотры', default=0)

    def __str__(self):
        return self.article.title

