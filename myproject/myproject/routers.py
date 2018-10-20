from rest_framework import routers
from movies.viewsets import MovieViewSet


router = routers.DefaultRouter()

router.register('movies', MovieViewSet)