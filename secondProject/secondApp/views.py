from django.shortcuts import render
import json
# Create your views here.
from shareApp.model_files.first_models import AdminRoles
from rest_framework.views import APIView
from django.http import JsonResponse
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from .serializers import (
    Adminaa
)

def get_admin():
    doctor = AdminRoles.objects.filter()
    doctor = Adminaa(doctor, many=True)
    print(doctor,"doct")
    doctor_data = orderedDict_to_dict_convertor(doctor.data)
    return doctor_data

def orderedDict_to_dict_convertor(data):
    temp_data = json.dumps(data)
    temp_data = json.loads(temp_data)
    return temp_data 
    
class SecondAPI(APIView):
    def get(self,save_quick):
        ad=get_admin()
        print(ad,"ad")
        channel_layer=get_channel_layer()
        group_name="doctor_group"
        async_to_sync(channel_layer.group_send)(
        group_name,{
            "type":"send.user",
            "data":ad
        }
        )  
        return JsonResponse(
            {
                "message":"Doctor Quickaction Diagnosis Updated",
                "status":True,
                "data":ad
            }
        )
