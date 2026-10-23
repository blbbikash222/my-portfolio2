
from django.db import models


class SiteSettings(models.Model):
    name = models.CharField(
        max_length=150,
        default="Bikash Belbase"
    )
    position = models.CharField(
        max_length=150,
        default="Education Consultant"
    )
    brand = models.CharField(
        max_length=150,
        default="Oasis Education Group"
    )
    about = models.TextField(blank=True)
    experience = models.TextField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=255, blank=True)
    whatsapp = models.CharField(max_length=30, blank=True)

    # Upload profile image through Django Admin
    profile_image = models.ImageField(
        upload_to="profile/",
        blank=True,
        null=True
    )

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return self.name


class Service(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    icon = models.CharField(max_length=50, blank=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "title"]

    def __str__(self):
        return self.title


class Destination(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return self.name


class Experience(models.Model):
    position = models.CharField(max_length=150)
    organization = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    start_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField(
        null=True,
        blank=True
    )
    is_current = models.BooleanField(default=False)

    class Meta:
        ordering = ["-start_year"]

    def __str__(self):
        return f"{self.position} - {self.organization}"


class Testimonial(models.Model):
    student_name = models.CharField(max_length=150)
    destination = models.CharField(max_length=100, blank=True)
    message = models.TextField()
    photo_url = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.student_name


class SuccessStory(models.Model):
    student_name = models.CharField(max_length=150)
    destination = models.CharField(max_length=100)
    university = models.CharField(max_length=200, blank=True)
    story = models.TextField()
    image_url = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.student_name} - {self.destination}"


class Enquiry(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    interested_destination = models.CharField(
        max_length=100,
        blank=True
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.email}"
