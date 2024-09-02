# detection/urls.py
from django.urls import path
from .views import ClothDetectionView

urlpatterns = [
    path('detect/', ClothDetectionView.as_view(), name='detect_clothes'),
]
