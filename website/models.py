from django.db import models

# Create your models here.
class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    address = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=9)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=10)

    def __str__(self) -> str:
        return(f"{self.first_name} {self.last_name}")
    
