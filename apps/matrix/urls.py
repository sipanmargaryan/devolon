from django.urls import path

from .views import ProductAPIView

app_name = 'matrix'
urlpatterns = [
    path('product/', ProductAPIView.as_view(), name='product'),
]
