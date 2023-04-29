from django.shortcuts import render
from django.http import HttpResponse

total_price = 0
tax_rate = 0.15
def home(request):
    return HttpResponse("This is a site to calculate tax")

def tax(request, number):
    total_price = number + (number * tax_rate)
    return HttpResponse("Calculated! Price after the tax is " + str(total_price))

def taxrate(request):
    return render(request, "projectApp/taxrate.html", {"tax_rate": tax_rate*100})