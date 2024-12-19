from django.db import models

class Signature(models.Model):
    original_image = models.ImageField(upload_to='originals/')
    uploaded_image = models.ImageField(upload_to='uploads/')
    result = models.TextField(blank=True, null=True)


