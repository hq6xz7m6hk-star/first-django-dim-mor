from django.shortcuts import render
from .models import Product
MENU = {"главная": "/", "каталог": "/catalog", "о сайте": "/about"}


def catalog_page(request):
    products = Product.objects.all()
    title = "Каталог"
    data = {"title": title, "menu": MENU, "products": products}
    return render(request, "./catalog.html", context=data)





