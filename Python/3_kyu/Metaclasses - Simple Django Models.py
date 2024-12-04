'''
[ Metaclasses - Simple Django Models ]

Django is a famous back-end framework written in Python.
It has a vast list of features including the creation of database tables through "models".

You can see an example of such model below:
class Person(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()

Apart from creating a table it can perform validation, generate HTML forms, and so on.
This is possible thanks to metaclasses.
Normally there are better solutions than using metaclasses, but they can be of great help in creating powerful framework interfaces.
This goal of this kata is to learn and understand how such frameworks works.

Your task is to implement a class Model and classes for its fields to support functionality like in the following example:
class User(Model):
    first_name = CharField(max_length=30)
    last_name = CharField(max_length=50)
    email = EmailField()
    is_verified = BooleanField(default=False)
    date_joined = DateTimeField(auto_now=True)
    age = IntegerField(min_value=5, max_value=120, blank=True)

user1 = User(first_name='Liam', last_name='Smith', email='liam@example.com')
user1.validate()

print(user1.date_joined)  # prints date and time when the instance was created
print(user1.is_verified)  # prints False (default value)

user1.age = 256
user1.validate()  # raises ValidationError - age is out of range

user2 = User()
user2.validate()  # raises ValidationError - first three fields are missing and mandatory
The classes which inherit from Model should:

support creation of fields using class-attribute syntax
have a validate method which checks whether all fields are valid
The field types you should implement are described below. Each of them also has parameters blank (default False), which determines whether None is allowed as a value, and default (default None) which determines the value to be used if nothing was provided at instantiation time of the Model.

CharField - a string with min_length (default 0) and max_length (default None) parameters, both inclusive if defined
IntegerField - an integer with min_value (default None) and max_value (default None) parameters, both inclusive if defined
BooleanField - a boolean
DateTimeField - a datetime with an extra parameter auto_now (default False). If auto_now is True and no default value has been provided, the current datetime should be used automatically at Model instantion time.
EmailField - a string in the format of address@subdomain.domain where address, subdomain, and domain are sequences of alphabetical characters with min_length (default 0) and max_length (default None) parameters
Each field type should have its own validate method which checks whether the provided value has the correct type and satisfies the length/value constraints.
'''



# TODO: Заметки
## Автор: Дуплей Максим Игоревич / Dupley Maxim Igorevich
## Дата: 02.12.2024
