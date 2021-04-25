from django import forms
from .models import Book

# trying to get date widget to show a calendar to pick date
# class DateInput(forms.DateInput):
#     input_type = 'date'

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'discussion_date', 'category', 'summary', 'is_current', 'purchase_link', 'uploaded_by') 

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'discussion_date': forms.SelectDateWidget(attrs={'class': 'form-control'}),
            # 'discussion_date': forms.DateInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'summary': forms.Textarea(attrs={'class': 'form-control'}),
            'is_current': forms.NullBooleanSelect(attrs={'class': 'form-control'}),
            'purchase_link': forms.URLInput(attrs={'class': 'form-control'}),
            'uploaded_by': forms.Select(attrs={'class': 'form-control'}),
        }

class UpdateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'discussion_date', 'category', 'summary', 'is_current', 'purchase_link', 'uploaded_by') 

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'discussion_date': forms.SelectDateWidget(attrs={'class': 'form-control'}),
            # 'discussion_date': forms.DateInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'summary': forms.Textarea(attrs={'class': 'form-control'}),
            'is_current': forms.NullBooleanSelect(attrs={'class': 'form-control'}),
            'purchase_link': forms.URLInput(attrs={'class': 'form-control'}),
            'uploaded_by': forms.Select(attrs={'class': 'form-control'}),
        }