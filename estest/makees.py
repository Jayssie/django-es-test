from elasticsearch import Elasticsearch, RequestsHttpConnection
from blog.search_indexes import BlogIndex

es_client = Elasticsearch('192.168.20.69:9200')
BlogIndex.init(using=es_client) 
# BlogIndex.init() 