from datetime import datetime
from django.core.paginator import Paginator
from django.views import generic

from books.models import Book


class BookListView(generic.ListView):
    model = Book


class BookListDateView(generic.ListView):
    model = Book
    paginate_by = 1

    def get_context_data(self, **kwargs):
        str_date = self.kwargs.get('date')
        pub_date = datetime.strptime(f'{str_date}', '%Y-%m-%d')
        context = super(BookListDateView, self).get_context_data(**kwargs)
        print(context['page_obj'])
        return context

    def get_queryset(self, **kwargs):
        context = super(BookListDateView, self).get_queryset().order_by('pub_date')
        return context

        #context = super(BookListDateView, self).get_context_data(**kwargs).filter('pub_date')
        #context['book_list'] = context['book_list'].filter('pub_date')