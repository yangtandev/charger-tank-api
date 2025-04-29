from rest_framework import generics, views, response, status
from . import models
from . import serializers

class ClientSettingListView(generics.ListCreateAPIView):
    serializer_class = serializers.ClientSettingSerializer
    queryset = models.ClientSetting.objects.all()

    def create(self, request, *args, **kwargs):
        name = request.data.get('name')
        group = request.data.get('group', '')
        value = request.data.get('value', '')

        # Try to get existing instance by name
        instance, created = models.ClientSetting.objects.get_or_create(
            name=name,
            defaults={'group': group, 'value': value}
        )

        if not created:
            # Update the existing instance
            instance.group = group
            instance.value = value
            instance.save()

        serializer = self.get_serializer(instance)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

class ClientSettingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ClientSetting.objects.all()
    serializer_class = serializers.ClientSettingSerializer
