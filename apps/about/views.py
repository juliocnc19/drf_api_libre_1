from rest_framework import viewsets
from .models import About
from .serializers import AboutSerializer

class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {"data": response.data}
        return response