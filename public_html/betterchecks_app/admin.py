from django.contrib import admin
from betterchecks_app.models import Enquiry,CourseEnquiry,Contacts




class EnquiryAdmin(admin.ModelAdmin):
    fields = ['name', 'email', 'phone', 'subject','file', 'message']
    
    search_fields = ['name','email','phone','subject']
    
    list_filter = ['phone', 'email', 'subject']
    
    list_display = ['name','phone', 'email', 'subject','file', 'message']
    
    

class CourseEnquiryAdmin(admin.ModelAdmin):
    fields = ['name', 'email', 'phone', 'country','organization', 'interest']
    
    search_fields = ['name','email','phone','country','organization']
    
    list_filter = ['phone', 'email', 'country']
    
    list_display = list_filter = ['name','phone', 'email', 'country','organization', 'interest']
    
    
class ContactsAdmin(admin.ModelAdmin):
    fields = ['name', 'email', 'phone', 'subject']
    
    search_fields = ['name','email','phone','subject']
    
    list_filter = ['phone', 'email', 'subject']
    
    list_display = ['name','phone', 'email', 'subject','message']


# Register your models here.
admin.site.register(Enquiry,EnquiryAdmin)
admin.site.register(CourseEnquiry,CourseEnquiryAdmin)
admin.site.register(Contacts,ContactsAdmin)


