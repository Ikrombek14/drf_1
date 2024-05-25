from django.urls import path
from .views import CategoryList, AuthorList, Booklist, Bookdetail
urlpatterns = [
    path('category/', CategoryList.as_view()),
    path('author/', AuthorList.as_view()),
    path('book/', Booklist.as_view()),
    path('book/<int:pk>/', Bookdetail.as_view()),

]
