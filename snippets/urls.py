from django.urls import path
from django.conf.urls import url
import snippets.views as views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    #url(r'^snippets/$', views.snippet_list),
    #url(r'^snippets/(?P<pk>[0-9]+)$', views.snippet_detail),
    url(r'^snippets/$', views.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)$', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)