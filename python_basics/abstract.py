from abc import ABC, abstractproperty


class Animal(ABC):
    @abstractproperty
    def talk():
        pass


class People(Animal):
    def __init__(self):
        self._talk = "hello"

    @property
    def talk(self):
        return self._talk


if __name__ == "__main__":
    colin = People()
    print(colin.talk)
