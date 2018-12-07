from django.db import models
from django.contrib.auth import models as auth_models


class User(auth_models.User):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_cr = models.BooleanField(default=False)
    roll_no = models.CharField(max_length=10)

    def __str__(self):
        return self.roll_no

