from rest_framework.pagination import LimitOffsetPagination

# specifies the maximum number that is acepted for the limit query parameter.
# the generic view will use the declared limit/offset oagination scheme set below rather 
# than the defaults in settings.py.


class LimitOffsetPaginationWithUpperBound(LimitOffsetPagination):
    # set the maximum limit value to 10
    max_limit = 10
