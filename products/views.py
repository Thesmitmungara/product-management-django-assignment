from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Product

def is_admin(user):
    return user.profile.role == 'ADMIN'

@login_required
def home(request):
    products = Product.objects.all()
    is_admin_user = is_admin(request.user)
    return render(request, 'home.html', {
        'products': products,
        'is_admin': is_admin_user
    })

@login_required
def add_product(request):
    if not is_admin(request.user):
        return HttpResponseForbidden("You are not allowed to add products")

    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']

        Product.objects.create(
            name=name,
            description=description,
            price=price
        )
        return redirect('home')

    return render(request, 'add_product.html')

@login_required
def edit_product(request, product_id):
    if not is_admin(request.user):
        return HttpResponseForbidden()

    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        product.name = request.POST['name']
        product.description = request.POST['description']
        product.price = request.POST['price']
        product.save()
        return redirect('home')

    return render(request, 'edit_product.html', {'product': product})

@login_required
def delete_product(request, product_id):
    if not is_admin(request.user):
        return HttpResponseForbidden()

    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('home')

@login_required
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})
