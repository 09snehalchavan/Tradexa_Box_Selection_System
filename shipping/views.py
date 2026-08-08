from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Box, Product, Order
from .serializers import BoxSerializer, ProductSerializer, OrderSerializer
from .services import recommend_box

# Create your views here.

class BoxListAPIView(APIView):

    def get(self, request):
        boxes = Box.objects.all()
        serializer = BoxSerializer(boxes, many=True)
        return Response(serializer.data)


class RecommendBoxAPIView(APIView):

    def post(self, request):

        products_data = request.data.get("products", [])

        if not products_data:
            return Response(
                {"error": "Products are required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        products = []

        for product_data in products_data:
            serializer = ProductSerializer(data=product_data)

            if not serializer.is_valid():
                return Response(
                    serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST
                )

            product = serializer.save()
            products.append(product)

        boxes = Box.objects.all()

        recommended_box = recommend_box(products, boxes)

        if not recommended_box:
            return Response(
                {"error": "No suitable box found."},
                status=status.HTTP_400_BAD_REQUEST
            )

        order = Order.objects.create(
            recommended_box=recommended_box
        )

        order.products.set(products)

        return Response(
            {
                "order_id": order.id,
                "recommended_box": recommended_box.name,
                "cost": recommended_box.cost,
            },
            status=status.HTTP_201_CREATED
        )


class OrderListAPIView(APIView):

    def get(self, request):
        orders = Order.objects.all().order_by("-created_at")
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)