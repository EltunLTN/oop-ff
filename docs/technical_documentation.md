# Car Rental Management System - Technical Documentation

## Sprint 1 - OOP Implementation

### Layihə Strukturu

```
car_rental_project/
├── src/
│   ├── models/          # Domain models
│   ├── repositories/    # Data access layer
│   ├── services/        # Business logic layer
│   └── main.py          # Entry point
├── tests/               # Unit tests
├── docs/                # Documentation
└── data/                # JSON data files
```

### OOP Prinsipləri

#### 1. Abstraction (Abstraksiya)
- **Vehicle** sinfi abstract base class kimi istifadə olunur
- Abstract method: `calculate_rental_cost()`

#### 2. Inheritance (Miras)
- **Car** sinfi **Vehicle** sinfindən miras alır
- `super()` metodu ilə parent class-in constructor-u çağırılır

#### 3. Encapsulation (Kapsulyasiya)
- Bütün atributlar private (`_` prefix ilə)
- Public access üçün `@property` decorator-ları istifadə olunur
- Setter metodları məhdudlaşdırılmış access üçün

#### 4. Polymorphism (Polimorfizm)
- `calculate_rental_cost()` metodu Car sinfində override edilir
- SUV tipli maşınlar üçün əlavə ödəniş hesablanır

#### 5. Composition (Kompozisiya)
- **Rental** sinfi **Car** və **Client** siniflərini kompozisiya kimi istifadə edir

### Siniflər

#### Vehicle (Abstract Base Class)
- `vehicle_id`: Maşının unikal ID-si
- `brand`: Marka
- `model`: Model
- `daily_rate`: Günlük icarə haqqı
- `is_available`: Mövcudluq statusu

#### Car (Concrete Class)
- Vehicle-dən miras alır
- `car_type`: Maşın tipi (SUV, Sedan, etc.)
- `seats`: Oturacaq sayı
- `calculate_rental_cost()`: İcarə haqqını hesablayır

#### Client
- `client_id`: Müştərinin unikal ID-si
- `name`: Ad
- `email`: Email
- `phone`: Telefon

#### Rental
- `rental_id`: İcarənin unikal ID-si
- `car`: Car obyekti (Composition)
- `client`: Client obyekti (Composition)
- `start_date`: Başlama tarixi
- `end_date`: Bitmə tarixi
- `total_cost`: Ümumi xərc
- `is_active`: Aktiv status

#### Repository
- CRUD əməliyyatları (Create, Read, Update, Delete)
- JSON fayllarla işləyir
- Logging dəstəyi

#### RentalService
- Business logic layer
- Car, Client və Rental-ları idarə edir
- Repository pattern istifadə edir

### Data Storage

- JSON fayllar istifadə olunur
- `data/cars.json`: Maşınlar
- `data/clients.json`: Müştərilər
- `data/rentals.json`: İcarələr

### Testing

- Unit testlər `tests/test_models.py` faylında
- unittest framework istifadə olunur
- Testlər inheritance, polymorphism, encapsulation prinsiplərini yoxlayır

### Logging

- Python logging modulu istifadə olunur
- INFO səviyyəsində loglar
- Əməliyyatların izlənməsi

