from tortoise.models import Model
from tortoise import fields
from datetime import date

class FeatureRequest(Model):
    id: int = fields.IntField(primary_key=True)
    title: str = fields.CharField(max_length=255)
    description: str = fields.TextField()
    created_at: date = fields.DateField(default=date.today)
    rating = fields.ForeignKeyField(
        'models.Rating',
        related_name="feature_request",
    )

    def __str__(self) -> str:
        return self.title

class Rating(Model):
    rating: int = fields.IntField(default=0)
