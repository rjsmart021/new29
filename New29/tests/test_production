# get app.py from parent directory
import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)
from app import create_app

import unittest
from unittest.mock import MagicMock, patch
from faker import Faker
from datetime import date

fake = Faker()

class TestProductionEndpoint(unittest.TestCase):
    def setUp(self):
        app = create_app('DevelopmentConfig')
        app.config['TESTING'] = True
        self.app = app.test_client()

    # test successful creation of production
    @patch('services.productionService.save')
    def test_create_production(self, mock_save):
        product_id = fake.random_digit_not_null()
        quantity_produced = fake.pyint(20, 2000, 10)
        # date_produced = fake.date_this_year() # MagicMock kept giving me this error: TypeError: descriptor 'isoformat' for 'datetime.date' objects doesn't apply to a 'MagicMock' object
        # so I hardcoded the value and changed the schema to take a string as a temporary solution
        date_produced = "2024-05-24"
        mock_production = MagicMock()
        mock_production.id = 1
        mock_production.product_id = product_id
        mock_production.quantity_produced = quantity_produced
        mock_production.date_produced = date_produced
        mock_save.return_value = mock_production

        payload = {
                "product_id": product_id,
                "quantity_produced": quantity_produced,
                "date_produced": date_produced
            }
        
        response = self.app.post('/productions/', json=payload)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['id'], mock_production.id)

    # test creation of production without date_produced
    @patch('services.productionService.save')
    def test_missing_date_produced_payload(self, mock_save):
        product_id = fake.random_digit_not_null()
        quantity_produced = fake.pyint(20, 2000, 10)
        mock_production = MagicMock()
        mock_production.id = 1
        mock_production.product_id = product_id
        mock_production.quantity_produced = quantity_produced
        mock_save.return_value = mock_production

        payload = {
                "product_id": product_id,
                "quantity_produced": quantity_produced,
            }

        response = self.app.post('/productions/', json=payload)

        self.assertEqual(response.status_code, 400)
        self.assertIn('date_produced', response.json)

    # test creation of production with superfluous data
    @patch('services.productionService.save')
    def test_extra_data_production(self, mock_save):
        product_id = fake.random_digit_not_null()
        quantity_produced = fake.pyint(20, 2000, 10)
        date_produced = fake.date_this_year()
        mock_production = MagicMock()
        mock_production.id = 1
        mock_production.product_id = product_id
        mock_production.quantity_produced = quantity_produced
        mock_production.date_produced = date_produced
        mock_save.return_value = mock_production

        payload = {
                "product_id": product_id,
                "quantity_produced": quantity_produced,
                "date_produced": date_produced,
                "qa_inspector": "Ted Quality"
            }
        
        response = self.app.post('/productions/', json=payload)

        self.assertEqual(response.status_code, 400)