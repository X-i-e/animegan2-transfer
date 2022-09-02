from django.urls import path

from .views import UploadImageViewSet
from django.conf.urls import url

urlpatterns = [
    path('', UploadImageViewSet.as_view()),
]


# urlpatterns = [
#     path('', views.show_upload),
#     path('handle/', views.upload_handle),
#     path('download/', views.download),
#     url(r'^test$', views.test),
# ]
