from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
import random, string



class Category(models.Model):
    name = models.CharField('Категория', max_length=200, db_index=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', blank=True, null=True)
    slug = models.SlugField('URL', max_length=200, unique=True, null=False, editable=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)


    class Meta:
        unique_together = (['slug', 'parent'])
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        full_path = [self.name]
        parent_category = self.parent
        while parent_category is not None:
            full_path.append(parent_category.name)
            parent_category = parent_category.parent
        return ' > '.join(full_path[::-1])

    @staticmethod
    def _rand_slug():
        # Generates a random slug consisting of lowercase letters and digits.
        # >>> rand_slug()
        #   'abc123'
        return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(3))

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self._rand_slug() + '-pickBetter' + self.name)
        super(Category, self).save(*args, **kwargs)



# class Category(models.Model):
#     name = models.CharField(max_length=200)
#     slug = models.SlugField(max_length=200, unique=True,blank=True)
#
#
#     class Meta:
#         ordering = ["name"]
#         indexes = [
#             models.Index(fields=["name"]),
#         ]
#         verbose_name = "category"
#         verbose_name_plural = "categories"
#
#     def __str__(self):
#         return self.name


# class PodCategory(models.Model):
#     category = models.ForeignKey(
#         Category, related_name="pod_categories", on_delete=models.CASCADE
#     )
#     name = models.CharField(max_length=200)
#     slug = models.SlugField(max_length=200, unique=True)
#
#     class Meta:
#         ordering = ["name"]
#         indexes = [
#             models.Index(fields=["name"]),
#         ]
#         verbose_name = "podcategory"
#         verbose_name_plural = "podcategory"
#
#     def __str__(self):
#         return self.name