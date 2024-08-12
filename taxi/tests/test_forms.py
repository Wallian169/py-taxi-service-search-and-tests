from django.test import TestCase
from taxi.forms import DriverLicenseUpdateForm, DriverCreationForm


class TestForm(TestCase):
    def test_driver_license_update_valid_data(self):
        data = {
            "license_number": "VVM45456"
        }
        form = DriverLicenseUpdateForm(data=data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["license_number"], "VVM45456")

    def test_driver_license_update_invalid_data(self):
        data = {
            "license_number": "Vdd09090"
        }
        form = DriverLicenseUpdateForm(data=data)
        self.assertFalse(form.is_valid())

    def test_driver_license_update_missing_data(self):
        form = DriverLicenseUpdateForm(data={})
        self.assertFalse(form.is_valid())

    def test_driver_create_form_valid_data(self):
        data = {
            "username": "user123",
            "password1": "79zilivi",
            "password2": "79zilivi",
            "first_name": "John",
            "last_name": "Doe",
            "license_number": "VVM45456",
        }
        form = DriverCreationForm(data=data)
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_driver_create_form_invalid_data(self):
        data = {
            "username": "user123",
            "password1": "79zilivi",
            "password2": "79zilivi",
            "first_name": "John",
            "last_name": "Doe",
            "license_number": "is_missing",
        }
        form = DriverCreationForm(data=data)
        self.assertFalse(form.is_valid())
