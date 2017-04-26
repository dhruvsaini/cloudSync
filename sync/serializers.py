from rest_framework import serializers
from .models import Files

class FileSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(
        read_only=True,
        slug_field='id',
        default = serializers.CurrentUserDefault(),
    )

    hash = serializers.ReadOnlyField(default = "")
    filename = serializers.ReadOnlyField(default = "")
    
    class Meta:
        model = Files
        fields = '__all__'
