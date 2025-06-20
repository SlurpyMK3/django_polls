
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from polls.views import IndexView, HomeView
from polls.views import contact_view
from polls.views import ResultsAllView
from polls.views import inscription
from polls.views import connexion
from polls.views import create_poll
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("", HomeView.as_view(), name="home"),   

    path("contact/", contact_view, name="contact"),   
    path("inscription/", inscription, name="inscription"),  
    path("connexion/", connexion, name="connexion"),  
    path('create_poll/', create_poll, name='create_polls'),
    path('resultat/', ResultsAllView.as_view(), name='results_all'),
    path("sondage/", include(("polls.urls", "polls"), namespace="polls")),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)