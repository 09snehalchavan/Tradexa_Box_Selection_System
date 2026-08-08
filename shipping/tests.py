from django.test import TestCase
from decimal import Decimal
from rest_framework.test import APIClient
from .models import Box

# Create your tests here.


class ShippingAPITestCase(TestCase):

    def setUp(self):
        self.client = APIClient()

        self.small_box = Box.objects.create(
            name="Small Box",
            length=35,
            width=25,
            height=10,
            max_weight=5,
            cost=40
        )

        self.medium_box = Box.objects.create(
            name="Medium Box",
            length=45,
            width=35,
            height=20,
            max_weight=10,
            cost=70
        )

    def test_get_boxes(self):
        response = self.client.get("/api/boxes/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_recommend_small_box(self):
        data = {
            "products": [
                {
                    "name": "Laptop",
                    "length": 30,
                    "width": 20,
                    "height": 5,
                    "weight": 2
                }
            ]
        }

        response = self.client.post(
            "/api/recommend-box/",
            data,
            format="json"
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            response.data["recommended_box"],
            "Small Box"
        )

    def test_no_suitable_box(self):
        data = {
            "products": [
                {
                    "name": "Huge Machine",
                    "length": 100,
                    "width": 100,
                    "height": 100,
                    "weight": 50
                }
            ]
        }

        response = self.client.post(
            "/api/recommend-box/",
            data,
            format="json"
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.data["error"],
            "No suitable box found."
        )