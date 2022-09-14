from django.urls import path
from users.views import *

urlpatterns = [
    path("google", GoogleView.as_view(), name='google'),

]