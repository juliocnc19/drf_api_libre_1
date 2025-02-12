from rest_framework import serializers
from .models import Testimonial
from django.contrib.auth.models import User


class TestimonialSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),  # Permite asignar un usuario al crear
        write_only=True  # Solo para escritura, ya que usaremos otro campo para lectura
    )
    author_detail = serializers.SerializerMethodField()
    class Meta:
        model = Testimonial
        fields = ['author','author_detail','content','created_at','is_approved']
        extra_kwargs = {'author': {'write_only': True}}
        
    def get_author_detail(self,obj):
        return{
            "id":obj.author.id,
            "username":obj.author.username,
            "first_name":obj.author.first_name,
            "last_name":obj.author.last_name
        }