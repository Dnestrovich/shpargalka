from django.urls import path
from shpargalka.views import articles_view, post_detail_tree, category_product_tree, search

urlpatterns = [
    path('', articles_view, name='home'),
    path('search/', search, name='search'),
    path('<slug:category_slug>', articles_view, name='article_by_category'),
    path('<slug:slug_article>/', post_detail_tree, name='article_detail'),
    path('category/<int:id>/<slug:slug_cat>', category_product_tree, name='category_product'),
]