from django.conf import settings
from django.db import models


class Image(models.Model):
    "Generated Model"
    userimage = models.BinaryField()
