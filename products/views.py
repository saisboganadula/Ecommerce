from django.shortcuts import render

# Create your views here.


from django.http import JsonResponse

def HelloView(request):
    return JsonResponse({'hello': 'world'})

def HelloName(request, username):
    print(request.headers)
    return JsonResponse({'hello': username})