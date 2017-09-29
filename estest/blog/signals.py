# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function, unicode_literals)

from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from elasticsearch import Elasticsearch
from serializers import Blog, ElasticBlogSerializer

es_client = Elasticsearch('192.168.20.69:9200')
@receiver(pre_save, sender=Blog, dispatch_uid="update_record")
def update_es_record(sender, instance, **kwargs):
    obj = ElasticBlogSerializer(instance)
    obj.save(using=es_client)


@receiver(post_delete, sender=Blog, dispatch_uid="delete_record")
def delete_es_record(sender, instance, *args, **kwargs):
    obj = ElasticBlogSerializer(instance)
    obj.delete(using=es_client, ignore=404)
