from datetime import datetime
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from models import Sighting
from serializers import SightingSerializer
from rest_framework import viewsets


class SightingViewSet(viewsets.ModelViewSet):
    queryset = Sighting.objects.all().order_by('-timestamp')
    serializer_class = SightingSerializer

    def get_paginate_by(self):
        """ 
        User smaller pagination for HTML view
        """
        if self.request.accepted_renderer.format == 'api':
            return 50
    
        return 1000
