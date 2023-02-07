from itertools import chain

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import DetailView, ListView
from .models import Article, CategoryArticle, CategoryTreeArticle, ArticleTree

from .forms import SearchForm

from django.db import models
from django.db.models import Q


def search(request):
    search_query = request.GET.get('q', '')
    categories_tree = CategoryTreeArticle.objects.all()

    if search_query:
        articles = ArticleTree.objects.filter(Q(title__iregex=search_query) | Q(full_text__iregex=search_query))
        categories_tree_search = CategoryTreeArticle.objects.filter(Q(name_cat__iregex=search_query))

    else:
        articles = ArticleTree.objects.all()
        categories_tree_search = CategoryTreeArticle.objects.all()

    context = {
        'articles': articles,
        'categories_tree': categories_tree,
        'categories_tree_search': categories_tree_search,
    }
    return render(request, 'shpargalka/search.html', context=context)


def articles_view(request, category_slug=None):
    category = None
    all_articles = Article.objects.all()
    all_articles_tree = ArticleTree.objects.all().order_by('number_post')
    categories = CategoryArticle.objects.all()
    categories_tree = CategoryTreeArticle.objects.all()
    if category_slug:
        category = get_object_or_404(CategoryArticle, slug_cat=category_slug)
        all_articles = all_articles.filter(category_article=category).order_by('-number_post')

    context = {
        'category': category,
        'categories': categories,
        'categories_tree': categories_tree,
        'all_articles': all_articles,
        'all_articles_tree': all_articles_tree,
    }
    return render(request, 'shpargalka/post_list.html', context=context)


# Post detail
def post_detail(request, slug_article):
    post = get_object_or_404(Article, slug_article=slug_article)
    categories = CategoryArticle.objects.all()

    context = {
        'post': post,
        'categories': categories,
    }
    return render(request, 'shpargalka/post_detail.html', context=context)


def category_list(request):
    categories = CategoryArticle.objects.all()
    return render(request, 'shop/shop_category.html', {'categories': categories})

# Block Tree View Start -------------------------------------------------------------


# Post category tree
def category_product_tree(request, id, slug_cat=None):
    category = None
    # categories = CategoryArticle.objects.all()
    categories_tree = CategoryTreeArticle.objects.all()
    all_articles_tree = ArticleTree.objects.all()

    if slug_cat:
        category = get_object_or_404(CategoryTreeArticle, slug_cat=slug_cat)
        all_articles_tree = all_articles_tree.filter(category_article=category)

    context = {
        'category': category,
        # 'categories': categories,
        'categories_tree': categories_tree,
        'all_articles_tree': all_articles_tree,
    }
    return render(request, 'shpargalka/category-tree.html', context=context)


# Post detail tree
def post_detail_tree(request, slug_article):
    post = get_object_or_404(ArticleTree, slug_article=slug_article)
    categories = CategoryTreeArticle.objects.all()
    categories_tree = CategoryTreeArticle.objects.all()

    context = {
        'post': post,
        'categories': categories,
        'categories_tree': categories_tree,
    }
    return render(request, 'shpargalka/post_detail_tree.html', context=context)

# Block Tree View end -------------------------------------------------------------
