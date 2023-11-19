
from app.views import *
from django.urls import path
app_name='anyhting'

urlpatterns=[
    path('semi/',semi,name='semi'),
    path('jeevan/',jeevan,name='jeevan'),
]
