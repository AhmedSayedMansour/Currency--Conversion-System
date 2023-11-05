from collections import OrderedDict

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class PageNumberAndSizePagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    page_size = 10
    max_page_size = 1000

    def get_paginated_response(self, data):
        return Response(
            OrderedDict(
                [
                    ('count', self.page.paginator.count), ('next', {
                        'page': self.page.next_page_number() if self.page.has_next() else None, 'page_size': self.get_page_size(
                            self.request)}), ('previous', {
                                'page': self.page.previous_page_number() if self.page.has_previous() else None, 'page_size': self.get_page_size(
                                    self.request)}), ('results', data)]))
