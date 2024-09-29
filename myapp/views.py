from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
from django.contrib.auth import logout 
from .models import Product, Purchase
from django.contrib.auth.decorators import login_required

def product_list(request):
    products = Product.objects.all() 
    return render(request, 'product_list.html', {'products': products})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт {username} был успешно создан!')
            messages.success(request, f'Аккаунт для {username} успешно создан! Теперь вы можете войти.')
            return redirect('login')
        else:
            form = UserCreationForm()
            return render(request, 'myapp/articles/register.html',{'form':form})
    else:
        form = UserCreationForm()

    return render(request, 'myapp/register.html', {'form': form})

def index(request):
    return render(request, 'index.html')

# Представление для выхода
def logout_view(request):
    logout(request)
    return redirect('index')

def index (request):
    products = Product.objects.all()
    return render(request, 'myapp/index.html', {'products':products})
@login_required
def buy_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        quantity = int(request.POST['quantity'])
        if quantity > product.stock:
            messages.error(request, 'Недостаточно товаров на складе')
        elif request.user.wallet < product.price * quantity:
            messages.error(request, 'Недостаточно средств на счёте')
        else:
            
            Purchase.objects.create(user=request.user, product=product, quantity=quantity)
            product.stock -= quantity
            product.save()
            request.user.wallet -= product.price * quantity
            request.user.save()
            messages.success(request, 'Покупка успешно совершена')
            return redirect('product_list')
    return render(request, 'buy_product.html', {'product': product})




