from django.shortcuts import render

def home(requests):
    return render(requests, 'pages/home.html')