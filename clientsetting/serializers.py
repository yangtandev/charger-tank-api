from rest_framework import serializers
from . import models
from django.utils import timezone
import pytz

# 台北時區
taipei_tz = pytz.timezone('Asia/Taipei')


class TaipeiDateTimeField(serializers.DateTimeField):
    """
    自訂 DateTimeField，讓它在輸出時自動轉成台北時區並格式化。
    """
    def to_representation(self, value):
        if not value:
            return None
        if timezone.is_naive(value):
            value = timezone.make_aware(value, timezone.utc)
        value = value.astimezone(taipei_tz)
        return value.isoformat()

class ClientSettingSerializer(serializers.ModelSerializer):
    last_modified = TaipeiDateTimeField(read_only=True)

    class Meta:
        model = models.ClientSetting
        fields = '__all__'

    def create(self, validated_data):
        validated_data['last_modified'] = timezone.now().astimezone(taipei_tz)
        if instance:
            return self.update(instance, validated_data)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data['last_modified'] = timezone.now().astimezone(taipei_tz)
        return super().update(instance, validated_data)
