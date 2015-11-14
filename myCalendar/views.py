from django.shortcuts import render

# Create your views here.
<<<<<<< HEAD
def main( request ):
    return HttpResponseRedirect(reverse('polls:results'))
=======
def main(request):
    return HttpResponse("You're looking at question %s." % question_id)
>>>>>>> origin/master
