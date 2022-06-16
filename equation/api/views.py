# from django_filters import rest_framework as filters
from rest_framework import filters
from equation.api.serializers import EquationSerializer
from equation.models import Equation
from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination



class EquationListAPIView(ListAPIView):
  queryset = Equation.objects.all().order_by('title')
  filter_backends = [filters.SearchFilter]
  search_fields = ['title']
  serializer_class = EquationSerializer
  pagination_class = LimitOffsetPagination