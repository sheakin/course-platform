from django.db import models


class AccessRequirement(models.TextChoices):
    ANYONE = "any","AnyOne"
    EMAIL_REQUIRED = "email","Email Required"

class PublishStatus(models.TextChoices):
    PUBLISHED = "publish", "published"      # pub is stored in the database ,published as user see,PUBLISHED use in the code.
    DRAFT = "draf", "Draft"
    COMING_SOON = "soon", "Coming Soon"

def handle_upload(instance, filename):
    return f"{filename}"

class courses(models.Model):            #models have hidenn field called id
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=handle_upload,blank=True,null=True)
    access = models.CharField(
        max_length=14,
        choices=AccessRequirement.choices,
        default=AccessRequirement.EMAIL_REQUIRED
        )

    status = models.CharField(
        max_length=10,
        choices=PublishStatus.choices,
        default=PublishStatus.DRAFT
        )
    @property
    def is_published(self):
        return self.status == PublishStatus.PUBLISHED