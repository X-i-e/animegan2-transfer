from django.urls import path

from transfer import views

from django.conf.urls import url


urlpatterns = [
    path('', views.show_upload),
    path('handle/', views.upload_handle),
    path('download/', views.download),
    url(r'^test$', views.test),
]
