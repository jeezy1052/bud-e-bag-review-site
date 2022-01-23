from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Reviewer
from .forms import  ReviewForm



# Create your views here.

def index(request):
    return render(request, 'crud_app/index.html')

def review_form(request):
    submitted = False
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/review_form?submitted=True')
    else:
        form = ReviewForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'crud_app/review_form.html', {'form':form} )

def database_page(request):
    reviewer = Reviewer.objects.all()
    context_dict = {'reviewer_from_context': reviewer}
    return render(request, 'crud_app/database_page.html', context_dict)

def success(request):
    return render(request,'crud_app/success.html')

