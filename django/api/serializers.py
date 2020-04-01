from rest_framework import serializers

from .models import Plan, Task

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ['id', 'plan_name', 'create_at', 'update_at']
        read_only_fields = ['id']

        def create(self, validated_data):
            return Plan.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.plan_name = validated_data.get('plan_name', instance.plan_name)
            instance.create_at = validated_data.get('create_at', instance.create_at)
            instance.update_at = validated_data.get('update_at', instance.update_at)
            instance.save()
            return instance

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'task_name', 'start_datetime', 'end_datetime', 'url', 'task_memo', 'plan', 'create_at', 'update_at']
        read_only_fields = ['id']

        def create(self, validate_data):
            return Task.objects.create(**validate_data)

        def update(self, instance, validate_data):
            instance.task_name = validate_data.get('task_name', instance.task_name)
            instance.start_datetime = validate_data.get('start_datetime', instance.start_datetime)
            instance.end_datetime = validate_data.get('end_datetime', instance.end_datetime)
            instance.url = validate_data.get('url', instance.url)
            instance.plan = validate_data.get('plan', instance.plan)
            instance.create_at = validate_data.get('create_at', instance.create_at)
            instance.update_at = validate_data.get('update_at', instance.update_at)
            instance.save()
            return instance