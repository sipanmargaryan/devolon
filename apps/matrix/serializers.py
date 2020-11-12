from rest_framework import serializers


__all__ = (
    'MatrixSerializer',
)


class MatrixSerializer(serializers.Serializer):
    product = serializers.ListField(
        child=serializers.ListField(
            child=serializers.ListField(
                child=serializers.IntegerField()
            ),
            min_length=2
        )
    )
