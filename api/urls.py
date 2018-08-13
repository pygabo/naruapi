from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from .views import NijaViewSet

API_TITLE = ' API'
API_DESCRIPTION = 'NaruApi'
schema_view = get_schema_view(title=API_TITLE)

router = DefaultRouter()
router.register('nijas', NijaViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('docs/',
    include_docs_urls(title=API_TITLE, description=API_DESCRIPTION))
]
