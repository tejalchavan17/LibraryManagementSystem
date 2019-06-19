from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Books,Issue
from LMS.forms import BooksForm
from LMS.forms import IssueForm

class HomeView(TemplateView):
   template_name = "LMS/home.html"

class AddView(TemplateView):
 template_name = "LMS/Add.html"

class DeleteView(TemplateView):
 template_name = "LMS/Delete.html"

class UpdateView(TemplateView):
     template_name = "LMS/Update.html"

class ListView(TemplateView):
         template_name = "LMS/List.html"

class IssueView(TemplateView):
             template_name = "LMS/Issue.html"

class IssuedBookView(TemplateView):
    template_name = "LMS/IssuedBook.html"

class ReturnBookView(TemplateView):
    template_name = "LMS/ReturnBook.html"

def BooksView(request):
    if request.method == 'POST':

        form = BooksForm(request.POST)
        if form.is_valid():
            print("HI")
            Book_id = request.POST.get('Book_id')
            Title = request.POST.get('Title')
            Author = request.POST.get('Author')
            Branch = request.POST.get('Branch')
            Quantity = request.POST.get('Quantity')
            book_obj = Books(Book_id = Book_id, Title = Title, Author = Author, Branch = Branch,Quantity = Quantity)
            book_obj.save()

            return  render(request, 'LMS/home.html')#HttpResponseRedirect(reverse('LMS:home'))
        else:
            form = BooksForm()
            context = {
                "form": form,
            }
            return render(request, 'LMS/home.html', context)

def BooksUpdateView(request):
    if request.method == 'POST':
        form = BooksForm(request.POST)
        if form.is_valid():
            all_books = Books.objects.all()
            for books in all_books:
                book_id=books.Book_id
                if request.POST.get('Book_id') == book_id:
                    print("Hello")
                    book_id = request.POST.get('Book_id')
                    title = request.POST.get('Title')
                    author = request.POST.get('Author')
                    branch = request.POST.get('Branch')
                    quantity = request.POST.get('Quantity')

                    book_obj1 = Books(Book_id=book_id, Title=title, Author=author, Branch=branch, Quantity=quantity)
                    book_obj1.save()

                    return render(request, 'LMS/home.html')  # HttpResponseRedirect(reverse('LMS:home'))
        else:
            return render(request, 'LMS/home.html')


def ListDataView(request):
    if request.method == 'POST':
        all_books = Books.objects.filter(Branch = request.POST.get('Branch'))
        context = {
            "all_books": all_books,
        }
        return render(request, 'LMS/ListData.html', context)

def Homeview(request):
    if request.method == 'POST':
        return render(request, 'LMS/home.html')
    else:
        return render(request, 'LMS/home.html')

def BooksIssueView(request):
    if request.method == 'POST':

        form = IssueForm(request.POST)
        if form.is_valid():
            all_books = Books.objects.all()
            for books in all_books:
                if request.POST.get('Book_id') == books.Book_id:
                    print("HI")
                    books.Quantity=books.Quantity-1
                    books.save()
                    Student_id = request.POST.get('Student_id')
                    #Book_id = request.POST.get('Book_id')
                    Brnch = request.POST.get('Brnch')
                    Return_date = request.POST.get('Return_date')
                    issue_obj = Issue(Student_id = Student_id, Book_id = books, Brnch = Brnch, Return_date = Return_date)
                    issue_obj.save()

            return  render(request, 'LMS/home.html')#HttpResponseRedirect(reverse('LMS:home'))
        else:
            form = IssueForm()
            context = {
                "form": form,
            }
        return render(request, 'LMS/home.html', context)

def BooksDeleteView(request):
    if request.method == 'POST':
        all_issue = Issue.objects.all()
        for issue in all_issue:
            bookid = issue.Book_id_id
            if bookid == request.POST.get('Book_id'):
                print("delete")
                context = {
                    "Book_id": issue.Book_id_id,
                    "Student_id": issue.Student_id,
                }
                return render(request, 'LMS/DeleteBook.html', context)
        book = Books.objects.filter(Book_id=request.POST.get('Book_id'))
        book.delete()
        return render(request, 'LMS/home.html')

def IssuedDataView(request):
    if request.method == 'POST':
        all_issue = Issue.objects.filter(Student_id = request.POST.get('Student_id'))
        context = {
            "all_issue": all_issue,
        }
        return render(request, 'LMS/IssuedData.html', context)

def ReturnView(request):
    if request.method == 'POST':
        all_issue = Issue.objects.all()
        for issue in all_issue:
            bookid = issue.Book_id_id
            studid = issue.Student_id
            if bookid == request.POST.get('Book_id'):
                if studid == request.POST.get('Student_id'):
                    issue.delete()
        all_books = Books.objects.all()
        for books in all_books:
            bid = books.Book_id
            if bid == request.POST.get('Book_id'):
                books.Quantity = books.Quantity + 1
                books.save()
        return render(request, 'LMS/home.html')