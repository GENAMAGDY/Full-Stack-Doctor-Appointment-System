from django.conf.urls import url
from DoctorApp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^Doctor/$',views.DoctorApi),
    url(r'^Doctor/([0-9]+)$',views.DoctorApi),
    url(r'^Patient/$',views.PatientApi),
    url(r'^Patient/([0-9]+)$',views.PatientApi),
    url(r'^SaveFile$', views.SaveFile),
    url(r'^SendEmailPatient$', views.SendEmailPatient),
    url(r'^SendEmailDoctor$', views.SendEmailDoctor),

    ] + static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)