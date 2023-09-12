# Model inheritance

Model inheritance in Django works almost identically to the way normal class inheritance works in Python, but the basics at the beginning of the page should still be followed. That means the base class should subclass django.db.models.Model.

The only decision you have to make is whether you want the parent models to be models in their own right (with their own database tables), or if the parents are just holders of common information that will only be visible through the child models.

There are three styles of inheritance that are possible in Django.
- Abstract class inheritance
- Multitable class inheritance
- Proxy Model inheritance

Often, you will just want to use the parent class to hold information that you don’t want to have to type out for each child model. This class isn’t going to ever be used in isolation, so Abstract base classes are what you’re after.

If you’re subclassing an existing model (perhaps something from another application entirely) and want each model to have its own database table, Multi-table inheritance is the way to go.

Finally, if you only want to modify the Python-level behavior of a model, without changing the models fields in any way, you can use Proxy models.

## Abstract base classes Inheritance
Abstract base classes are useful when you want to put some common information into a number of other models. You write your base class and put abstract=True in the Meta class. This model will then not be used to create any database table. Instead, when it is used as a base class for other models, its fields will be added to those of the child class.

An example:
** Example 1:
```python
#abstract class inheritance test
class commonModel(models.Model):
    name=models.CharField(max_length=45)
    id=models.IntegerField(primary_key=True)
    address=models.TextField(max_length=50)
    class Meta:
        abstract=True
class studentInfoModel(commonModel):
    payment=models.IntegerField()
    section=models.CharField(max_length=45)
class teacherInfoModel(commonModel):
    subject=models.CharField(max_length=45)
    salary=models.IntegerField()

```
** Example 2:
```python
from django.db import models
class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True

class Student(CommonInfo):
    home_group = models.CharField(max_length=5)
```


The Student model will have three fields: name, age and home_group. The CommonInfo model cannot be used as a normal Django model, since it is an abstract base class. It does not generate a database table or have a manager, and cannot be instantiated or saved directly.

Fields inherited from abstract base classes can be overridden with another field or value, or be removed with None.

For many uses, this type of model inheritance will be exactly what you want. It provides a way to factor out common information at the Python level, while still only creating one database table per child model at the database level.

## Multi-table inheritance
The second type of model inheritance supported by Django is when each model in the hierarchy is a model all by itself. Each model corresponds to its own database table and can be queried and created individually. The inheritance relationship introduces links between the child model and each of its parents (via an automatically-created OneToOneField). For example:

Example 1:
```python
#multitable inheritance test 
class employeeModel(models.Model):
    name=models.CharField(max_length=45)
    id=models.IntegerField(primary_key=True)
    address=models.TextField(max_length=50)
    designation=models.CharField(max_length=44)
class managerModel(employeeModel):
    take_hire=models.BooleanField()
    take_interview=models.BooleanField()
    take_promotion=models.BooleanField()
```
Example 2:
```python
from django.db import models
class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)
class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)
```
All of the fields of Place will also be available in Restaurant, although the data will reside in a different database table. So these are both possible:

>>> Place.objects.filter(name="Bob's Cafe")
>>> Restaurant.objects.filter(name="Bob's Cafe")
If you have a Place that is also a Restaurant, you can get from the Place object to the Restaurant object by using the lowercase version of the model name:

>>> p = Place.objects.get(id=12)
# If p is a Restaurant object, this will give the child class:
>>> p.restaurant
<Restaurant: ...>
However, if p in the above example was not a Restaurant (it had been created directly as a Place object or was the parent of some other class), referring to p.restaurant would raise a Restaurant.DoesNotExist exception.

The automatically-created OneToOneField on Restaurant that links it to Place looks like this:
```python
place_ptr = models.OneToOneField(
    Place,
    on_delete=models.CASCADE,
    parent_link=True,
    primary_key=True,
)
```

You can override that field by declaring your own OneToOneField with parent_link=True on Restaurant.

Meta and multi-table inheritance¶
In the multi-table inheritance situation, it doesn’t make sense for a child class to inherit from its parent’s Meta class. All the Meta options have already been applied to the parent class and applying them again would normally only lead to contradictory behavior (this is in contrast with the abstract base class case, where the base class doesn’t exist in its own right).

So a child model does not have access to its parent’s Meta class. However, there are a few limited cases where the child inherits behavior from the parent: if the child does not specify an ordering attribute or a get_latest_by attribute, it will inherit these from its parent.

If the parent has an ordering and you don’t want the child to have any natural ordering, you can explicitly disable it:
```python
class ChildModel(ParentModel):
    # ...
    class Meta:
        # Remove parent's ordering effect
        ordering = []
```
Inheritance and reverse relations
Because multi-table inheritance uses an implicit OneToOneField to link the child and the parent, it’s possible to move from the parent down to the child, as in the above example. However, this uses up the name that is the default related_name value for ForeignKey and ManyToManyField relations. If you are putting those types of relations on a subclass of the parent model, you must specify the related_name attribute on each such field. If you forget, Django will raise a validation error.

