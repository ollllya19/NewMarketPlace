from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework .permissions import IsAuthenticated
from .serializers import AllProductsSerializer, CartSerializer, CartCreateSerializer, OrderSerializer

from api.models import Product
from .models import Cart, Order, OrderItem
    
    
class AllProductsViewSet(ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = AllProductsSerializer


class CartsViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    
    def list(self, request):
        queryset = (
            Cart.objects
            .filter(user=request.user)
            #.values_list('product', 'col')
        )
        
        serializer = CartSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        cart_item = Cart(
            product=Product.objects.get(id=request.data['product']),
            col=request.data['col'],
            user=request.user
        )
        cart_item.save()
        serializer = CartCreateSerializer(cart_item)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        cart_item = (
            Cart.objects.get(id=pk)
            #.values('product', 'col')
        )
        serializer = CartSerializer(cart_item)
        return Response(serializer.data)
    
    def destroy(self, request, pk=None):
        cart_item = Cart.objects.get(id=pk)
        cart_item.delete()
        print("Object was deleted")
        return Response({'delete': 'Object was deleted'})
    

class OrderViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    
    def list(self, request):
        order_queryset = Order.objects.filter(user=request.user)
        order_serializer = OrderSerializer(order_queryset, many=True)
        return Response(order_serializer.data)
    
    def create(self, request):
        # order creation
        order = Order(
            deliv_date=request.data['deliv_date'],
            user=request.user,
            address=request.data['address']
        )
        order.save()
        
        # order items creation
        products = request.data['products']
        for product_item in products:
            new_order_item = OrderItem(
                order=Order.objects.get(id=order.id),
                product=Product.objects.get(id=product_item['id']),
                col=product_item['col']
            )
            new_order_item.save()
        
        serializer = OrderSerializer(order)
        return Response(serializer.data)
    