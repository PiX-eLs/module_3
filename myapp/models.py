from django.db import models
from django.contrib.auth.models import User

# Расширение модели User для добавления поля кошелек
class ExtendedUser(User):
    wallet_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

# Модель товара
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    stock_quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

# Модель покупки
class Purchase(models.Model):
    user = models.ForeignKey(ExtendedUser, on_delete=models.CASCADE)
    product = models.ForeignKey('myapp.Product', on_delete=models.CASCADE)  # Используйте строковое представление
    quantity = models.PositiveIntegerField()
    purchase_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.name} x {self.quantity}"

# Модель возврата
class Return(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    request_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Return Request for {self.purchase}"
