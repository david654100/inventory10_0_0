from django.db import models

# Create your models here.
class user (models.Model):
    user_id = models.AutoField(primary_key=true)
    first_name = models.CharField(max_length=30)
    last_name  = models.CharField(max_lenght=30)
    email = models.CharField(max_length = 254)
    

class account_activity (models.Model):
    activity_id = models.AutoField(primary_key=true)
    user_id= models.ForeignKey(user.user_id,on_delete=models.CASCADE)
    activity_type = models.TextField
    action_timestamp = models.DateTimeField

class user_login_information (models.Model):
    login_id = models.AutoField(primary_key=true)
    login_timestamp = models.DateTimeField
    log_out_timestamp = models.DateTimeField
    ser_id= models.ForeignKey(user.user_id,on_delete=models.CASCADE)