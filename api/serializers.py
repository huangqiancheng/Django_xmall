from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.relations import HyperlinkedIdentityField

User = get_user_model()



class UserSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.ReadOnlyField()
    # url = HyperlinkedIdentityField(many=True,view_name="user-detail",lookup_field ="pk")
    class Meta:
        model = User
        fields = ('id','username','mobile','image')


class UserSerializerPassWdPost(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)