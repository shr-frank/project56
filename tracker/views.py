from django.shortcuts import render
def sample(request):
    context = {'latest_question_list': 'hello'}
    return render(request, 'tracker/sample.html', context)


# Create your views here.
