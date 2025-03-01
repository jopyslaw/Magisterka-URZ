from django.contrib.auth.hashers import BasePasswordHasher

class PlaintextPasswordHasher(BasePasswordHasher):
    algorithm = "plaintext"

    def encode(self, password, salt):
        return f"{self.algorithm}${password}"

    def decode(self, encoded):
        return encoded.split("$", 1)[1]

    def verify(self, password, encoded):
        return password == self.decode(encoded)

    def must_update(self, encoded):
        return False
    
    def safe_summary(self, encoded):
        return {
            'algorithm': self.algorithm,
            "password": self.decode(encoded)
        }