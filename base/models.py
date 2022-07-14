from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django_quill.fields import QuillField
# from ckeditor.fields import RichTextField
# from ckeditor_uploader.fields import RichTextUploadingField
import readtime 



class SubCategory(models.Model):
    # name = models.CharField(max_length=100)
    # slug = models.SlugField(
    #         default='',
    #         editable=False,
    #     )
    
    # created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)
    # def get_absolute_url(self):
    #     kwargs = {
    #         'pk': self.id,
    #         'slug': self.slug
    #     }
    #     return reverse('subcategorypost', kwargs=kwargs)

    # def save(self, *args, **kwargs):
    #     value = self.name
    #     self.slug = slugify(value, allow_unicode=True)
    #     super().save(*args, **kwargs)
    # def __str__(self):
    #     return self.name
    pass
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(
            default='',
            editable=False,
        )
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def get_absolute_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.slug
        }
        return reverse('categorypost', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(
            default='',
            editable=False,
        )
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def get_absolute_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.slug
        }
        return reverse('tagpost', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug =models.SlugField(
            default='',
            editable=False,
        )
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    # subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE,null=True,blank=True)
    thumbnail = models.ImageField(upload_to='postimage/')
    description = QuillField()
    short_description = models.TextField(null=True,blank=True)
    tags = models.ManyToManyField(Tag)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    feature = models.BooleanField(default=False)
    views=models.IntegerField(default=0,null=True,blank=True)
    
    class Meta:
        ordering = ['-created']
    def get_absolute_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.slug
        }
        return reverse('detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.title
    
    