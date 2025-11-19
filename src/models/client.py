class Client:
    """Client class - Single Responsibility Principle"""

    def __init__(self, client_id: str, name: str, email: str,
                 phone: str):
        self._client_id = client_id
        self._name = name
        self._email = email
        self._phone = phone

    @property
    def client_id(self):
        return self._client_id

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    @property
    def phone(self):
        return self._phone

    def to_dict(self):
        return {
            'client_id': self._client_id,
            'name': self._name,
            'email': self._email,
            'phone': self._phone
        }

    @classmethod
    def from_dict(cls, data: dict):
        """JSON deserialization üçün"""
        return cls(
            client_id=data['client_id'],
            name=data['name'],
            email=data['email'],
            phone=data['phone']
        )

