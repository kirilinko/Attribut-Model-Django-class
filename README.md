Models-Django

 
## Simple model django.  :floppy_disk: <a href="https://github.com/kirilinko/Models-Django/blob/main/class%20simple%20Django.py">Download</a> 
```python
from django.db import models

class Sujet(models.Model) :
    title = models.CharField(max_length = 200)
    description = models.TextField()
    last_modified = models.DateTimeField(auto_now_add = True)
    img = models.ImageField(upload_to = "images/")
 ```
* models.CharField() ::: Fields of type character with the value of ```max_length``` the number of character
* models.TextField()  ::: Fields of type text, to be used for fields whose maximum value is not known 
* models.DateTimeField() ::: Date fields with ```auto_now_add``` to specify the current time at the time of the update   
* models.ImageField()   ::: Fields of type image with ```upload_to to``` define the path where the images will be saved. <br/>
 #### PS: Before using models.ImageField() as it should be. You must install the <a href="https://pypi.org/project/Pillow/">pillow module</a>
 
 ## Many-to-one relational model django.
```python
from django.db import models
  
class Album(models.Model):
    title = models.CharField(max_length = 100)
    artist = models.CharField(max_length = 100)
  
class Song(models.Model):
    title = models.CharField(max_length = 100)
    album = models.ForeignKey(Album, on_delete = models.CASCADE)
 ```
 * models.ForeignKey() ::: Relational fields with ```Album``` the name of the model to which it is linked and ```on_delete = models.CASCADE``` to define the Many-to-one configuration
 
 ## Many-to-many relational model django.
```python
from django.db import models
  
class Author(models.Model):
    name = models.CharField(max_length = 100)
    desc = models.TextField(max_length = 300)
  
class Book(models.Model):
    title = models.CharField(max_length = 100)
    desc = models.TextField(max_length = 300)
    authors = models.ManyToManyField(Author)
 ```
 * models.ManyToManyField() ::: Relational fields with ```Album``` the name of the model to which it is linked

## One-to-one relational model django.
```python
from django.db import models
  
class Vehicle(models.Model):
    reg_no = models.IntegerField()
    owner = models.CharField(max_length = 100)
  
class Car(models.Model):
    vehicle = models.OneToOneField(Vehicle, 
          on_delete = models.CASCADE, primary_key = True)
    car_model = models.CharField(max_length = 100)
 ```
 * models.IntegerField() ::: Field of type integer
 * models.OneToOneField() ::: Relational fields with ```Vehicle``` the name of the model to which it is linked and ```on_delete = models.CASCADE, primary_key = True``` to define the Many-to-one configuration

## About on_delete

* on_delete = models.CASCADE – This is the default value. It automatically deletes all the related records when a record is deleted.(e.g. when an Album record is deleted all the Song records related to it will be deleted)
* on_delete = models.PROTECT – It blocks the deletion of a record having relation with other records.(e.g. any attempt to delete an Album record will be blocked)
* on_delete = models.SET_NULL – It assigns NULL to the relational field when a record is deleted, provided null = True is set.
* on_delete = models.SET_DEFAULT – It assigns default values to the relational field when a record is deleted, a default value has to be provided.
* on_delete = models.SET() – It can either take a default value as parameter, or a callable, the return value of which will be assigned to the field.
* on_delete = models.DO_NOTHING – Takes no action. Its a bad practice to use this value.

## :gift: Very useful bonus

### Basic model data types and fields list

* ```AutoField``` : It An IntegerField that automatically increments.
* ```BigAutoField```	: It is a 64-bit integer, much like an AutoField except that it is guaranteed to fit numbers from 1 to 9223372036854775807.
* ```BigIntegerField``` :	It is a 64-bit integer, much like an IntegerField except that it is guaranteed to fit numbers from -9223372036854775808 to 9223372036854775807.
* ```BinaryField``` :	A field to store raw binary data.
* ```BooleanField``` : 	A true/false field. The default form widget for this field is a CheckboxInput.
* ```CharField``` :	It is string filed for small to large-sized input
* ```DateField``` :	A date, represented in Python by a datetime.date instance
* ```DecimalField``` :	It is a fixed-precision decimal number, represented in Python by a Decimal instance.
* ```DurationField``` :	A field for storing periods of time.
* ```EmailField``` :	It is a CharField that checks that the value is a valid email address.
* ```FileField``` :	It is a file-upload field.
* ```FloatField```:	It is a floating-point number represented in Python by a float instance.
* ```ImageField``` :	It inherits all attributes and methods from FileField, but also validates that the uploaded object is a valid image.
* ```IntegerField```	: It is an integer field. Values from -2147483648 to 2147483647 are safe in all databases supported by Django.
* ```NullBooleanField``` :	Like a BooleanField, but allows NULL as one of the options.
* ```PositiveIntegerField```	: Like an IntegerField, but must be either positive or zero (0).
* ```PositiveSmallIntegerField```	: Like a PositiveIntegerField, but only allows values under a certain (database-dependent) point.
* ```SlugField```	: Slug is a newspaper term. A slug is a short label for something, containing only letters, numbers, underscores or hyphens. They’re generally used in URLs.
* ```SmallIntegerField``` :	It is like an IntegerField, but only allows values under a certain (database-dependent) point.
* ```TextField```	: A large text field. The default form widget for this field is a Textarea.
* ```TimeField``` : 	A time, represented in Python by a datetime.time instance.
* ```URLField```	: A CharField for a URL, validated by URLValidator.

### Field Options
* ```Null```	: If True, Django will store empty values as NULL in the database. Default is False.
* ```Blank``` :	If True, the field is allowed to be blank. Default is False.
* ```db_column```	: The name of the database column to use for this field. If this isn’t given, Django will use the field’s name. 
* ```Default```	: The default value for the field. This can be a value or a callable object. If callable it will be called every time a new object is created.  
* ```help_text``` :	Extra “help” text to be displayed with the form widget. It’s useful for documentation even if your field isn’t used on a form. 
* ```primary_key``` :	If True, this field is the primary key for the model.
* ```editable``` :	If False, the field will not be displayed in the admin or any other ModelForm. They are also skipped during model validation. Default is True. 
* ```error_messages``` :	The error_messages argument lets you override the default messages that the field will raise. Pass in a dictionary with keys matching the error messages you want to override. 
* ```help_text```	: Extra “help” text to be displayed with the form widget. It’s useful for documentation even if your field isn’t used on a form. 
* ```verbose_name``` :	A human-readable name for the field. If the verbose name isn’t given, Django will automatically create it using the field’s attribute name, converting underscores to spaces. 
* ```validators```	: A list of validators to run for this field. See the validators documentation for more information. 
* ```Unique```	: If True, this field must be unique throughout the table. 
