from django.db import models

class Feedback(models.Model):
    comment = models.TexttField()
    created_at = model.DateTimeFIeld(auto_now_add=True)

    def___str___(self):
        return self.comment[:50]

# Create your models here.
