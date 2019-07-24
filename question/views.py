from question.models import Question
from question.forms import QuestionForm
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
# Create your views here.

def home(request):
    question = Question.objects.all()
    return render(request, "question/home.html", {'question': question})

def create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            data = form.save()
            messages.success(request, data.title + 'Added Successfully')
            return redirect("/show/")

        # else:
        #     messages.error(request, "Unsuccessful")
    else:
        form = QuestionForm()
    return render(request, 'question/index.html', {'form': form})

def show(request):
    question = Question.objects.all()
    return render(request, "question/show.html", {'question': question})

def edit(request,id):
    try:
        form = QuestionForm()
        question = Question.objects.get(id = id)
        return render(request, 'question/edit.html', {'question': question, 'form': form})
    except:
        return HttpResponse('Object not in database')

def update(request,id):
    question = Question.objects.get(id=id)
    form = QuestionForm(request.POST, instance = question)
    # print(id)
    if form.is_valid():
        data = form.save()
        # print("Hello")
        messages.success(request, data.title + 'Updated Successfully')
        return redirect("/show/")
    else:
        # messages.error(request, "Update Failure")
        return render(request, 'question/edit.html', {'question': question,'form':form})

def delete(request,id):
    question = Question.objects.get(id = id)
    title = question.title

    if request.method == "POST":
        question.delete()
        messages.success(request, title + 'Deleted Successfully')
        return redirect("/show/")

    return render(request, 'question/delete.html', {'question': question})


# def error(request):
#     form = QuestionForm(request.POST, instance=question)
#     if form.is_valid:
#         form.save()
#         return redirect("show")
#     else:
#         form.errors(request, "/error/")