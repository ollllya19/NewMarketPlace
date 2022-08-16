from api.models import Product


class ProductRepository:

    @staticmethod
    def get_all():
        return Product.objects.all()
    