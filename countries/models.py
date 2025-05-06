from django.db import models
from django.utils import timezone

class BaseModel(models.Model):
    created_at=models.DateTimeField(db_index=True, default=timezone.now)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True


class Country(BaseModel):
    name=models.CharField(max_length=255)
    official_name=models.CharField(max_length=255)
    capital=models.CharField(max_length=255)
    region=models.CharField(max_length=255)
    subregion=models.CharField(max_length=255)
    area=models.FloatField(null=True)
    population=models.IntegerField(null=True)
    flag_url=models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

