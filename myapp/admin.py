from django.contrib import admin
from .models import Profile,Contact
admin.site.site_header="Chencho Portfolio & User profile!!"

class AdminProfile(admin.ModelAdmin):
    list_display = ('user','bio','phone_no','dob','profile_img')
    list_filter = ('user','phone_no')
admin.site.register(Profile, AdminProfile)

class AdminContact(admin.ModelAdmin):
    list_display = ('name','email','phone','msg')
    list_filter = ('name','email','phone')
admin.site.register(Contact,AdminContact)
