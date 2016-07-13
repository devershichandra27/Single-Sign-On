from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.


class Message(models.Model):
    Sender = models.CharField(max_length=20)
    Recipient = models.CharField(max_length=20)
    Mails = models.CharField(max_length=20)

    def __str__(self):
        return self.Sender + '-' + self.Recipient + '-' + self.Mails

    def get_absolute_url(self):
            return reverse('chat:inbox')
