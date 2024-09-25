from abc import ABC, abstractclassmethod
from django.db import models

class AddBase:
    # @abstractclassmethod # depreceted
    def add(self):
        raise NotImplementedError("Subclass not implement add method")

class UpdateBase:
    def update(self):
        raise NotImplementedError("Subclass not implement update method")

class DeleteBase:
    def delete(self):
        raise NotImplementedError("Subclass not implement delete method")

class DetailBase:
    def detail(self):
        raise NotImplementedError("Subclass not implement detail method")

class ListBase:
    def list(self):
        raise NotImplementedError("Subclass not implement list method")


class CRUDBase(
    AddBase,
    UpdateBase,
    DeleteBase,
    DetailBase,
):
    pass
