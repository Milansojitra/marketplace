from django.urls import path
from .views import internal_recommand, external_recommand


urlpatterns = [
    path('internal-recommand/', internal_recommand.as_view(),
         name='internal-recommand'),
    path('external-recommand/', external_recommand.as_view(),
         name='external-recommand'),
]
