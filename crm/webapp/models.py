from django.db import models

class Record(models.Model):

    creation_date = models.DateTimeField(auto_now_add=True)

    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    lga = models.CharField(max_length=50)

    def __str__(self):
        # Fix typo and use full_name instead of separate fields
        return self.full_name
