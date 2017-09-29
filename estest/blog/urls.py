from django.conf.urls import url
from . import views
app_name = 'blog'
urlpatterns = [
    url(regex=r'^blog/$',view=views.BlogView.as_view(),name='blog-list'),
    # url(regex=r'^test/$',view=views.TestLogView.as_view(),name='testlog'),
]