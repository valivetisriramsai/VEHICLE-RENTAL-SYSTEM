from typing import OrderedDict
import django_filters 
from.models import *

class filter(django_filters.filterSet):
      class meta:
            model= Car #class name in models.py
            fields='__all__'