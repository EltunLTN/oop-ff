# Car Rental Management System - User Guide

## Sprint 1 - İstifadə Təlimatı

### Sistem Tələbləri

- Python 3.7 və ya daha yüksək versiya
- Standard Python library (xarici paketlər lazım deyil)

### Quraşdırma

1. Layihəni klonlayın və ya yükləyin
2. Terminal-də layihə qovluğuna keçin:
   ```bash
   cd "Car Rental Managment System"
   ```

### İstifadə

#### Sistemin işə salınması

```bash
python src/main.py
```

Bu əmr nümunə məlumatlar yaradacaq və sistemin işləməsini nümayiş etdirəcək.

#### Kodda istifadə

```python
from src.models.car import Car
from src.models.client import Client
from src.services.rental_service import RentalService
from src.repositories.repository import Repository

# Repository-ləri yaradın
cars_repo = Repository('data/cars.json')
clients_repo = Repository('data/clients.json')
rentals_repo = Repository('data/rentals.json')

# Service yaradın
service = RentalService(cars_repo, clients_repo, rentals_repo)

# Maşın əlavə edin
car = Car('C001', 'Toyota', 'Camry', 50.0, 'Sedan', 5)
service.add_car(car)

# Müştəri əlavə edin
client = Client('CL001', 'John Doe', 'john@example.com', '+1234567890')
service.add_client(client)

# İcarə yaradın
rental = service.create_rental('R001', 'C001', 'CL001')

# Mövcud maşınları göstərin
available_cars = service.get_available_cars()
for car in available_cars:
    print(f"{car.brand} {car.model} - ${car.daily_rate}/day")
```

### Testlərin işə salınması

```bash
python -m unittest tests.test_models
```

və ya

```bash
python tests/test_models.py
```

### Məlumat Faylları

Sistem avtomatik olaraq `data/` qovluğunda aşağıdakı JSON faylları yaradacaq:

- `cars.json`: Maşın məlumatları
- `clients.json`: Müştəri məlumatları
- `rentals.json`: İcarə məlumatları

### Əsas Funksiyalar

#### Maşınlar
- Maşın əlavə etmək
- Mövcud maşınları görmək
- Maşın məlumatlarını oxumaq

#### Müştərilər
- Müştəri əlavə etmək
- Müştəri məlumatlarını oxumaq

#### İcarələr
- Yeni icarə yaratmaq
- Aktiv icarələri görmək
- İcarəni tamamlamaq

### Növbəti Sprintlər

Sprint 1-də əsas OOP strukturu və CRUD əməliyyatları həyata keçirilmişdir. Növbəti sprintlərə aşağıdakı funksiyalar əlavə oluna bilər:

- İstifadəçi interfeysi (CLI və ya GUI)
- Tarixçə və hesabatlar
- Ödəniş sistemi
- Maşın və müştəri axtarışı
- Validasiya və xəta idarəetməsi

