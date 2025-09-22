from django.shortcuts import render

# Create your views here.


from django.http import JsonResponse

from products.models import Product


def helloView(request):
    return JsonResponse({'hello': 'world'})

def helloName(request, username):
    print(request.headers)
    p=Product.objects.all()
    print(p[0].name)

    return JsonResponse({'hello': username})