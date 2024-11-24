from django.db import models


class AccessRequirement(models.Model):
    ANYONE = "any","Any One"
    EMAIL_REQUIRED = "email_required","Email Required"

class PublishStatus(models.TextChoices):
    PUBLISHED = "publish", "published"      # pub is stored in the database ,published as user see,PUBLISHED use in the code.
    DRAFT = "draf", "Draft"
    COMING_SOON = "soon", "Coming Soon"

class courses(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    # image
    access = models.CharField(
        max_length=10,
        choices=AccessRequirement.choices,
        default=AccessRequirement.DRAFT
        )

    status = models.CharField(
        max_length=10,
        choices=PublishStatus.choices,
        default=PublishStatus.DRAFT
        )
    @property
    def is_published(self):
        return self.status == PublishStatus.PUBLISHED