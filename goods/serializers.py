from rest_framework import serializers
from rest_framework.relations import HyperlinkedIdentityField

from goods.models import Good


class GoodsListSerializers(serializers.HyperlinkedModelSerializer):
    # id = serializers.IntegerField()
    # salePrice = serializers.DecimalField(max_digits=10,decimal_places=2)
    # productName = serializers.CharField()
    # subTitle = serializers.CharField()
    # productImageBig = serializers.ImageField()
    # created = serializers.DateTimeField()
    # updated = serializers.DateTimeField()

    class Meta:
        model = Good
        fields = ('id','salePrice', 'productName', 'subTitle', 'productImageBig', 'created', 'updated')

