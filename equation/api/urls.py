from django.urls import path
from equation.api import views as api_views

urlpatterns = [
    path('equation/',api_views.EquationListAPIView.as_view(), name='equation'),
]


