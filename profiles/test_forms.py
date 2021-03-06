from django.test import TestCase
from django.contrib.auth import get_user_model
from .forms import UserProfileForm


class TestProfileForms(TestCase):

    def test_create_UserProfileForm(self):
        form = UserProfileForm({
            'full_name': 'test',
            'email': 'test@gmail.com',
            'phone_number': '123456 789',
            'address_line1': '123 test street',
            'town_or_city': 'test city',
            'country': 'RU'})
        self.assertTrue(form.is_valid())
