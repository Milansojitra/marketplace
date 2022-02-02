from django.urls import path
from .views import internal_recommand

urlpatterns = [
    path('internal-recommand/', internal_recommand.as_view(),
         name='internal-recommand'),
]
