from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Article, CategoryArticle, CategoryTreeArticle, ArticleTree

from django.db.models import Q


# Search
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
    # global is_paginated, next_url, prev_url, page
    category = None
    # all_articles = Article.objects.all()
    all_articles_tree = ArticleTree.objects.order_by('number_post')
    categories = CategoryArticle.objects.all()
    categories_tree = CategoryTreeArticle.objects.all()
    if category_slug:
        category = get_object_or_404(CategoryArticle, slug_cat=category_slug)
        all_articles_tree = ArticleTree.objects.filter(category_article=category).order_by('-number_post')
        paginator = Paginator(all_articles_tree, 8)
        page_number = request.GET.get('page', 1)
        page_object = paginator.get_page(page_number)

        is_paginated = page_object.has_other_pages()

        if page_object.has_previous():
            prev_url = f'?page={page_object.previous_page_number()}'
        else:
            prev_url = ''

        if page_object.has_next():
            next_url = f'?page={page_object.next_page_number()}'
        else:
            next_url = ''
    else:

        paginator = Paginator(all_articles_tree, 8)
        page_number = request.GET.get('page', 1)
        page_object = paginator.get_page(page_number)

        is_paginated = page_object.has_other_pages()

        if page_object.has_previous():
            prev_url = f'?page={page_object.previous_page_number()}'
        else:
            prev_url = ''

        if page_object.has_next():
            next_url = f'?page={page_object.next_page_number()}'
        else:
            next_url = ''

    context = {
        'category': category,
        'categories': categories,
        'categories_tree': categories_tree,
        # 'all_articles': all_articles,
        'all_articles_tree': all_articles_tree,
        'page_object': page_object,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url,
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


# Category list
def category_list(request):
    categories = CategoryArticle.objects.all()
    return render(request, 'shop/shop_category.html', {'categories': categories})


# Block Tree View Start -------------------------------------------------------------

# Post category list tree
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

