from django.shortcuts import render, redirect
from django.utils.translation import ugettext as _, activate
from django.views import View
from django.views.generic import DetailView, View
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from .models import *
from .mixins import CategoryDetailMixin


def store_main_page(request):
    return render(request, 'store_main_page.html', {
                      'title': _('Главная страница'),
                  })


class BaseView(View):

    def get(self, request, *args, **kwargs):
        categories = Category.objects.get_categories_for_left_sidebar()
        products = LatestProducts.objects.get_products_for_main_page(
            'notebooks', 'smartphones', 'videocards', 'processors', 'motherboards', 'ram', 'coolers', 'ssd', 'hdd',
            'cases', 'powersupply', with_respect_to='notebooks'
        )
        context = {
            'title': _('TechStore'),
            'categories': categories,
            'products': products,
            'wide': True
        }
        return render(request, 'main_page.html', context)


class ProductDetailView(CategoryDetailMixin, DetailView):

    CT_MODEL_MODEL_CLASS = {
        'notebooks': Notebook,
        'smartphones': Smartphone,
        'videocards': VideoCards,
        'processors': Processors,
        'motherboards': Motherboard,
        'ram': RAM,
        'coolers': Coolers,
        'ssd': SSD,
        'hdd': HDD,
        'cases': Case,
        'powersupply': PowerSupply
    }

    def dispatch(self, request, *args, **kwargs):
        self.model = self.CT_MODEL_MODEL_CLASS[kwargs['ct_model']]
        self.queryset = self.model._base_manager.all()
        return super().dispatch(request, *args, **kwargs)

    context_object_name = 'product'
    template_name = 'product_detail.html'
    slug_url_kwarg = 'slug'


class CategoryDetailView(CategoryDetailMixin, DetailView):

    model = Category
    queryset = Category.objects.all()
    context_object_name = 'category'
    template_name = 'category_detail.html'
    slug_url_kwarg = 'slug'


def test(request):
    posts = Post.objects.all()[:2]
    return render(request, 'test.html', {'posts': posts})


class DynamicPostLoad(View):

    @staticmethod
    def get(request, *args, **kwargs):
        last_post_id = request.GET.get('lastPostId')
        more_posts = Post.objects.filter(pk__gt=int(last_post_id)).values('id', 'main_title', 'title')[:2]
        if not more_posts:
            return JsonResponse({'data': False})
        data = []
        for post in more_posts:
            obj = {
                'id': id,
                'main_title': post['main_title'],
                'title': ['title']
            }
            data.append(obj)
        data[-1]['last_post'] = True
        return JsonResponse({'data': data})


#def store_main_page(request):
    #category = Category.objects.all()
    #products = []
    #for el_in_cat in category:
        #product = Product.objects.filter(category=el_in_cat)
        #products.append((el_in_cat, product))
    #one_product = Product.objects.get(pk=1)
    #return render(request, 'store_main_page.html',
                  #{
                      #'title': _('@TechStore'),
                      #'products': products,
                      #'one_product': one_product,
                      #'wide': True
                  #})