class LiteralMatcher:
    def __init__(self, key):
        self.literals = {}
        self.key = key
        self.cipher = Fernet(key)

    def add_literal(self, key, value, encrypted=False):
        if encrypted:
            value = self.cipher.decrypt(value.encode()).decode()
        self.literals[key] = value

    def sanitize(self, text):
        for key, value in self.literals.items():
            text = text.replace(key, value)
        return text