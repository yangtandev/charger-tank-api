from rest_framework import serializers
from django.utils import timezone
import pytz

from .models import ChargerTankCurrent, ChargerTankHistory, ChargerTankStatus

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


class ChargerTankCurrentSerializer(serializers.ModelSerializer):
    record_datetime = TaipeiDateTimeField(read_only=True)

    class Meta:
        model = ChargerTankCurrent
        fields = '__all__'
        extra_kwargs = {
            f's{str(i).zfill(2)}': {'required': False} for i in list(range(1, 19))
        }

    def create(self, validated_data):
        loc = validated_data.get('location')
        tt  = validated_data.get('temp_type')
        instance = ChargerTankCurrent.objects.filter(location=loc, temp_type=tt).first()
        validated_data['record_datetime'] = timezone.now().astimezone(taipei_tz)
        if instance:
            return self.update(instance, validated_data)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data['record_datetime'] = timezone.now().astimezone(taipei_tz)
        return super().update(instance, validated_data)


class ChargerTankHistorySerializer(serializers.ModelSerializer):
    record_datetime = TaipeiDateTimeField(read_only=True)

    class Meta:
        model = ChargerTankHistory
        fields = '__all__'
        extra_kwargs = {
            f's{str(i).zfill(2)}': {'required': False} for i in list(range(1, 19))
        }

    def create(self, validated_data):
        validated_data['record_datetime'] = timezone.now().astimezone(taipei_tz)
        return super().create(validated_data)


class ChargerTankStatusSerializer(serializers.ModelSerializer):
    record_datetime = TaipeiDateTimeField(read_only=True)

    class Meta:
        model = ChargerTankStatus
        fields = '__all__'
        extra_kwargs = {
            'env_temp': {'required': False},
            **{f'charger_status{str(i).zfill(2)}': {'required': False} for i in range(1, 17)}
        }

    def create(self, validated_data):
        loc = validated_data.get('location')
        instance = ChargerTankStatus.objects.filter(location=loc).first()
        validated_data['record_datetime'] = timezone.now().astimezone(taipei_tz)
        if instance:
            return self.update(instance, validated_data)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data['record_datetime'] = timezone.now().astimezone(taipei_tz)
        return super().update(instance, validated_data)
