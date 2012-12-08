"""
Mixin support for django models
"""
from django.db import models
from django.db.models.signals import class_prepared
from django.dispatch import receiver
from django.db.models.fields import Field


class ModelMixin(object):
    """
    Base class for model mixins
    """

    @classmethod
    def model_mixin(cls):
        """
        Adds the fields of the class to the all classes that mix it in
        """
        fields = {}

        for (name, attr) in cls.__dict__.items():
            if isinstance(attr, models.Field):
                fields[name] = attr

        for fieldname in fields.keys():
            delattr(cls, fieldname)

        for subclass in cls.__subclasses__():
            assert issubclass(subclass, models.Model)
            for (fieldname, field) in fields.items():
                field.contribute_to_class(subclass, fieldname)



@receiver(class_prepared)
def mixin(sender, **kwargs):
    for base in sender.__bases__:
        if issubclass(base, ModelMixin):
            base.model_mixin()
