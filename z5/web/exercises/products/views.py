from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, HttpResponse
from products.models import Product


def hello_world(req):
    return HttpResponse("Hello World")


def hello_world_name(req, name):
    return HttpResponse("Hello " + name)

# def products_list(request):
#     products = Product.objects.all()
#     output = ""
#     for prod in products:
#         output += str(prod) + "<br>"
#
#     return HttpResponse(output)


def products_list(request):
    products = Product.objects.all()
    return render(
        request=request,
        context={'products': products},
        template_name="products_list.html"
    )


