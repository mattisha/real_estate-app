from django.shortcuts import render

def home(requests):
    return render(requests, 'pages/home.html')

def about(requests):
    return render(requests, 'pages/about.html')
