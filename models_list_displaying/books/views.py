from datetime import datetime
from django.core.paginator import Paginator
from django.views import generic

from books.models import Book


class BookListView(generic.ListView):
    model = Book

class BookListPageView(generic.ListView):
    model = Book
    #paginate_by = 1

    def get_context_data(self, **kwargs):
        print(111)
        context = super(BookListPageView, self).get_context_data(**kwargs)
        context['book_list'] = Book.objects.all().order_by('pub_date')
        return context

    def get_queryset(self, **kwargs):
        print(222)
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        day = self.kwargs.get('day')
        if year and month and day:
            pub_date = datetime.strptime(f'{year}.{month}.{day}', '%Y.%m.%d')
            context = super(BookListPageView, self).get_queryset().filter(pub_date=pub_date)
            return context
        return super(BookListPageView, self).get_queryset()
