from django.shortcuts import render
from betterchecks_app.forms import EnquiryForm,CourseEnquiryForm,ContactForm
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import messages




# Create your views here.

def index(request):
    form = EnquiryForm()
    
    if request.method == 'POST':
        form = EnquiryForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Thanks for getting in touch we will get back to you as soon as posible')
            form = EnquiryForm()
    else:
        print('ERROR INVALID INPUT')
    
    return render(request, 'betterchecks_app/index.html', {'form':form})


class Fakenews(TemplateView):
    template_name = 'betterchecks_app/fakenews.html'
    

class PrivacyPolicy(TemplateView):
    template_name = 'betterchecks_app/privacy.html'
    
    
    
class Factchecking(TemplateView):
    template_name = 'betterchecks_app/factchecking.html'
    

class Coronavirus(TemplateView):
    template_name = 'betterchecks_app/coronavirus.html'


def Training(request):
    form = CourseEnquiryForm()
    
    if request.method == 'POST':
        form = CourseEnquiryForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, 'Thanks for getting in touch we will get back to you as soon as posible')
            form = CourseEnquiryForm()
        else:
            print('ERROR FORM INVALID')
    return render(request, 'betterchecks_app/training.html', {'form':form})
    
    
def InfoResearch(request):
    form = CourseEnquiryForm()
    
    if request.method == 'POST':
        form = CourseEnquiryForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, 'Thanks for getting in touch we will get back to you as soon as posible')
            form = CourseEnquiryForm()
        else:
            print('ERROR FORM INVALID')
    return render(request, 'betterchecks_app/inforesearch360.html', {'form':form})

def Infodemic(request):
    form = CourseEnquiryForm()
    
    if request.method == 'POST':
        form = CourseEnquiryForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, 'Thanks for getting in touch we will get back to you as soon as posible')
            form = CourseEnquiryForm()
        else:
            print('ERROR FORM INVALID')
    return render(request, 'betterchecks_app/infodemic.html',{'form':form})

def Contacts(request):
    form = ContactForm()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, 'Thanks for getting in touch we will get back to you as soon as posible')
            form = ContactForm()
        else:
            print('ERROR FROM INVALID')
    return render(request, 'betterchecks_app/contacts.html',{'form':form})

def FactCheck(request):
    form = ContactForm()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, 'Thanks for getting in touch we will get back to you as soon as posible')
            form = ContactForm()
        else:
            print('ERROR FROM INVALID')
    return render(request, 'betterchecks_app/factcheck.html',{'form':form})


def MoneyTrail(request):
    form = ContactForm()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, 'Thanks for getting in touch we will get back to you as soon as posible')
            form = ContactForm()
        else:
            print('ERROR FROM INVALID')
    return render(request, 'betterchecks_app/moneytrail.html',{'form':form})



def ShadySpotlight(request):
    form = ContactForm()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, 'Thanks for getting in touch we will get back to you as soon as posible')
            form = ContactForm()
        else:
            print('ERROR FROM INVALID')
    return render(request, 'betterchecks_app/shadyspotlight.html',{'form':form})
    
    


    

