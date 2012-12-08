django-model-mixins
===================

Simple helper to extend django models using mixins

When you mixin a django model into another one, it probably behaving not how you want, because of django's metaclass magic.

## Example

```python
from modelmixins import ModelMixin

class Car(models.Model):
    model = models.CharField(max_length=200)
    color = models.CharField(max_length=200)

class CarOwner(ModelMixin):
    cars = models.ManyToManyField(Car)


class Person(models.Model, CarOwner):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
```