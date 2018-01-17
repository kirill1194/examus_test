from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from mini_utils.file_names import file_name_generator


def image_file_name_generator(instance, filename):
    return file_name_generator('menu_images', instance, filename)


class MenuItem(models.Model):
    name = models.CharField(_("name"), max_length=255, blank=False, null=False)
    price = models.DecimalField(_("price"), max_digits=6, decimal_places=2, null=False,
                                validators=[MinValueValidator(0)])
    nutrition_value = models.IntegerField(_("nutrition value"), blank=False, null=False,
                                          validators=[MinValueValidator(0)])
    picture = models.ImageField(_("picture"), blank=False, null=False, upload_to=image_file_name_generator)
