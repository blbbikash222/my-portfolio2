
from django.contrib import admin
from .models import (
    SiteSettings,
    Service,
    Destination,
    Experience,
    Testimonial,
    SuccessStory,
    Enquiry,
)


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "brand", "updated_at")
    search_fields = ("name", "position", "brand")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "order")
    list_filter = ("is_active",)
    search_fields = ("title", "description")
    list_editable = ("is_active", "order")


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active", "order")
    list_filter = ("is_active",)
    search_fields = ("name", "description")
    list_editable = ("is_active", "order")


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        "position",
        "organization",
        "start_year",
        "end_year",
        "is_current",
    )
    list_filter = ("is_current",)
    search_fields = ("position", "organization")


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("student_name", "destination", "is_active", "created_at")
    list_filter = ("is_active", "destination")
    search_fields = ("student_name", "message")
    readonly_fields = ("created_at",)


@admin.register(SuccessStory)
class SuccessStoryAdmin(admin.ModelAdmin):
    list_display = (
        "student_name",
        "destination",
        "university",
        "is_active",
        "created_at",
    )
    list_filter = ("is_active", "destination")
    search_fields = ("student_name", "university", "story")
    readonly_fields = ("created_at",)


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "phone",
        "interested_destination",
        "is_read",
        "created_at",
    )
    list_filter = ("is_read", "interested_destination")
    search_fields = ("name", "email", "phone", "message")
    readonly_fields = ("created_at",)
