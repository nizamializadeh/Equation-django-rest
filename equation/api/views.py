from rest_framework import filters
from equation.api.serializers import EquationSerializer
from equation.models import Equation
from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import permissions,status
from rest_framework_simplejwt.authentication import JWTAuthentication



class EquationListAPIView(ListAPIView):

  authentication_classes = (JWTAuthentication,)
  permission_classes = (permissions.IsAuthenticated,)
  queryset = Equation.objects.all().order_by('title')
  filter_backends = [filters.SearchFilter]
  search_fields = ['title']
  serializer_class = EquationSerializer
  pagination_class = LimitOffsetPagination