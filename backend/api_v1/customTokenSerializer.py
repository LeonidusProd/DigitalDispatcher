from rest_framework import serializers
from djoser.serializers import TokenSerializer
from djoser.conf import settings


class CustomTokenSerializer(TokenSerializer):
    role = serializers.SerializerMethodField(method_name='get_role')

    def get_role(self, obj):
        user = obj.user
        if user.is_superuser:
            return 'admin'
        elif user.is_staff:
            return 'staff'
        else:
            return 'user'

    class Meta:
        model = settings.TOKEN_MODEL
        fields = ('auth_token', 'role')
