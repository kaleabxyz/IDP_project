from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register('doctor',Backendviewset ,basename= "doctor")
router.register('patient',PatientViewSet, basename= "patient")
router.register('room',RoomViewSet, basename= "room")



urlpatterns = router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
