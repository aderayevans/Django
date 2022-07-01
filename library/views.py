from django.shortcuts import render
# from .models import Choice, Question


def index(request):
    return render(request, 'library/index.html')
    # return HttpResponse("Hello, world. You're at the library index.")
