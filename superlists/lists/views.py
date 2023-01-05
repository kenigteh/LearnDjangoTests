from django.http import HttpResponse
from django.shortcuts import render


# Создайте здесь представления свои.
def home_page(request):
    """Домашняя страница"""
    return render(request, "home.html")
