from django.urls import path
from equation.api import views as api_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [
 
    path("token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('equation/',api_views.EquationListAPIView.as_view(), name='equation'),

]


