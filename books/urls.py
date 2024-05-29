from django.urls import path
from .views import CategoryList, AuthorList, Booklist, Bookdetail, BookDelete, BookUpdate
urlpatterns = [
    path('category/', CategoryList.as_view()),
    path('author/', AuthorList.as_view()),
    path('book/', Booklist.as_view()),
    path('book/<int:pk>/', Bookdetail.as_view()),
    path('book/delete/<int:pk>/', BookDelete.as_view()),
    path('book/update/<int:pk>/', BookUpdate.as_view()),



]
