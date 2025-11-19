# Car Rental Management System

Python OOP layihəsi - Car Rental Management Sistemi

## Sprint 1 - OOP Implementation

Bu layihə OOP (Object-Oriented Programming) prinsiplərinin praktiki tətbiqini nümayiş etdirir.

### OOP Prinsipləri

- ✅ **Abstraction**: Abstract base class (Vehicle)
- ✅ **Inheritance**: Car sinfi Vehicle-dən miras alır
- ✅ **Encapsulation**: Private atributlar və property metodları
- ✅ **Polymorphism**: calculate_rental_cost() metodunun override edilməsi
- ✅ **Composition**: Rental sinfində Car və Client kompozisiya

### Layihə Strukturu

```
car_rental_project/
├── src/
│   ├── models/          # Domain models
│   │   ├── base.py      # Abstract Vehicle class
│   │   ├── car.py       # Car class
│   │   ├── client.py    # Client class
│   │   └── rental.py    # Rental class
│   ├── repositories/    # Data access layer
│   │   └── repository.py
│   ├── services/        # Business logic
│   │   └── rental_service.py
│   └── main.py          # Entry point
├── tests/               # Unit tests
│   └── test_models.py
├── docs/                # Documentation
│   ├── technical_documentation.md
│   └── user_guide.md
└── data/                # JSON data files
```

### Quraşdırma

1. Python 3.7+ tələb olunur
2. Xarici paketlər lazım deyil (yalnız standard library)

### İstifadə

#### Sistemin işə salınması:

```bash
python run.py
```

və ya

```bash
python src/main.py
```

#### Testlərin işə salınması:

```bash
python -m unittest tests.test_models
```

### Əsas Funksiyalar

- ✅ Maşın idarəetməsi (CRUD)
- ✅ Müştəri idarəetməsi (CRUD)
- ✅ İcarə əməliyyatları
- ✅ JSON fayllarla data storage
- ✅ Logging dəstəyi
- ✅ Unit testlər

### Növbəti Addımlar

Sprint 1 tamamlandı! Növbəti sprintlərə aşağıdakı funksiyalar əlavə oluna bilər:

- CLI interfeysi
- GUI (Tkinter və ya PyQt)
- Database inteqrasiyası (SQLite, PostgreSQL)
- Hesabatlar və analitika
- Ödəniş sistemi
- Email bildirişləri

### Müəllif

Car Rental Management System - Sprint 1

### Lisenziya

Bu layihə təhsil məqsədi ilə yaradılmışdır.

