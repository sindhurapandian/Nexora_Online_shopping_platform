from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . models import Account

# Register your models here.
#to make password readonly
class AccountAdmin(UserAdmin):
     list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')

     list_display_links = ('email', 'first_name', 'last_name')
     readonly_fields = ('last_login', 'date_joined')
   # shows descending order
     ordering = ('date_joined',)

    #rules to display the password readonly
     filter_horizontal = ()
     list_filter = ()
     fieldsets = ()

admin.site.register(Account,AccountAdmin)