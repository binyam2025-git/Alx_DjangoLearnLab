# notifications/serializers.py

from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.ReadOnlyField(source='actor.username')
    target_type = serializers.CharField(source='content_type.model', read_only=True)

    class Meta:
        model = Notification
        fields = ['id', 'actor', 'verb', 'target_type', 'created_at', 'read']