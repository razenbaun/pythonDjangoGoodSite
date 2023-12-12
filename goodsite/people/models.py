from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Portfolio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    creation_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    description = models.TextField(max_length=765)
    skills = models.CharField(max_length=255)
    photo_1 = models.ImageField(upload_to='portfolio/%Y/%m/%d/', blank=True, null=True)
    link_1 = models.URLField(blank=True)
    photo_2 = models.ImageField(upload_to='portfolio/%Y/%m/%d/', blank=True, null=True)
    link_2 = models.URLField(blank=True)
    photo_3 = models.ImageField(upload_to='portfolio/%Y/%m/%d/', blank=True, null=True)
    link_3 = models.URLField(blank=True)
    photo_4 = models.ImageField(upload_to='portfolio/%Y/%m/%d/', blank=True, null=True)
    link_4 = models.URLField(blank=True)
    photo_5 = models.ImageField(upload_to='portfolio/%Y/%m/%d/', blank=True, null=True)
    link_5 = models.URLField(blank=True)
    photo_6 = models.ImageField(upload_to='portfolio/%Y/%m/%d/', blank=True, null=True)
    link_6 = models.URLField(blank=True)
    photo_7 = models.ImageField(upload_to='portfolio/%Y/%m/%d/', blank=True, null=True)
    link_7 = models.URLField(blank=True)
    photo_8 = models.ImageField(upload_to='portfolio/%Y/%m/%d/', blank=True, null=True)
    link_8 = models.URLField(blank=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('portfolio_slug', kwargs={'portfolio_slug': self.pk})

    class Meta:
        verbose_name = 'Портфолио'
        verbose_name_plural = 'Портфолио'
        ordering = ['-creation_date', 'user']
