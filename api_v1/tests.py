import io
import tempfile

from PIL import Image
from django.conf import settings
from django.test import override_settings
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from core.models import MenuItem

MEDIA_ROOT = tempfile.mkdtemp()


@override_settings(MEDIA_ROOT=MEDIA_ROOT)
class TestMenuItemApi(APITestCase):
    url = reverse('menu-items-list')

    @staticmethod
    def generate_picture():
        file = io.BytesIO()
        image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        return file

    @staticmethod
    def build_data():
        picture = TestMenuItemApi.generate_picture()
        data = {
            'name': 'Test',
            'price': 100,
            'nutrition_value': 1000,
            'picture': picture,
        }
        return data

    def test_menu_item_create(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + settings.API_TOKEN)
        response = self.client.post(self.url, self.build_data(), format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(MenuItem.objects.count(), 1)

    def test_incorrect_token(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + settings.API_TOKEN + '1')
        response = self.client.post(self.url, self.build_data(), format='multipart')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_missing_token(self):
        response = self.client.post(self.url, self.build_data(), format='multipart')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
