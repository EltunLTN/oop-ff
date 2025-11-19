import unittest
import os
import sys
from datetime import datetime

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from models.car import Car
from models.client import Client
from models.rental import Rental


class TestCar(unittest.TestCase):

    def setUp(self):
        self.car = Car('C001', 'Toyota', 'Camry', 50.0, 'Sedan', 5)

    def test_inheritance(self):
        """Inheritance testi"""
        self.assertEqual(self.car.vehicle_id, 'C001')
        self.assertIsInstance(self.car, Car)

    def test_polymorphism(self):
        """Polymorphism testi"""
        cost = self.car.calculate_rental_cost(3)
        self.assertEqual(cost, 150.0)

    def test_polymorphism_suv(self):
        """Polymorphism testi - SUV üçün əlavə ödəniş"""
        suv_car = Car('C002', 'Honda', 'CR-V', 70.0, 'SUV', 7)
        cost = suv_car.calculate_rental_cost(3)
        # 70 * 3 * 1.2 = 252.0
        self.assertEqual(cost, 252.0)

    def test_encapsulation(self):
        """Encapsulation testi"""
        self.assertTrue(self.car.is_available)
        self.car.is_available = False
        self.assertFalse(self.car.is_available)

    def test_to_dict(self):
        """Serialization testi"""
        car_dict = self.car.to_dict()
        self.assertEqual(car_dict['vehicle_id'], 'C001')
        self.assertEqual(car_dict['brand'], 'Toyota')
        self.assertEqual(car_dict['car_type'], 'Sedan')

    def test_from_dict(self):
        """Deserialization testi"""
        car_dict = {
            'vehicle_id': 'C003',
            'brand': 'BMW',
            'model': '320i',
            'daily_rate': 100.0,
            'car_type': 'Sedan',
            'seats': 5,
            'is_available': True
        }
        car = Car.from_dict(car_dict)
        self.assertEqual(car.vehicle_id, 'C003')
        self.assertEqual(car.brand, 'BMW')


class TestClient(unittest.TestCase):

    def setUp(self):
        self.client = Client('CL001', 'John Doe', 'john@example.com', '+1234567890')

    def test_client_properties(self):
        """Client properties testi"""
        self.assertEqual(self.client.client_id, 'CL001')
        self.assertEqual(self.client.name, 'John Doe')
        self.assertEqual(self.client.email, 'john@example.com')

    def test_to_dict(self):
        """Client serialization testi"""
        client_dict = self.client.to_dict()
        self.assertEqual(client_dict['client_id'], 'CL001')
        self.assertEqual(client_dict['name'], 'John Doe')

    def test_from_dict(self):
        """Client deserialization testi"""
        client_dict = {
            'client_id': 'CL002',
            'name': 'Jane Smith',
            'email': 'jane@example.com',
            'phone': '+0987654321'
        }
        client = Client.from_dict(client_dict)
        self.assertEqual(client.client_id, 'CL002')
        self.assertEqual(client.name, 'Jane Smith')


class TestRental(unittest.TestCase):

    def setUp(self):
        self.car = Car('C001', 'Toyota', 'Camry', 50.0, 'Sedan', 5)
        self.client = Client('CL001', 'John Doe', 'john@example.com', '+1234567890')
        self.start_date = datetime(2024, 1, 1)
        self.rental = Rental('R001', self.car, self.client, self.start_date)

    def test_composition(self):
        """Composition testi"""
        self.assertEqual(self.rental.car.vehicle_id, 'C001')
        self.assertEqual(self.rental.client.client_id, 'CL001')

    def test_calculate_total_cost(self):
        """Rental cost calculation testi"""
        end_date = datetime(2024, 1, 4)  # 3 days
        self.rental.end_date = end_date
        cost = self.rental.calculate_total_cost()
        # 50 * 3 = 150
        self.assertEqual(cost, 150.0)

    def test_complete_rental(self):
        """Complete rental testi"""
        self.assertTrue(self.rental.is_active)
        self.assertTrue(self.car.is_available)
        
        self.rental.complete_rental()
        
        self.assertFalse(self.rental.is_active)
        self.assertTrue(self.car.is_available)  # Car should be available again


if __name__ == '__main__':
    unittest.main()

