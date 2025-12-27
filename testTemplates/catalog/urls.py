from django.urls import path
from .views import *

urlpatterns = [

    path("", catalog_page),
    path("-comment/", comment_page),
    path("-thanks/", thanks_page),

]

