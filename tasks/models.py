
from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):

    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    title = models.CharField(max_length=200)
    description = models.TextField()

    # Task completion status
    completed = models.BooleanField(default=False)

    # Task due date
    due_date = models.DateField(
        null=True,
        blank=True
    )

    # Task priority
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='Medium'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
