from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

class account_activity (models.Model):
    activity_id = models.AutoField(primary_key=True)
    user_id= models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.TextField(null=True, blank=True, default=None)
    action_timestamp = models.DateTimeField(null=True, blank=True, default=None)

class user_login_information (models.Model):
    user_id= models.ForeignKey(User, on_delete=models.CASCADE)
    login_timestamp = models.DateTimeField(null=True, blank=True, default=None)
    log_out_timestamp = models.DateTimeField(null=True, blank=True, default=None)
