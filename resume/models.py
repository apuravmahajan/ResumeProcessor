from django.db import models

# Candidate model
class Candidate(models.Model):
    first_name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name