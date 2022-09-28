from django.db import models


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=25, unique=True, null=False)

    def __str__(self):
        return self.name


class Note(models.Model):
    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=150, null=False)
    done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, through='NoteToTag')

    def __str__(self):
        return self.name


class NoteToTag(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
