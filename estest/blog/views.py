from __future__ import (absolute_import, division, print_function, unicode_literals)
from rest_framework_elasticsearch import es_views, es_pagination, es_filters
from .search_indexes import *
from elasticsearch import Elasticsearch


class BlogView(es_views.ListElasticAPIView):
    es_client = Elasticsearch('192.168.20.69:9200')
    es_model = BlogIndex
    es_filter_backends = (
        es_filters.ElasticFieldsFilter,
        es_filters.ElasticSearchFilter
    )
    es_filter_fields = (
        es_filters.ESFieldFilter('tag', 'tags'),
    )
    es_search_fields = (
        'tags',
        'title',
    )