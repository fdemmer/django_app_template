# -*- coding: utf-8 -*-
{{ unicode_literals }}from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible, force_text
from django.utils.translation import ugettext_lazy as _


# Create your models here.
# @python_2_unicode_compatible
# class MyModel(models.Model):
#     """
#
#     """
#     class Meta:
#         verbose_name = _('')
#         verbose_name_plural = _('')
#         ordering = ()
#
#     def __str__(self):
#         return force_text(self.pk)
#
#     def get_absolute_url(self):
#         return reverse('blog:myview', args=(self.pk,))
