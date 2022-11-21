# Attribut-Model-Django-class
Classe Attribute Model Django per la creazione di un database relazionale

from django.db import models
 
## Simple model django.  :floppy_disk: <a href="https://github.com/kirilinko/Models-Django/blob/main/class%20simple%20Django.py">Download</a> 
```python
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
