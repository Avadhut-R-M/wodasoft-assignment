from django.contrib import admin
from .models import AccountOne, AccountThree, AccountTwo
# Register your models here.

admin.site.register(AccountOne)
admin.site.register(AccountTwo)
admin.site.register(AccountThree)
