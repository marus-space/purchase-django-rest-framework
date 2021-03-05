from django.shortcuts import render, redirect
from .models import Product, Category, Categorization, Purchase
from .forms import PurchaseForm


def index(request):
    purchases = Purchase.objects.order_by('-date', 'id')
    return render(request, 'main/index.html', {'title': 'Мои покупки', 'purchases': purchases})


def new_purchase(request):
    error = ''
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'В вводимых данных содержится ошибка'

    form = PurchaseForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/new_purchase.html', context)
