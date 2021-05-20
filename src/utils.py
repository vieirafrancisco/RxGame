class Request:
    def __init__(self, method, data=None):
        self.method = method
        self.data = data

    def encode(self):
        return f"{self.method} {self.data}".encode()

    @classmethod
    def decode(cls, string):
        method, data = string.decode().split(" ")
        return cls(method=method, data=data)

    @property
    def prep_data(self):
        if self.method == "SEND":
            return self.data.split("&")
        if self.method == "GET":
            output = []
            for data in self.data.split("%"):
                output.append(data.split("&"))
            return output
        raise Exception("Error")


class Response:
    def __init__(self, type, data=None):
        self.type = type
        self.data = data

    def encode(self):
        return f"{self.type} {self.data}".encode()

    @classmethod
    def decode(cls, string):
        type, data = string.decode().split(" ")
        return cls(type=type, data=data)

    @staticmethod
    def prep_data(string):
        for data in string.split(" "):
            if len(data) > 0:
                id, px, py = data.split("&")
            yield id, int(px), int(py)
