import json

from django.db.models.signals import post_delete, post_save
from django.core.signals import request_finished
from django.dispatch import receiver

from diary.models import Diary
from diary.serializers import DiaryModelSerializer

from pilotadmin.models import Pilotadmin
from pilotadmin.serializers import PilotadminModelSerializer

from .models import Log


@receiver(post_save, sender=Diary, dispatch_uid='post_save_diary')
def post_save_diary(sender, instance, created, **kwargs):
    action = 'CREATE' if created else 'UPDATE'
    app_label = sender._meta.app_label
    model_name = sender._meta.model_name
    created_by = instance.created_by if hasattr(instance, 'created_by') else None
    Log.objects.create(
        action=action,
        app_label=app_label,
        model_name=model_name,
        data=json.dumps(DiaryModelSerializer(instance).data, ensure_ascii=False),
        created_by=created_by,
    )


@receiver(post_delete, sender=Diary, dispatch_uid='post_delete_diary')
def post_delete_diary(sender, instance, **kwargs):
    action = 'DELETE'
    app_label = sender._meta.app_label
    model_name = sender._meta.model_name
    created_by = instance.created_by if hasattr(instance, 'created_by') else None
    Log.objects.create(
        action=action,
        app_label=app_label,
        model_name=model_name,
        data=json.dumps(DiaryModelSerializer(instance).data, ensure_ascii=False),
        created_by=created_by,
    )


@receiver(post_save, sender=Pilotadmin, dispatch_uid='post_save_pilotadmin')
def post_save_pilotadmin(sender, instance, created, **kwargs):
    action = 'CREATE' if created else 'UPDATE'
    app_label = sender._meta.app_label
    model_name = sender._meta.model_name
    updated_by = instance.updated_by if hasattr(instance, 'updated_by') else None
    Log.objects.create(
        action=action,
        app_label=app_label,
        model_name=model_name,
        data=json.dumps(PilotadminModelSerializer(instance).data, ensure_ascii=False),
        created_by=updated_by,
    )


@receiver(post_delete, sender=Pilotadmin, dispatch_uid='post_delete_pilotadmin')
def post_delete_pilotadmin(sender, instance, **kwargs):
    action = 'DELETE'
    app_label = sender._meta.app_label
    model_name = sender._meta.model_name
    updated_by = instance.updated_by if hasattr(instance, 'updated_by') else None
    Log.objects.create(
        action=action,
        app_label=app_label,
        model_name=model_name,
        data=json.dumps(PilotadminModelSerializer(instance).data, ensure_ascii=False),
        created_by=updated_by,
    )