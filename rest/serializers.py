from rest_framework import serializers
from .models import Property,Profile



class PropertySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=120)
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    location=serializers.CharField(max_length=20)
    image = serializers.ImageField()

class PropertyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property

        fields=['name','description','price','location','image'] 
      

class PropertyUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property

        fields=['name','image','description','price','location'] 

class PropertyDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property

        fields=['name','description','price','location','image'] 

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile

        fields=['user','image','property','bio','contacts'] 

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.property = validated_data.get('property', instance.property)
        instance.save()
        return instance