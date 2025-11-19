from datetime import datetime
from typing import Optional
from .car import Car
from .client import Client


class Rental:
    """Rental class - Composition pattern"""

    def __init__(self, rental_id: str, car: Car, client: Client,
                 start_date: datetime, end_date: Optional[datetime] = None):
        self._rental_id = rental_id
        self._car = car  # Composition
        self._client = client  # Composition
        self._start_date = start_date
        self._end_date = end_date
        self._total_cost = 0.0
        self._is_active = True

    @property
    def rental_id(self):
        return self._rental_id

    @property
    def car(self):
        return self._car

    @property
    def client(self):
        return self._client

    @property
    def start_date(self):
        return self._start_date

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value: datetime):
        self._end_date = value

    @property
    def total_cost(self):
        return self._total_cost

    @property
    def is_active(self):
        return self._is_active

    def calculate_total_cost(self) -> float:
        """Calculate rental cost based on days"""
        if self._end_date:
            days = (self._end_date - self._start_date).days
            if days <= 0:
                days = 1
        else:
            # If not returned yet, calculate from start to now
            days = (datetime.now() - self._start_date).days
            if days <= 0:
                days = 1

        self._total_cost = self._car.calculate_rental_cost(days)
        return self._total_cost

    def complete_rental(self, end_date: Optional[datetime] = None):
        """Complete the rental and calculate final cost"""
        if end_date:
            self._end_date = end_date
        else:
            self._end_date = datetime.now()
        self._total_cost = self.calculate_total_cost()
        self._is_active = False
        self._car.is_available = True

    def to_dict(self):
        """JSON serialization üçün"""
        return {
            'rental_id': self._rental_id,
            'car': self._car.to_dict(),
            'client': self._client.to_dict(),
            'start_date': self._start_date.isoformat(),
            'end_date': self._end_date.isoformat() if self._end_date else None,
            'total_cost': self._total_cost,
            'is_active': self._is_active
        }

    @classmethod
    def from_dict(cls, data: dict):
        """JSON deserialization üçün"""
        from datetime import datetime
        car = Car.from_dict(data['car'])
        client = Client.from_dict(data['client'])
        rental = cls(
            rental_id=data['rental_id'],
            car=car,
            client=client,
            start_date=datetime.fromisoformat(data['start_date']),
            end_date=datetime.fromisoformat(data['end_date']) if data.get('end_date') else None
        )
        rental._total_cost = data.get('total_cost', 0.0)
        rental._is_active = data.get('is_active', True)
        return rental

