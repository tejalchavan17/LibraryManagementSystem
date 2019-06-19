from django import forms


class BooksForm(forms.Form):
    Book_id = forms.CharField()
    Title = forms.CharField()
    Author = forms.CharField()
    Branch = forms.CharField()
    Quantity = forms.IntegerField()


class IssueForm(forms.Form):
    Student_id = forms.CharField()
    Book_id = forms.CharField()
    Brnch = forms.CharField()
    Return_date = forms.DateField()

