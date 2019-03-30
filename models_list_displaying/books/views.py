from datetime import datetime
from django.views import generic

from books.models import Book


class BookListView(generic.ListView):
    model = Book


class BookListDateView(generic.ListView):
    model = Book

    def get_context_data(self, **kwargs):
        date = datetime.strptime(self.kwargs.get('date'), '%Y-%m-%d').date()
        context = super(BookListDateView, self).get_context_data(**kwargs)
        context['book_list'] = Book.objects.order_by('pub_date').filter(pub_date__exact=date)
        context['prev_book'] = Book.objects.order_by('pub_date').filter(pub_date__lt=date).last()
        context['next_book'] = Book.objects.order_by('pub_date').filter(pub_date__gt=date).first()
        if context['prev_book']:
            context['prev_book_url'] = context['prev_book'].pub_date.strftime('%Y-%m-%d')
        if context['next_book']:
            context['next_book_url'] = context['next_book'].pub_date.strftime('%Y-%m-%d')
        return context
