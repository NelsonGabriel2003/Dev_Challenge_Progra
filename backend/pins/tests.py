from django.test import TestCase
from pins.forms import RutaForm
from pins.models import Ruta

class RutaFormTest(TestCase):

    def test_ruta_form_valid_data(self):
        """
        Test that the RutaForm is valid with correct data.
        """
        form_data = {
            'titulo': 'Ruta de prueba',
            'descripcion': 'Esta es una descripción de prueba.',
            'punto_inicio': 'Origen de prueba',
            'punto_destino': 'Destino de prueba',
            'tipo_transporte': 'BUS',
        }
        form = RutaForm(data=form_data)
        self.assertTrue(form.is_valid(), f"Form is not valid: {form.errors}")

    def test_ruta_form_invalid_data_missing_fields(self):
        """
        Test that the RutaForm is invalid when required fields are missing.
        """
        form_data = {
            'titulo': '',  # Missing required field
            'descripcion': 'Esta es una descripción de prueba.',
            'punto_inicio': 'Origen de prueba',
            'punto_destino': 'Destino de prueba',
            'tipo_transporte': 'BUS',
        }
        form = RutaForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('titulo', form.errors)

    def test_ruta_form_invalid_tipo_transporte(self):
        """
        Test that the RutaForm is invalid with an invalid tipo_transporte.
        """
        form_data = {
            'titulo': 'Ruta de prueba',
            'descripcion': 'Esta es una descripción de prueba.',
            'punto_inicio': 'Origen de prueba',
            'punto_destino': 'Destino de prueba',
            'tipo_transporte': 'INVALIDO',  # Invalid choice
        }
        form = RutaForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('tipo_transporte', form.errors)

    def test_ruta_form_no_data(self):
        """
        Test that the RutaForm is invalid with no data.
        """
        form = RutaForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 5) # All fields are required