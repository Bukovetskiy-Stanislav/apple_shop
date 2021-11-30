from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView
from .models import Category, Product, MacBook, Iphone,Ipad
# Create your views here.
def home(request,):
    return render(request,'home.html')



class CategoryDetailView( DetailView):

    model = Category
    queryset = Category.objects.all()
    context_object_name = 'category'
    template_name = 'category_detail.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProductDetailView( DetailView):

    CT_MODEL_MODEL_CLASS = {
        'macbook': MacBook,
        'iphone': Iphone,
        'ipad': Ipad
    }

    def dispatch(self, request, *args, **kwargs):
        self.model = self.CT_MODEL_MODEL_CLASS[kwargs['ct_model']]
        self.queryset = self.model._base_manager.all()
        return super().dispatch(request, *args, **kwargs)

    context_object_name = 'product'
    template_name = 'product_detail.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ct_model'] = self.model._meta.model_name
        return context

   
def product(request, category_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e
    return render(request, 'product_detail.html', {'product': product})

def iphone(request, category_slug=None):
    category_page= None
    products = None
    if category_slug != None:
        category_page = get_object_or_404(Category, slug = category_slug)
        products = Product.objects.filter(category = category_page, available = True)
    else:
        products = Product.objects.all().filter(category_id = '1')
    return render(request,'iphone.html', {'category':category_page, 'products':products})


def ipad(request, category_slug=None):
    category_page= None
    products = None
    if category_slug != None:
        category_page = get_object_or_404(Category, slug = category_slug)
        products = Product.objects.filter(category = category_page, available = True)
    else:
        products = Product.objects.all().filter(category_id = '2')
    return render(request,'ipads.html', {'category':category_page, 'products':products})


def macbook(request, category_slug=None):
    category_page= None
    products = None
    if category_slug != None:
        category_page = get_object_or_404(Category, slug = category_slug)
        products = Product.objects.filter(category = category_page, available = True)
    else:
        products = Product.objects.all().filter(category_id = '3')
    return render(request,'macbook.html', {'category':category_page, 'products':products})


