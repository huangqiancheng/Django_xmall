from django.core import serializers
from django.shortcuts import render

# Create your views here.
from django.views import View
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics, filters, request
from rest_framework.pagination import PageNumberPagination
from django_filters import rest_framework, OrderingFilter
from rest_framework.request import Request

from goods.filters import GoodsFilter
from goods.models import Good
from django.http import HttpResponse

# class GoodsView(View):
# #     def get(self,requst):
# #         goods = Good.objects.all()
# #         json_data =  serializers.serialize('json', goods)
# #         print(json_data)
# #         return HttpResponse(json_data,content_type ='application/json')
from goods.serializers import GoodsListSerializers


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'size'


class GoodsListView(generics.ListAPIView):
    serializer_class = GoodsListSerializers
    pagination_class = LargeResultsSetPagination
    filter_backends = (DjangoFilterBackend,filters.OrderingFilter,)
    filter_class = GoodsFilter

    def get_queryset(self):
        queryset = Good.objects.all()
        sort = self.request.query_params.get('sort', None)
        if sort == "1":
            queryset = queryset.order_by('salePrice')
        elif sort == "-1":
            queryset = queryset.order_by('-salePrice')
        return queryset


class GoodListDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Good.objects.all()
    serializer_class = GoodsListSerializers