For example, using the above Place class again, let’s create another subclass with a ManyToManyField:
```python
class Supplier(Place):
    customers = models.ManyToManyField(Place)
```

This results in the error:
Reverse query name for 'Supplier.customers' clashes with reverse query
name for 'Supplier.place_ptr'.

HINT: Add or change a related_name argument to the definition for
'Supplier.customers' or 'Supplier.place_ptr'.
Adding related_name to the customers field as follows would resolve the error: models.ManyToManyField(Place, related_name='provider').

Specifying the parent link field¶
As mentioned, Django will automatically create a OneToOneField linking your child class back to any non-abstract parent models. If you want to control the name of the attribute linking back to the parent, you can create your own OneToOneField and set parent_link=True to indicate that your field is the link back to the parent class.



# Proxy models inheritance

When using multi-table inheritance, a new database table is created for each subclass of a model. This is usually the desired behavior, since the subclass needs a place to store any additional data fields that are not present on the base class. Sometimes, however, you only want to change the Python behavior of a model – perhaps to change the default manager, or add a new method.

This is what proxy model inheritance is for: creating a proxy for the original model. You can create, delete and update instances of the proxy model and all the data will be saved as if you were using the original (non-proxied) model. The difference is that you can change things like the default model ordering or the default manager in the proxy, without having to alter the original.

Proxy models are declared like normal models. You tell Django that it’s a proxy model by setting the proxy attribute of the Meta class to True.

For example, suppose you want to add a method to the Person model. You can do it like this:

** Example 1:
```python
# proxy model inheritance test
class FriendModel(models.Model):
    name = models.CharField(max_length=45)
    section = models.CharField(max_length=34)
    attendance = models.BooleanField()
    hw = models.CharField(max_length=50)

class MeModel(FriendModel):
    class Meta:
        proxy = True
        # ordering = ['id']
```
** Example 2:
```python
from django.db import models
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class MyPerson(Person):
    class Meta:
        proxy = True

    def do_something(self):
        # ...
        pass
```
The MyPerson class operates on the same database table as its parent Person class. In particular, any new instances of Person will also be accessible through MyPerson, and vice-versa:
```python
>>> p = Person.objects.create(first_name="foobar")
>>> MyPerson.objects.get(first_name="foobar")
<MyPerson: foobar>
```

You could also use a proxy model to define a different default ordering on a model. You might not always want to order the Person model, but regularly order by the last_name attribute when you use the proxy:
```python
class OrderedPerson(Person):
    class Meta:
        ordering = ["last_name"]
        proxy = True
```

Now normal Person queries will be unordered and OrderedPerson queries will be ordered by last_name.

Proxy models inherit Meta attributes in the same way as regular models.

QuerySets still return the model that was requested¶
There is no way to have Django return, say, a MyPerson object whenever you query for Person objects. A queryset for Person objects will return those types of objects. The whole point of proxy objects is that code relying on the original Person will use those and your own code can use the extensions you included (that no other code is relying on anyway). It is not a way to replace the Person (or any other) model everywhere with something of your own creation.

Base class restrictions¶
A proxy model must inherit from exactly one non-abstract model class. You can’t inherit from multiple non-abstract models as the proxy model doesn’t provide any connection between the rows in the different database tables. A proxy model can inherit from any number of abstract model classes, providing they do not define any model fields. A proxy model may also inherit from any number of proxy models that share a common non-abstract parent class.

Proxy model managers¶
If you don’t specify any model managers on a proxy model, it inherits the managers from its model parents. If you define a manager on the proxy model, it will become the default, although any managers defined on the parent classes will still be available.

Continuing our example from above, you could change the default manager used when you query the Person model like this:

```python
from django.db import models
class NewManager(models.Manager):
    # ...
    pass
class MyPerson(Person):
    objects = NewManager()

    class Meta:
        proxy = True
```
If you wanted to add a new manager to the Proxy, without replacing the existing default, you can use the techniques described in the custom manager documentation: create a base class containing the new managers and inherit that after the primary base class:

# Create an abstract class for the new manager.
```python
class ExtraManagers(models.Model):
    secondary = NewManager()
    class Meta:
        abstract = True

class MyPerson(Person, ExtraManagers):
    class Meta:
        proxy = True
```
You probably won’t need to do this very often, but, when you do, it’s possible.

## Differences between proxy inheritance and unmanaged models
Proxy model inheritance might look fairly similar to creating an unmanaged model, using the managed attribute on a model’s Meta class.

