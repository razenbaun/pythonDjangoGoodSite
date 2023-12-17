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

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('portfolio_slug', kwargs={'portfolio_slug': self.slug})

    class Meta:
        verbose_name = 'Портфолио'
        verbose_name_plural = 'Портфолио'
        ordering = ['-creation_date', 'user']


class AcademicAchievements(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/')
    creation_date = models.DateField(auto_now_add=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Достижения'
        verbose_name_plural = 'Достижения'
        ordering = ['-creation_date', 'user']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']