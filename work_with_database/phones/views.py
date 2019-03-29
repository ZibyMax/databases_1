from django.shortcuts import render
from .models import Phone

def show_catalog(request):
    sort = request.GET.get('sort')
    if sort == 'name':
        phones = Phone.objects.all().order_by('name')
    elif sort == 'min_price':
        phones = Phone.objects.all().order_by('price')
    elif sort == 'max_price':
        phones = Phone.objects.all().order_by('-price')
    else:
        phones = Phone.objects.all()

    return render(
        request,
        'catalog.html',
        context={'phones': phones}
    )


def show_product(request, slug):
    phone = Phone.objects.filter(slug=slug)
    return render(
        request,
        'product.html',
        context={'phone': phone[0]}
    )
