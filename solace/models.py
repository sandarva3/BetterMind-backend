from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    fullname = models.CharField(max_length=45)

    def __str__(self):
        return self.username



class User(CustomUser):
    pass



class Prof(CustomUser):
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username



class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userdata')
    questionNo = models.IntegerField()
    questionText = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return f"Userdata of {self.user.username}"
    


class ProfData(models.Model):
    prof = models.OneToOneField(Prof, on_delete=models.CASCADE, related_name='profdata')
    questionNo = models.IntegerField()
    questionText = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return f"Profdata of {self.prof.username}"