from django.shortcuts import render

# Create your views here.
def main(request):
    return HttpResponse("You're looking at question %s." % question_id)
