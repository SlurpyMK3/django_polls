from django.db import models
import datetime
from django.utils import timezone
# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    image = models.ImageField(upload_to='images/', blank=True, null=True)  # si tu avais cette colonne


    
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Utilisateur(models.Model):
    nom = models.CharField(max_length=100)
    #prenom = models.CharField(max_length=100)
    #email = models.EmailField()
    mot_de_passe = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.prenom} {self.nom} ({self.email})"