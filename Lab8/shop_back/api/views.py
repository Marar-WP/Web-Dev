from django.http import JsonResponse
from .models import Product, Category
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from rest_framework.filters import SearchFilter, OrderingFilter



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(detail=True, methods=['get'])
    def products(self, request, pk=None):
        category = self.get_object()
        products = Product.objects.filter(category=category)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name', 'price']
    ordering = ['name']

    def get_queryset(self):
        queryset = Product.objects.all()

        category = self.request.query_params.get('category')
        is_active = self.request.query_params.get('is_active')

        if category:
            queryset = queryset.filter(category_id=category)

        if is_active is not None:
            if is_active.lower() == 'true':
                queryset = queryset.filter(is_active=True)
            elif is_active.lower() == 'false':
                queryset = queryset.filter(is_active=False)

        return queryset

    @action(detail=False, methods=['get'])
    def active(self, request):
        queryset = Product.objects.filter(is_active=True)

        category = request.query_params.get('category')
        search = request.query_params.get('search')
        ordering = request.query_params.get('ordering')

        if category:
            queryset = queryset.filter(category_id=category)

        if search:
            queryset = queryset.filter(name__icontains=search)

        if ordering in ['name', '-name', 'price', '-price']:
            queryset = queryset.order_by(ordering)

        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)
def products_list(request):
    products = Product.objects.all()

    category = request.GET.get("category")
    active = request.GET.get("active")
    search = request.GET.get("search")

    if category:
        products = products.filter(category_id=category)

    if active:
        if active.lower() == "true":
            products = products.filter(is_active=True)
        elif active.lower() == "false":
            products = products.filter(is_active=False)

    if search:
        products = products.filter(name__icontains=search)

    data = []

    for p in products:
        data.append({
            "id": p.id,
            "name": p.name,
            "price": p.price,
            "description": p.description,
            "count": p.count,
            "is_active": p.is_active,
            "category_id": p.category.id
        })

    return JsonResponse(data, safe=False)


def product_detail(request, id):
    p = Product.objects.get(id=id)

    data = {
        "id": p.id,
        "name": p.name,
        "price": p.price,
        "description": p.description,
        "count": p.count,
        "is_active": p.is_active,
        "category_id": p.category.id
    }

    return JsonResponse(data)


def categories_list(request):
    categories = Category.objects.all()
    data = []

    for c in categories:
        data.append({
            "id": c.id,
            "name": c.name
        })

    return JsonResponse(data, safe=False)


def category_detail(request, id):
    c = Category.objects.get(id=id)

    data = {
        "id": c.id,
        "name": c.name
    }

    return JsonResponse(data)


def category_products(request, id):
    products = Product.objects.filter(category_id=id)
    data = []

    for p in products:
        data.append({
            "id": p.id,
            "name": p.name,
            "price": p.price
        })

    return JsonResponse(data, safe=False)