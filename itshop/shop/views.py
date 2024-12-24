from django.shortcuts import render
from django.urls import reverse_lazy
from time import sleep

from .forms import *
from django.views.generic import CreateView , ListView

def home(request):
    print(request)
    return render(request,'shop/home.html')
def contact(request):
    return render(request,'shop/contact.html')
def mode(request):
    return render(request,'shop/mode.html')
def add_category(request):
    if request.method == 'POST':
        form= CategoryForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            slug=form.cleaned_data['slug']
            print(name)
            Category.objects.create(name=name,slug=slug)
    else:
        form=CategoryForm()
    return render(request,'shop/add_category.html',{'form':form})
'''def add_product(request):
    if request.method == 'POST':
        form= ProductForm(request.POST)
        if form.is_valid():
            product=form.cleaned_data
            Product.objects.create(name=product['name'],
                                   description=product['description'],
                                   price=product['price'],
                                   category=product['category'],
                                   seller=product['seller'])
    else:
        form=ProductForm()
    return render(request, 'shop/add_category.html', {'form': form})'''


class AddProduct(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'shop/add_category.html'
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        form.instance.user=self.request.user.id
        print(self.request.user.id)
        sleep(10)
        form.save()
        return super().form_valid(form)

class Products(ListView):
    model = Product
    template_name = 'shop/products.html'
    context_object_name = 'products'

# Create your views here.
