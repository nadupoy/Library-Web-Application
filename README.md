# Online Library Application - Django Project:
This repository documents the process and things I learnt building my first Django Project, a library web application.

## Introduction:
This documentation is written without a specific process but comprises of general notes of things I have learnt and implemented from the [documentation](https://docs.djangoproject.com/en/4.2/) on Django's [official website](https://www.djangoproject.com/).

## General notes:
- Determine your views (i.e. webpages) and link them to URLs that you have named appropriately.

- A view mapped onto a URL as used in the project:
```python
    def home_page(request):
        return HttpResponse("This is the Home page.")
```

```python
    urlpatterns = [
        ...
        path('', views.home_page, name='home'),
        ...
    ]
```

- When structuring the models, I decided to add a thumbnail field to the *Book* class.
```python
    class Book(models.Model):
        ...
        thumbnail = models.ImageField()
        ...
```
- Upon installing the [*Pillow module*](https://pillow.readthedocs.io/en/latest/) which is required when using *ImageField()*, I encountered the following error when running the *makemigrations* command in the Windows terminal:
```
    ModuleNotFoundError: No module named 'Pillow'
```
- I managed to find a solution that worked [here](https://stackoverflow.com/questions/23834663/pillow-installed-but-getting-no-module-named-pillow-when-importing), opting to use the following option provided:
```python
    ...
    import PIL
    ...
```

- I got an opportunity to use Django's database API to make queries, as explained in the official documentation in *2.4.4 Playing with the API*.

Using the Python shell to query the objects in the database gave the following output:
```
    ...
    >>> from library_app.models import Book, Author
    >>> Author.objects.all()
    <Queryset [<Author: Author object(1)>]>
    >>> Book.objects.all()
    <Queryset [<Book: Book object(1)>]>
    ...
```
This was also reflected in the admin site as shown below and is not an effecient way of representing the objects in the database.

![Author object representation in the admin site.](https://github.com/nadupoy/Library-Web-Application/blob/main/images_documentation/author_object.png?raw=true "Author object representation in the admin site.")

![Book object representation in the admin site.](https://github.com/nadupoy/Library-Web-Application/blob/main/images_documentation/book_object.png?raw=true "Book object representation in the admin site.")

I wanted the objects to be represented by their names in the database.

- The code below solved the above issue:
```python
    class Author(models.Model):
        first_name = models.CharField(max_length=50, null=True)
        last_name = models.CharField(max_length=50, null=True)

        @property
        def full_name(self):
            return f"{self.first_name} {self.last_name}"

        def __str__(self):
            return self.full_name
```
Sources that provided the above solution can be found [here](https://docs.djangoproject.com/en/4.2/topics/db/models/#model-methods) and [here](https://docs.djangoproject.com/en/4.2/ref/models/instances/#django.db.models.Model.__str__) in the [Django documentation](https://docs.djangoproject.com/en/4.2/).

Resultant change in the admin site is shown below:

![Author objects representation by value in the admin site.](https://github.com/nadupoy/Library-Web-Application/blob/main/images_documentation/author_object%2001.png?raw=true "Author objects representation by value in the admin site.")

- I also learnt how to hide the secret key by referencing it  externally before uploading to Github [here](https://dev.to/vladyslavnua/how-to-protect-your-django-secret-and-oauth-keys-53fl).

I encountered the following  error when installing the [python-dotenv package](https://pypi.org/project/python-dotenv/) which makes the above external referencing possible:

```
    Encountered error while generating package metadata.
```
I managed to find a solution for the above [here](https://sebhastian.com/error-metadata-generation-failed/).

- I learned to create a *requirements.txt* file [here](https://www.w3schools.com/django/django_deploy_requirements.php).