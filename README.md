django-model-mixins
===================

Simple helper to extend django models using mixins

When you mixin a django model into another one, it is probably behaving not how you want it to. This is caused by django's metaclass magic.

This package provides a single class ```ModelMixin``` that you can use as the base for mixins, that provide additional fields to the object the class get's mixed in to.

```ModelMixin``` is a direct subclass of ```object``` and therefore it's subclass is not going to be an own table.


## Example

### Model

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

### SQL Output

```sql
BEGIN;
CREATE TABLE "cars_car" (
    "id" integer NOT NULL PRIMARY KEY,
    "model" varchar(200) NOT NULL,
    "color" varchar(200) NOT NULL
)
;
CREATE TABLE "cars_person_cars" (
    "id" integer NOT NULL PRIMARY KEY,
    "person_id" integer NOT NULL,
    "car_id" integer NOT NULL REFERENCES "cars_car" ("id"),
    UNIQUE ("person_id", "car_id")
)
;
CREATE TABLE "cars_person" (
    "id" integer NOT NULL PRIMARY KEY,
    "firstname" varchar(200) NOT NULL,
    "lastname" varchar(200) NOT NULL
)
;
COMMIT;
```