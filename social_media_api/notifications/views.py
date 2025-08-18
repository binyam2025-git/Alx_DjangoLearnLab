#from django.shortcuts import render

# notifications/views.py

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from .models import Notification
from .serializers import NotificationSerializer

class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user).all()

class MarkAsReadView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.recipient != request.user:
            return Response({"detail": "Not authorized."}, status=status.HTTP_403_FORBIDDEN)
        instance.read = True
        instance.save()
        return Response({"detail": "Notification marked as read."}, status=status.HTTP_200_OK)
