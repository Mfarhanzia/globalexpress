from cities_light.models import City, Country
from django.contrib.auth.models import AbstractUser, Group
from django.core.validators import EmailValidator
from django.db import models
from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _
from PIL import Image

from booking.common import BaseModel
from common.utils import get_upload_path

# Create your models here.


class GenderChoice(TextChoices):
    MALE = "male", "Male"
    FEMALE = "female", "Female"
    OTHER = "other", "Other"


class User(BaseModel):
    username = models.TextField(
        _("username"),
        unique=True,
        validators=[EmailValidator],
        help_text=_("Required. Should be a syntactically valid email."),
        error_messages={"unique": _("A user with that username already exists.")},
    )
    email = models.EmailField(unique=True, validators=[EmailValidator])
    profile_image = models.ImageField(upload_to=get_upload_path, blank=True, null=True)

    phone = models.CharField(max_length=30)

    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    post_code = models.CharField(max_length=10)
    address = models.CharField(max_length=255)

    is_verified = models.BooleanField(default=True)

    middle_name = models.CharField(max_length=150, blank=True, null=True)

    father_name = models.CharField(max_length=150, blank=True, null=True)

    gender = models.CharField(max_length=20, choices=GenderChoice.choices, null=True)

    birth_date = models.DateField(null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.profile_image:
            try:
                img = Image.open(self.profile_image.path)
                if img.height > 300 or img.width > 300:
                    output_size = (300, 300)
                    img.thumbnail(output_size)
                    img.save(self.profile_image.path)
            except Exception as e:
                pass  # TODO: what should be done here
