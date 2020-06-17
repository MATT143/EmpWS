from rest_framework import serializers
from .models import expertTaskDetails

class getTaskDetailsSerializer(serializers.ModelSerializer):
    taskAttachment1=serializers.URLField(required=False,allow_blank=True)
    taskAttachment2=serializers.URLField(required=False,allow_blank=True)
    class Meta:
        model= expertTaskDetails
        exclude=['user','expertTaskId']



