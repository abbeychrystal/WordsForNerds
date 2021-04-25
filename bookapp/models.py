from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

# Create your models here.
class Book(models.Model):
    CATEGORY_CHOICES = [
        ('Fiction', 'Fiction'),
        ('Nonfiction', 'Nonfiction'),
    ]
    
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES)
    summary = models.TextField()
    # cover_image = models.ImageField(null=True, blank=True, upload_to="images/")
    discussion_date = models.DateField() #widget DateInput
    purchase_link = models.URLField(max_length=255, null=True, blank=True) # widget - URLInput
    is_current = models.BooleanField()
    uploaded_by = models.ForeignKey(User, related_name="uploaded_books", on_delete=models.CASCADE)
    # users_who_like = models.ManyToManyField(User, related_name="liked_books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # this method will allow us to see the title of the book on the admin page instead of just the object location etc
    def __str__(self):
        return self.title

    # this method tells the browser where to go after submitting the form. In the current iteration, it is the equivalent of a redirect statement in a views.py method. The args provide the primary key id for this newly added book so we can go to the page to display the book that we just added
    def get_absolute_url(self):
        return reverse('book_details', args=(str(self.id)))
        # to redirect to home, you would just need:
        # return reverse('home')