With careful setting of Meta.db_table you could create an unmanaged model that shadows an existing model and adds Python methods to it. However, that would be very repetitive and fragile as you need to keep both copies synchronized if you make any changes.

On the other hand, proxy models are intended to behave exactly like the model they are proxying for. They are always in sync with the parent model since they directly inherit its fields and managers.

The general rules are:

If you are mirroring an existing model or database table and don’t want all the original database table columns, use Meta.managed=False. That option is normally useful for modeling database views and tables not under the control of Django.
If you are wanting to change the Python-only behavior of a model, but keep all the same fields as in the original, use Meta.proxy=True. This sets things up so that the proxy model is an exact copy of the storage structure of the original model when data is saved.


# Model Relationships in django 
## One-to-One Relationship
In this section, you define two Django models, `Person` and `Passport`, to represent a one-to-one relationship between a person and their passport. The `Person` model has fields for name, age, city, and email. The `Passport` model has a one-to-one relationship with `Person` using `OneToOneField`. This means that each passport is associated with exactly one person.
```python
#one to one relationship
class Person(models.Model):
    name = models.CharField(max_length=45)
    age = models.IntegerField()
    city=models.CharField(max_length=45)
    email=models.CharField(max_length=35)

    def __str__(self) -> str:
        return f"{self.name}"
class Passport(models.Model):
    person_user=models.OneToOneField(to="Person",on_delete=models.CASCADE,related_name='passport')
    passport_type=models.CharField(max_length=20)
    passport_number=models.IntegerField()
    page=models.IntegerField()
    validity=models.IntegerField()
    regional_office=models.CharField(max_length=45)
```


## One-to-Many Relationship
In this section, you define two Django models, `Student` and `Library`, to represent a one-to-many relationship between students and the library. The `Student` model has fields for name, ID, address, and section. The `Library` model has a foreign key relationship with `Student` using `ForeignKey`. This means that each library entry is associated with one student, but a student can have multiple library entries.
```python
# one to many relationship
class Student(models.Model):
    name = models.CharField(max_length=45)
    id = models.IntegerField(primary_key=True)
    address = models.TextField(max_length=50)
    section = models.CharField(max_length=45)
    def __str__(self) -> str:
        return f"{self.name}"
class Library(models.Model):
    # student_user=models.ForeignKey(to=Student, on_delete=models.SET_NULL,null=True)
    student_user=models.ForeignKey(to=Student, on_delete=models.CASCADE,related_name='student')
    book_name=models.CharField(max_length=45)
    who_take_book=models.IntegerField()
```


## Many-to-Many Relationship
In this section, you define two Django models, `Studentinfo` and `Teacherinfo`, to represent a many-to-many relationship between students and teachers. The `Studentinfo` model has fields for name, ID, address, and current class. The `Teacherinfo` model has a many-to-many relationship with `Studentinfo` using `ManyToManyField`. This means that each teacher can be associated with multiple students, and each student can be associated with multiple teachers.
```python

# many to many relationship
# many to many relationship
class Studentinfo(models.Model):
    name=models.CharField(max_length=45)
    id =models.IntegerField(primary_key=True)
    address=models.TextField(max_length=50)
    cur_class=models.CharField(max_length=20)
    def __str__(self):
        return self.name
    def teacher_list(self):
        return ",".join([str(i) for i in self.teacherinfo.all()])
class Teacherinfo(models.Model):
    student_user=models.ManyToManyField(to=Studentinfo,related_name="teacherinfo")
    name=models.CharField(max_length=45)
    address=models.TextField(max_length=50)
    subject=models.CharField(max_length=45)
    salary=models.IntegerField()
    phone=models.CharField(max_length=11)
    def __str__(self) -> str:
        return f"{self.name}"

    def student_list(self):
        return ",".join([str(i) for i in self.student_user.all()])

```
## Relationship Views
You have provided two Django views to demonstrate how to retrieve data from the defined relationships:

### show_data_one_to_one
This view is meant to demonstrate the retrieval of data in a one-to-one relationship. However, there's a minor issue in the code where you're trying to access `person.city`, which is incorrect. You should access it as `person.person_user.city` because `person` is related to `Passport`, and `city` is a field of the `Person` model.
```python
#one to one relationship
def show_data_one_to_one(request):
    passt=Passport.objects.get(passport_number=454578)
    person=passt.passport.all()
    print(person.city)
# many to many relations
def show_data(request):
    # one teacher has students
    teacher = Teacherinfo.objects.get(name="Hasan")
    students=teacher.student_user.all()
    for student in students:
        print(student.name)

    # one student has teachers
    student = Studentinfo.objects.get(name="Nihad")
    #teachers = student.teacherinfo_set.all()
    teachers = student.teacherinfo.all()
    for teacher in teachers:
        print(teacher.name)
    return render(request, 'show_data.html')

```





