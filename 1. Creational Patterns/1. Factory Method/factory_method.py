from __future__ import annotations
from abc import ABC, abstractmethod

# Фабричный метод позволяет подклассам суперкласса изменять тип создаваемых объектов,
# при помощи создания и указания общего интерфейса объектов в суперклассе
# и переопределения абстрактного метода создания объектов в подклассе.

# Суперкласс с фабричным методом
class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self) -> str:
        product = self.factory_method()
        result = f"Creator: The same creator's code has just worked with {product.operation()}"

        return result

# Подкласс1 с переопределенным фабричным методом
class ConcreteCreator1(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct1()

# Подкласс2 с переопределенным фабричным методом
class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct2()

# Общий интерфейс объектов
class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

# Реализация интерфейса в классе объектов 1
class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"

# Реализация интерфейса в классе объектов 2
class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"

# Клиентская функция
def client_code(creator: Creator) -> None:
    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}", end="")

# запуск программы
if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Launched with the ConcreteCreator2.")
    client_code(ConcreteCreator2())

'''Output:
App: Launched with the ConcreteCreator1.
Client: I'm not aware of the creator's class, but it still works.
Creator: The same creator's code has just worked with {Result of the ConcreteProduct1}

App: Launched with the ConcreteCreator2.
Client: I'm not aware of the creator's class, but it still works.
Creator: The same creator's code has just worked with {Result of the ConcreteProduct2}
'''


