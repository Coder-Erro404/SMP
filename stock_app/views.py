from django.shortcuts import render, redirect
from stock_app.lstm_prediction import *
from .models import Contact
from django.contrib import  messages
from .models import Contact

# --------------- MAIN WEB PAGES -----------------------------
def redirect_root(request):
    return redirect('/pred_app/index')

def index(request):

	return render(request, 'pred_app/index.html')
	 

def pred(request):
    return render(request, 'pred_app/prediction.html')

def contact(request):
    if request.method=="POST":
        F_name=request.POST['F_name']
        L_name=request.POST['L_name']
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
        if len(F_name)<2 or len(L_name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact=Contact(F_name=F_name,L_name=L_name , email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request, 'pred_app/contact.html')
def search(request, se, stock_symbol):
	import json
	predicted_result_df = lstm_prediction(se, stock_symbol)
	return render(request, 'pred_app/search.html', {"predicted_result_df": predicted_result_df})
# -----------------------------------------------------------