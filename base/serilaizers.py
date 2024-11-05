
from rest_framework.serializers import ModelSerializer
from .models import *


class listSerializers(ModelSerializer):
    class Meta:
        model = Lists
        fields = '__all__'