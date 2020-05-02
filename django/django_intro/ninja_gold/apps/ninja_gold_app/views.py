from django.shortcuts import render, HttpResponse, redirect
import random, datetime

def index(request):
    if not request.session.get('gold'):
        request.session['gold'] = 0
        request.session['activities'] = ""
    return render(request, "ninja_gold_app/index.html")
   
def gold(request):
    if request.POST.get('farm'):
        num = random.randint(10,20)
        request.session['gold'] += num
        request.session['activities'] += f"Earned {num} gold from farm! {datetime.datetime.now()}<br>"

    elif request.POST.get('cave'):
        num = random.randint(5,10)
        request.session['gold'] += num
        request.session['activities'] += f"Earned {num} gold from cave! {datetime.datetime.now()}<br>"

    elif request.POST.get('house'):
        num = random.randint(2,5)
        request.session['gold'] += num
        request.session['activities'] += f"Earned {num} gold from house! {datetime.datetime.now()}<br>"
        
    elif request.POST.get('casino'):
        num = random.randint(-50,50)
        request.session['gold'] += num
        if num <= 0:
            request.session['activities'] += f"Lost {num} gold from casino! {datetime.datetime.now()}<br>"
        else:
            request.session['activities'] += f"Earned {num} gold from casino! {datetime.datetime.now()}<br>"
    return redirect('/')