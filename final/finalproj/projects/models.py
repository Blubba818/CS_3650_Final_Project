from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Project(models.Model):

    def __str__(self):
        return self.name

    PriorityOptions = (
        ('LL', 'Lowest'),
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High'),
        ('HH', 'Highest')
    )

    StatusOptions = (
        ('X', 'Incomplete'),
        ('I', 'In-Progress'),
        ('C', 'Complete')
    )

    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', default='images/project.jpg')
    description = models.CharField(max_length=1000)
    priority = models.CharField(max_length=200, choices=PriorityOptions)
    status = models.CharField(max_length=200, choices=StatusOptions)
    date_added = models.DateField
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("projects:detail", kwargs={"pk": self.pk})
