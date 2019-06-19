from django.urls import path
from LMS.views import HomeView
from LMS.views import AddView
from LMS.views import DeleteView
from LMS.views import UpdateView
from LMS.views import ListView
from LMS.views import IssueView
from LMS.views import IssuedBookView
from LMS.views import ReturnBookView
from LMS import views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('Add/', AddView.as_view(), name='add'),
    path('addbook/', views.BooksView),
    path('Delete/', DeleteView.as_view(), name='delete'),
    path('deletebook/', views.BooksDeleteView),
    path('Update/', UpdateView.as_view(), name='update'),
    path('updatebook/', views.BooksUpdateView),
    path('List/', ListView.as_view(), name='list'),
    path('listbook/', views.ListDataView),
    path('Issue/', IssueView.as_view(), name='issue'),
    path('issuebook/', views.BooksIssueView),
    path('IssuedBook/', IssuedBookView.as_view(), name='issuedbook'),
    path('issueddata/', views.IssuedDataView),
    path('ReturnBook/', ReturnBookView.as_view(), name='returnbook'),
    path('return/', views.ReturnView),

]
