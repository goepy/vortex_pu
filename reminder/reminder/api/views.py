from django.shortcuts import render
from rest_framework import viewsets
from .models import Table
from .serializer import TableSerializer

# Create your views here.

class TableViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    queryset = Table.objects.all()
    serializer_class = TableSerializer

    def perform_create(self, serializer):
        print("debug: perform_create")
        serializer.save()


