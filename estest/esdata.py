from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch( "192.168.20.69:9200" ) 
data = {
    "title":"testblog",
    "created_at":datetime.now(),
    "body":"bodybodybodybody",
    "tags":["a","b"]
}

es.index( index="blog", doc_type="error_code", body=data )