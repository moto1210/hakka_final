from django.contrib import admin
from django.urls import path,include
from django.conf.urls import include
from method2.views import  post_detail

urlpatterns = [
    path("admin/", admin.site.urls),
    path("method2/",include("method2.urls")),
    path("<slug:slug>/", post_detail, name="post_detail")
]
