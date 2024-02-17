from django.shortcuts import render

def top_page(request):
    return render(request, 'top.html')