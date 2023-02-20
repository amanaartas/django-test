from shareApp.model_files.first_models import AdminRoles
from rest_framework import serializers

class Adminaa(serializers.ModelSerializer):
    class Meta:
        model=AdminRoles
        fields="__all__"