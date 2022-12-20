from django.core import validators
from django.db import models


class Profile(models.Model):
    MIN_USERNAME_LEN = 2
    MAX_USERNAME_LEN = 10
    MIN_USERNAME_LEN_MESSAGE = "The username must be a minimum of 2 chars"
    MIN_AGE = 18
    MAX_PASSWORD_LEN = 30
    MAX_FIRST_NAME_LEN = 30
    MAX_LAST_NAME_LEN = 30

    username = models.CharField(
        max_length=MAX_USERNAME_LEN,
        validators=(
            [validators.MinLengthValidator(MIN_USERNAME_LEN, message=MIN_USERNAME_LEN_MESSAGE)]
        ),
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        null=False,
        blank=False,
        validators=(
            (validators.MinValueValidator(MIN_AGE),)
        )
    )

    password = models.CharField(
        max_length=MAX_PASSWORD_LEN,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LEN,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LEN,
        blank=True,
        null=True,
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
    )


class Car(models.Model):
    MAX_LEN_CAR_TYPE = 10
    CAR_TYPE_CHOICES = [
        "Sports Car",
        "Pickup",
        "Crossover",
        "Minibus",
        "Other",
    ]

    MAX_LEN_MODEL = 20
    MIN_LEN_MODEL = 2

    MIN_YEAR = 1980
    MAX_YEAR = 2049
    YEAR_RANGE_MESSAGE = "Year must be between 1980 and 2049"

    MIN_PRICE = 1.0

    type = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LEN_CAR_TYPE,
        choices=[(x, x) for x in CAR_TYPE_CHOICES]
    )

    model = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LEN_MODEL,
        validators=(validators.MinLengthValidator(MIN_LEN_MODEL),),
    )

    year = models.IntegerField(
        null=False,
        blank=False,
        validators=(
            validators.MinValueValidator(MIN_YEAR, message=YEAR_RANGE_MESSAGE),
            validators.MaxValueValidator(MAX_YEAR, message=YEAR_RANGE_MESSAGE),
        )
    )

    car_image_url = models.URLField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=(validators.MinValueValidator(MIN_PRICE),)
    )

