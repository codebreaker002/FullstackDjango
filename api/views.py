from django.shortcuts import render
from rest_framework import viewsets
from api.models import Item
from api.serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = Item.objects.all()
        sku = self.request.query_params.get('sku')
        name = self.request.query_params.get('name')
        category = self.request.query_params.get('category')
        tags = self.request.query_params.getlist('tags')
        stock_status = self.request.query_params.get('stock_status')
        available_stock = self.request.query_params.get('available_stock')

        # Filter based on query parameters
        if sku:
            queryset = queryset.filter(sku=sku)
        if name:
            queryset = queryset.filter(name__icontains=name)
        if category:
            queryset = queryset.filter(category__name=category)
        if tags:
            queryset = queryset.filter(tags__name__in=tags)
        if stock_status:
            queryset = queryset.filter(stock_status=stock_status)
        if available_stock:
            queryset = queryset.filter(available_stock=available_stock)

        return queryset