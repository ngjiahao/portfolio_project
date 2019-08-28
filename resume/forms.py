from django import forms
from .models import Feedback


# class FeedbackForm(forms.Form):
#     choice_tup = (("1", "Not Satisfied"), ("2", "Less Satisfied"), ("3", "Moderate"),
#                   ("4", "Satisfied"), ("5", "Awesome"))
#     user = forms.CharField(max_length=100)
#     rating = forms.ChoiceField(widget=forms.RadioSelect, choices=choice_tup)
#     comments = forms.CharField(max_length=1000, widget=forms.Textarea)


class FeedbackForm(forms.ModelForm):
    choice_tup = (("1", "Not Satisfied"), ("2", "Less Satisfied"), ("3", "Moderate"),
                  ("4", "Satisfied"), ("5", "Awesome"))
    rating = forms.ChoiceField(widget=forms.RadioSelect(), choices=choice_tup)

    class Meta:
        model = Feedback
        fields = ["interviewer", "rating", "comments"]

