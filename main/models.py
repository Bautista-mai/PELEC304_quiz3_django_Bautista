from django.db import models

class Student(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    date_enrolled = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.full_name