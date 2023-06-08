class Book:
    __code = 100
    def __init__(self, name, writer, qty, edition='') -> None:
        self.name = name
        self.writer = writer
        self.quantity = qty
        self.edition = edition
        self.unique_code = self.__class__.unique_code_generator()

    @classmethod
    def unique_code_generator(cls):
        cls.__code += 1
        return cls.__code
        
    def __repr__(self) -> str:
        return f'Code: {self.unique_code} \tName: {self.name}\t\tWriter: {self.writer}'