from django.db import models
import uuid as uuid_lib

# Create your models here.

class Table(models.Model):
    uuid = models.UUIDField(
            primary_key=True,
            db_index=True,
            default=uuid_lib.uuid4,
            editable=False)
    date = models.DateTimeField()
    text = models.TextField()

