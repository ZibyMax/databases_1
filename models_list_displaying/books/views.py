from datetime import datetime

from django.views import generic

from books.models import Book


class BookListView(generic.ListView):
    model = Book

#    def get_context_data(self, **kwargs):
#        pass

    def get_queryset(self, **kwargs):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        day = self.kwargs.get('day')
        if year and month and day:
            pub_date = datetime.strptime(f'{year}.{month}.{day}', '%Y.%m.%d')
            print(pub_date)
            return super(BookListView, self).get_queryset().filter(pub_date=pub_date)
        return super(BookListView, self).get_queryset()
