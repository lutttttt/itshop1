from django.contrib.auth.views import LoginView
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from time import sleep


from .forms import *
from django.views.generic import CreateView , ListView,DetailView
from django.contrib.auth import logout


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
    template_name = 'shop/add_product.html'
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        form.instance.user=self.request.user.id
        print(self.request.user.id)
        form.save()
        return super().form_valid(form)

class Products(ListView):
    model = Product
    template_name = 'shop/products.html'
    context_object_name = 'products'
class Sellers(ListView):
    model=Seller
    template_name = 'shop/seller.html'
    context_object_name = 'sellers'
class DProducts(DetailView):
    model=Product
    template_name= 'shop/product.html'
    context_object_name='product'
    slug_url_kwarg='product_slug'
class Seller(DetailView):
    model = Seller
    template_name = 'shop/dseller.html'
    context_object_name = 'seller'
    slug_url_kwarg = 'seller_slug'
class Login(LoginView):
    template_name = 'shop/login.html'
    context_object_name='login'
    success_url = reverse_lazy('home')
class Home(ListView):
    model=Product
    template_name='shop/home.html'
    context_object_name='products'
def register(request):
    if request.method=="POST":
        form=UserRegisterForm(request.POST)

        form.save()
        username=form.cleaned_data.get('username')
        print(username)
        return redirect('home')
        # else:
        #    print(form.cleaned_data)
        #    print('eror in validation form')
        #    return redirect("register")
    else:
        form=UserRegisterForm()
        return render(request,'shop/register.html',{'form':form})
def logoutv(request):
    logout(request)
    print('h')
    return redirect('home')

        

# Create your views here.
