from rest_framework import serializers
from .models import Testimonial

class TestimonialSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    class Meta:
        model = Testimonial
        fields = ['author','content','created_at','is_approved']
        
    def get_author(self,obj):
        return{
            "id":obj.author.id,
            "username":obj.author.username,
            "first_name":obj.author.first_name,
            "last_name":obj.author.last_name
        }