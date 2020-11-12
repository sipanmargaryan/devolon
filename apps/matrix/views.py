from rest_framework import generics
from rest_framework.response import Response

from .serializers import MatrixSerializer

__all__ = (
    'ProductAPIView',
)


class ProductAPIView(generics.CreateAPIView):
    serializer_class = MatrixSerializer

    def post(self, request, *args, **kwargs):
        product = request.data['product']
        while len(product) > 1:
            first, second = product[:2]
            result = [[sum(a * b for a, b in zip(first_row, second_col))
                       for second_col in zip(*second)] for first_row in first]
            product = product[2:]
            product.insert(0, result)
        return Response(product)
