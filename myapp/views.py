
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
from django.contrib.auth import logout, login
from .models import Product, Purchase
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


def product_list(request):
    products = Product.objects.all() 
    return render(request, 'product_list.html', {'products': products})

# Представление для регистрации
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт для {username} успешно создан! Теперь вы можете войти.')

            # После создания аккаунта, логиним пользователя и перенаправляем на главную
            login(request, user)
            return redirect('index')  # Перенаправление на главную страницу
    else:
        form = UserCreationForm()

    return render(request, 'myapp/register.html', {'form': form})

# Главная страница
def index(request):
    return render(request, 'index.html')

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    def get_success_url(self):
        return reverse_lazy('index')

# Представление для выхода
def logout_view(request):
    logout(request)
    return redirect('index')

def index (request):
    products = Product.objects.all()
    return render(request, 'myapp/index.html', {'products':products})

@login_required
def buy_product(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        user = request.user
        quantity = int(request.POST['quantity'])

        if quantity > product.stock:
            messages.error(request, 'Недостаточно товаров на складе.')
        elif user.wallet < product.price * quantity:
            messages.error(request, 'У вас недостаточно средств.')
        else:
            
            product.stock -= quantity
            product.save()
            user.wallet -= product.price * quantity
            user.save()

            Purchase.objects.create(user=user, product=product, quantity=quantity)

            messages.success(request, f'Вы успешно купили {quantity} шт. {product.name}.')
        
        return redirect('index')




