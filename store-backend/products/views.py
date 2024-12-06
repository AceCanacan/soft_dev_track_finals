from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, ProductImage
from .forms import ProductForm  # moved form to a separate forms.py
from django.http import HttpResponse

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'admin' and password == 'admin':
            request.session['user_type'] = 'admin'
            return redirect('product_list_admin')
        else:
            # any other username/password = 'user'
            request.session['user_type'] = 'user'
            return redirect('product_list')
    return render(request, 'products/login.html')

def logout_view(request):
    request.session.flush()
    return redirect('login')

def require_login(func):
    """Decorator to ensure the user is logged in at all."""
    def wrapper(request, *args, **kwargs):
        if 'user_type' not in request.session:
            return redirect('login')
        return func(request, *args, **kwargs)
    return wrapper

def require_admin(func):
    """Decorator to ensure the user is an admin."""
    def wrapper(request, *args, **kwargs):
        if request.session.get('user_type') != 'admin':
            return redirect('login')
        return func(request, *args, **kwargs)
    return wrapper

@require_login
def product_list(request):
    # For end-user
    # Only accessible if logged in (user or admin)
    products = Product.objects.filter(available=True)
    return render(request, 'products/product_list.html', {'products': products})

@require_login
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk, available=True)
    return render(request, 'products/product_detail.html', {'product': product})

@require_login
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk, available=True)
    cart = request.session.get('cart', [])
    if product.id not in cart:
        cart.append(product.id)
        request.session['cart'] = cart
    return redirect('product_list')

@require_login
def checkout(request):
    cart = request.session.get('cart', [])
    if request.method == 'POST':
        if not cart:
            return render(request, 'products/checkout.html', {'message': 'Cart is empty'})
        Product.objects.filter(id__in=cart, available=True).update(available=False)
        request.session['cart'] = []
        return render(request, 'products/checkout.html', {'message': 'Checkout successful', 'cart': []})
    products = Product.objects.filter(id__in=cart, available=True)
    return render(request, 'products/checkout.html', {'cart': products})

@require_admin
def product_list_admin(request):
    # Display all products, allow add, edit, delete
    products = Product.objects.all()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list_admin')
    else:
        form = ProductForm()
    return render(request, 'products/product_list_admin.html', {'products': products, 'form': form})

@require_admin
def product_edit(request, pk):
    # Edit a product
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list_admin')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/product_edit.html', {'form': form, 'product': product})

@require_admin
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('product_list_admin')