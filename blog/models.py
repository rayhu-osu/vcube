from django.db import models


class Post (models.Model):  # a table, every variable is a column


    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()  # date and time

    # Django will also create an id for each post object

    def __str__(self):  # str(Post) will call __str__ method
        # https://stackoverflow.com/questions/12448175/confused-about-str-in-python
        return self.title
