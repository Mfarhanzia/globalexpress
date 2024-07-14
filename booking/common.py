from uuid import uuid4

from django.db import models


class BaseModel(models.Model):
    """
    The abstract base class to be used by all models.
    """

    id = models.UUIDField(
        unique=True,
        default=uuid4,
        primary_key=True,
        editable=False,
    )

    created_on = models.DateTimeField(auto_now_add=True, editable=False)

    updated_on = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(
        "core.User",
        on_delete=models.PROTECT,
        db_column="created_by",
        related_name="%(class)s_created_by",
        editable=False,
    )

    updated_by = models.ForeignKey(
        "core.User",
        on_delete=models.PROTECT,
        db_column="updated_by",
        related_name="%(class)s_updated_by",
    )

    deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    updated_by_ip = models.CharField(max_length=20, null=True, blank=True)

    class Meta(object):
        """
        Meta class.
        """

        abstract = True

    def save_model(self, request, obj, form, change):
        obj.updated_by = request.user
        obj.created_by = request.user
        return super().save_model(request, obj, form, change)
