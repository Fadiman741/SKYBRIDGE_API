from rest_framework import serializers 
from api.models import Property

class PropertySerialiazer(serializers.Serializer):
        id=serializers.IntegerField()
        name=serializers.CharField( max_length=100)
        image=serializers.CharField(max_length=100)
        type=serializers.CharField(max_length=20)
        province=serializers.CharField(max_length=20)
        address=serializers.CharField(max_length=100)
        description=serializers.CharField(max_length=300)
        # name=serializers.CharField()
        dateListed =serializers.DateField()
        rooms=serializers.IntegerField()
        bathrooms=serializers.IntegerField()
        garage=serializers.IntegerField()
        size=serializers.IntegerField()
        price=serializers.IntegerField()

        def create(self, data):
                return Property.objects.create(**data)
        
        def update(self,instance , data):
                instance.name = data.get('name',instance.name)
                instance.image = data.get('image',instance.image)
                instance.type = data.get('type',instance.type)
                instance.province = data.get('province',instance.province)
                instance.address = data.get('address',instance.address)
                instance.description = data.get('description',instance.description)
                instance.dateListed = data.get('dateListed',instance.dateListed)
                instance.rooms = data.get('rooms',instance.rooms)
                instance.bathrooms = data.get('bathrooms',instance.bathrooms)
                instance.garage = data.get(' garage',instance. garage)
                instance.name = data.get('size',instance.size)
                instance.price = data.get('price',instance.size)

                instance.save()
                return instance