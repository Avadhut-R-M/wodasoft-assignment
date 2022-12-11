from django.db import models

# Create your models here.


class AccountOne(models.Model):
    parent = models.ForeignKey(
        'AccountOne',
        null=True,
        blank=True,
        related_name='child',
        on_delete=models.DO_NOTHING
    )
    left_child = models.ForeignKey(
        'AccountOne',
        null=True,
        blank=True,
        related_name='left_parent',
        on_delete=models.DO_NOTHING
    )
    right_child = models.ForeignKey(
        'AccountOne',
        null=True,
        blank=True,
        related_name='right_parent',
        on_delete=models.DO_NOTHING
    )
    email = models.EmailField(
        max_length=50,
        null=True,
        blank=True,
        unique=True
    )
    is_active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.email


class AccountTwo(models.Model):
    left_child = models.ForeignKey(
        'AccountTwo',
        null=True,
        blank=True,
        related_name='left_parent',
        on_delete=models.DO_NOTHING
    )
    right_child = models.ForeignKey(
        'AccountTwo',
        null=True,
        blank=True,
        related_name='right_parent',
        on_delete=models.DO_NOTHING
    )
    email = models.EmailField(
        max_length=50,
        null=True,
        blank=True,
        unique=True
    )
    is_active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.email


class AccountThree(models.Model):
    parent = models.ForeignKey(
        'AccountThree',
        null=True,
        blank=True,
        related_name='child',
        on_delete=models.DO_NOTHING
    )
    email = models.EmailField(
        max_length=50,
        null=True,
        blank=True,
        unique=True
    )
    is_active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.email
