from django.urls import path
from wishlist.views import *

urlpatterns = [
    path('search-book/<str:title>/<str:author>/<str:publisher>/<str:apikey>',Title_Author_Publisher.as_view()),
    path('search-bookTA/<str:title>/<str:author>/<str:apikey>',Title_Author.as_view()),
    path('search-bookTP/<str:title>/<str:publisher>/<str:apikey>',Title_Publisher.as_view()),
    path('search-bookAP/<str:author>/<str:publisher>/<str:apikey>',Author_Publisher.as_view()),
    path('my-bookshelve-all/<int:user>/<str:apikey>',My_BookShelves_Public_All.as_view()),
    path('my-bookshelve-specific/<int:user>/<int:bookshelve>/<str:apikey>',My_BookShelves_Public_Specific.as_view()),
    path('list-bookshelve/<int:user>/<int:bookshelve>/<str:apikey>',List_BookShelves_Public.as_view()),
    path('list-bookshelve-mylibrary/<str:apikey>',List_BookShelves_Private.as_view()),
    path('callAPI/',callAPI.as_view()),
    path('connectAPI/',connectBigQuery.as_view()),
]