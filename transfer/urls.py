from transfer import views

from django.conf.urls import url


urlpatterns = [
    url(r'^upload$', views.show_upload),
    url(r'^handle$', views.upload_handle),
    url(r'^download/$', views.download),
    url(r'^test$', views.test)
]
