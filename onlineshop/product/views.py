import math
from functools import reduce
from django.db.models import Q, Count
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Product, Category, Filters
from .serializer import ProductSerializer, CategoryListSerializer, FilterListSerializer


class LatestProductsList(APIView):
    def get(self, request, per_page, page, format=None):
        limit = int(per_page) if int(per_page) < 100 else 20
        start_offset = int(page)*limit
        end_offset = start_offset + limit

        products = Product.objects.all()[start_offset:end_offset]
        serializer = ProductSerializer(products, many=True)
        total = Product.objects.count()
        return Response({"total": math.ceil(total/limit), "products": serializer.data})

class CategoryLits(APIView):
    def get(self, request, format=None):
        category = Category.objects.all()
        serializer = CategoryListSerializer(category, many=True)
        return Response(serializer.data)


class ProductDetail(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class CategoryDetail(APIView):
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, per_page, page, format=None):
        limit = int(per_page) if int(per_page) < 100 else 9
        start_offset = int(page) * limit
        end_offset = start_offset + limit
        category = self.get_object(category_slug)
        products = Product.objects.filter(category_id=category.id).all()[start_offset:end_offset]
        serializer = ProductSerializer(products, many=True)
        total = Product.objects.filter(category_id=category.id).count()
        return Response({
            "id": category.id,
            "name": category.name,
            "total": math.ceil(total/limit),
            "get_absolute_url": category.get_absolute_url(),
            "products": serializer.data
        })

    def post(self, request, category_slug, per_page, page, format=None):
        limit = int(per_page) if int(per_page) < 100 else 9
        start_offset = int(page) * limit
        end_offset = start_offset + limit
        category = self.get_object(category_slug)

        products_filtered = Product.objects.filter(category_id=category.id)
        filters_list = request.data.get('filters', [])
        for filter_obj in filters_list:
            if filter_obj.get('price'):
                max_price = float(filter_obj['price']['max_price'])
                min_price = float(filter_obj['price']['min_price'])
                products_filtered = products_filtered.filter(price__range=(min_price, max_price))
            elif filter_obj.get('brands'):
                print(filter_obj.get('brands'))
                products_filtered = products_filtered.filter(reduce(lambda x, y: x | y, [Q(brand=item) for item in filter_obj['brands']]))

        products = products_filtered.all()[start_offset:end_offset]
        total = products_filtered.count()
        serializer = ProductSerializer(products, many=True)
        print(total)
        return Response({
            "id": category.id,
            "name": category.name,
            "total": math.ceil(total / limit),
            "get_absolute_url": category.get_absolute_url(),
            "products": serializer.data
        })

@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response({"products": []})


class FiltersList(APIView):
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        filters = Filters.objects.filter(category_id=category.id).all()
        serializer = FilterListSerializer(filters, many=True)
        return Response(serializer.data)


class getBrandList(APIView):
    def get(self, request, format=None):
        brand = Product.objects.values('brand').annotate(total=Count('id')).values('brand', 'total')
        return Response(brand)