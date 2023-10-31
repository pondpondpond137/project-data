from django.db import models

# Create your models here.
class ListContact(models.Model):
    user = models.CharField(max_length=50, null=True)
    message = models.TextField(null=True)

    def __str__(self):
        return f"ข้อความจาก {self.user}"