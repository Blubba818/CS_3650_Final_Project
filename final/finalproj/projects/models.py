from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Project(models.Model):

    def __str__(self):
        return self.name

    PriorityOptions = (
        (5, 'Lowest'),
        (4, 'Low'),
        (3, 'Medium'),
        (2, 'High'),
        (1, 'Highest')
    )

    StatusOptions = (
        (1, 'Pending'),
        (2, 'In-Progress'),
        (3, 'Complete')
    )

    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', default='images/checklist.png')
    description = models.CharField(max_length=1000)
    priority = models.IntegerField(choices=PriorityOptions, default=3)
    status = models.IntegerField(choices=StatusOptions, default=1)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("projects:detail", kwargs={"pk": self.pk})
