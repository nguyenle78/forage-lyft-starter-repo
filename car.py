from abc import ABC, abstractmethod


class Car:
    @abstractmethod
    def needs_service(self):
        pass
