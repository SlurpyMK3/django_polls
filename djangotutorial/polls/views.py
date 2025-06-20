from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Choice, Question
from django.db.models import F
from django.urls import reverse
from django.views import generic
from django.views.generic import TemplateView

from django.contrib.auth.forms import UserCreationForm 
from .form import CustomUserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Question, Choice
from django.forms import modelform_factory, inlineformset_factory
from django.utils import timezone

class HomeView(TemplateView):
    template_name = "home.html"

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    return context


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsAllView(TemplateView):
    template_name = "polls/results_all.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Récupère toutes les questions avec leurs choix, triées par date décroissante
        context['questions'] = Question.objects.prefetch_related('choice_set').order_by('-pub_date')
        return context


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "Vous n'avez pas sélectionnez de choix.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
    



QuestionForm = modelform_factory(Question, fields=['question_text', 'pub_date'])
ChoiceFormSet = inlineformset_factory(Question, Choice, fields=['choice_text'], extra=3)

def create_poll(request):
    error_message = None

    if request.method == "POST":
        question_text = request.POST.get("question_text")
        choices = request.POST.getlist("choice")  # récupère tous les choix envoyés
        image = request.FILES.get("image")

        # Filtrer les choix vides et garder au moins 2 choix remplis
        choices = [c for c in choices if c.strip()]
        if not question_text or len(choices) < 2:
            error_message = "Remplis la question et au moins 2 réponses."
        else:
            question = Question.objects.create(
                question_text=question_text,
                pub_date=timezone.now(),
                image=image  
            )
            for choice_text in choices:
                Choice.objects.create(question=question, choice_text=choice_text)

            return redirect('polls:index')

    return render(request, "create_poll.html", {"error_message": error_message})




def delete_poll(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    # if request.user != question.author:  # Si tu veux gérer les auteurs
    #     return HttpResponseForbidden("Tu n'as pas le droit de supprimer ce sondage.")

    if request.method == "POST":
        question.delete()
        return redirect('polls:index')

    return render(request, "polls/confirm_delete.html", {"question": question})


def contact_view(request):
    return render(request, 'contact.html')

# Create your views here.
def inscription(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('connexion')
    else:
        form = CustomUserCreationForm()
    return render(request, 'inscription.html', {'form': form})

def connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # <- redirige vers la liste des sondages
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    return render(request, 'connexion.html')


def accueil(request):
    if request.user.is_authenticated:
        # Version pour utilisateur connecté (si tu veux)
        return render(request, 'home.html', {"connected": True})
    else:
        # Version publique, non connectée
        return render(request, 'home.html', {"connected": False})

def deconnexion(request):
    logout(request)
    return redirect('connexion')