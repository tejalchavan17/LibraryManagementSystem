from django.db import models

# Create your models here.

class Options(models.Model):
    Option = models.CharField(max_length=30)

    def __str__(self):
        return self.Option


class Books(models.Model):
    Book_id = models.CharField(max_length=10, primary_key=True)
    Title = models.CharField(max_length=100)
    Author = models.CharField(max_length=200)
    Branch = models.CharField(max_length=50)
    Quantity = models.IntegerField()



    def __str__(self):
        return self.Book_id


class Issue(models.Model):
    Student_id = models.CharField(max_length=15)
    Book_id = models.ForeignKey(Books, on_delete=models.CASCADE, verbose_name="Book_id")
    Brnch = models.CharField(max_length=50)
    Return_date = models.DateField()

    def __str__(self):
        return self.Student_id








