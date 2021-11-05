from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    auteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titre = models.CharField(max_length=200)
    texte = models.TextField()
    date_de_creation = models.DateTimeField(default=timezone.now)
    date_de_publication = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.date_de_publication = timezone.now()
        self.save()

    def __str__(self):
        return self.titre