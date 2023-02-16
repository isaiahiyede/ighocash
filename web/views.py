from django.shortcuts import render
from django.views import View
from django.conf import settings
import os


class IndexView(View):
    template_name = "web/index.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
        
class AboutView(View):
    template_name = "web/about.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class ContactView(View):
    template_name = "web/contact.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
        
class CapacityView(View):
    template_name = "web/services/capacity.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)  

class AnalyticsView(View):
    template_name = "web/services/analytics.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)  
        
class SmeLoanView(View):
    template_name = "web/services/sme.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)  

class SilverLoanView(View):
    template_name = "web/services/silver.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name) 
    
class DiamondLoanView(View):
    template_name = "web/services/diamond.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name) 

class GoldLoanView(View):
    template_name = "web/services/gold.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name) 

class IndustriesView(View):
    template_name = "web/services/industries.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)     