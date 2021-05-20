class Auth:
    def __init__(self):
        pass

    def authenticate(self, username: str, password: str) -> bool:
        pass

    def register(self, username: str, password: str, confirm_password: str) -> None:
        pass

    def login(self, username: str, password: str) -> str:
        pass
