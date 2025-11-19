from .base import Vehicle


class Car(Vehicle):
    """Concrete class - Inheritance və Polymorphism"""

    def __init__(self, vehicle_id: str, brand: str, model: str,
                 daily_rate: float, car_type: str, seats: int):
        super().__init__(vehicle_id, brand, model, daily_rate)
        self._car_type = car_type  # SUV, Sedan, etc.
        self._seats = seats

    def calculate_rental_cost(self, days: int) -> float:
        """Polymorphism - Override abstract method"""
        base_cost = self._daily_rate * days
        # Premium car type üçün əlavə ödəniş
        if self._car_type.lower() == 'suv':
            return base_cost * 1.2
        return base_cost

    @property
    def car_type(self):
        return self._car_type

    @property
    def seats(self):
        return self._seats

    def to_dict(self):
        """JSON serialization üçün"""
        return {
            'vehicle_id': self._vehicle_id,
            'brand': self._brand,
            'model': self._model,
            'daily_rate': self._daily_rate,
            'car_type': self._car_type,
            'seats': self._seats,
            'is_available': self._is_available
        }

    @classmethod
    def from_dict(cls, data: dict):
        """JSON deserialization üçün"""
        car = cls(
            vehicle_id=data['vehicle_id'],
            brand=data['brand'],
            model=data['model'],
            daily_rate=data['daily_rate'],
            car_type=data['car_type'],
            seats=data['seats']
        )
        car._is_available = data.get('is_available', True)
        return car

