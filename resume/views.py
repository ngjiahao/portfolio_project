from django.shortcuts import render
from .forms import FeedbackForm


def home(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        feedback_form = FeedbackForm(request.POST)

        # check whether it's valid:
        if feedback_form.is_valid():
            feedback_form.save()
            note = "Thanks for your valuable feedback to Jia Hao, {}! " \
                   "Feedback has been saved to database.".format(feedback_form.cleaned_data["interviewer"])
            return render(request, "home.html", context={"note": note, "feedback": feedback_form})

    # if a GET (or any other method) we'll create a blank form
    else:
        feedback_form = FeedbackForm()

    return render(request, "home.html", context={"feedback": feedback_form})


def employment(request):
    return render(request, "employment.html")


def education(request):
    return render(request, "education.html")


def tech_experience(request):
    return render(request, "tech_experience.html")


def add_experience(request):
    return render(request, "add_experience_awards.html")


def language(request):
    return render(request, "language.html")
