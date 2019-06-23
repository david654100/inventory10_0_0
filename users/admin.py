from django.contrib import admin
from users.models import account_activity, user_login_information, Profile

# Register your models here.

admin.site.register(Profile)
admin.site.register(account_activity)
admin.site.register(user_login_information)
