from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    name = models.CharField(max_length=50, null=False)
    price = models.CharField(max_length=10, null=False)
    image = models.CharField(max_length=100)
    release_date = models.DateField(auto_now=False, auto_now_add=False)
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(max_length=50)

    def save(self, *args, **kwargs):
        if not self.slug:
            print("пусто")
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
