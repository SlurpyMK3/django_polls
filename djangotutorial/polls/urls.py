from django.urls import path

from . import views

from django.conf.urls.static import static

from .views import ResultsAllView
app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),  
    path("contact/", views.contact_view, name="contact"),  
    path("connexion/", views.connexion, name="connexion"),
    path("deconnexion/", views.deconnexion, name="deconnexion"),
    path("inscription/", views.inscription, name="inscription"),
    path("resultat/", ResultsAllView.as_view(), name="results_all"),
    path("create_poll/", views.create_poll, name="create_poll"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/resultat/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path('polls/<int:question_id>/delete/', views.delete_poll, name='delete_poll'),

]
