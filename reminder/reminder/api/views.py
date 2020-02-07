from django.shortcuts import render
from rest_framework import viewsets
from .models import Table
from .serializer import TableSerializer
from .cloudwatchevents_accessor import CloudWatchEventsAccessor
from datetime import datetime
from datetime import timedelta

# Create your views here.

class TableViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    queryset = Table.objects.all()
    serializer_class = TableSerializer

    def perform_create(self, serializer):
        serializer.save()
        b = CloudWatchEventsAccessor()
        b.set_event(
                date_=datetime.strptime(serializer.data["date"], "%Y-%m-%dT%H:%M:%S+09:00") - timedelta(hours=9),
                id_=serializer.data["uuid"])
        print("debug: perform_create")
    
#    def perform_update(self, serializer):
#        serializer.save()
#        b = CloudWatchEventsAccessor()
#        try:
#            b.delete_event("fy19pu-reminder-" + (datetime.strptime(serializer.data["date"], "%Y-%m-%dT%H:%M:%S+09:00") - timedelta(hours=9)).strftime("%Y%m%d%H%M"))
#        except:
#            print("debug: delete events is noting.")
#        
#        b.set_event(
#                date_=datetime.strptime(serializer.data["date"], "%Y-%m-%dT%H:%M:%S+09:00") - timedelta(hours=9),
#                id_=serializer.data["uuid"])
#        print("debug: perform_update")
    
    def perform_destroy(self, instance):
        b = CloudWatchEventsAccessor()
        try:
            delete_event_name = "fy19pu-reminder-" + (datetime.strptime(instance.data["date"], "%Y-%m-%dT%H:%M:%S+09:00") - timedelta(hours=9)).strftime("%Y%m%d%H%M")
            print("debug: delete event name:", delete_event_name)
            b.delete_event(delete_event_name)
        except:
            print("debug: delete events is noting.")
        print("debug: perform_destroy")

    class META:
        lookup_field = 'uuid'


