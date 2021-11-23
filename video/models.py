
from django.db import models
from django.conf import settings

# Create your models here.


class Category(models.Model):
    list_display = ("C_title",)
    C_title = models.CharField(max_length=128, blank = True, null = True,verbose_name= '视频分类')

    def __str__(self):
        return self.C_title

    class Meta:
        db_table = "A_category"



class Tag(models.Model):
    list_display = ("T_tag",)
    T_tag = models.CharField(max_length=128, verbose_name='视频标签')

    def __str__(self):
        return self.T_tag

    class Meta:
        db_table = "C_tag"




class Video(models.Model):


    title = models.CharField(max_length=100, blank=True, null=True)
    desc = models.CharField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(Category, null=True,on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, null=True,on_delete=models.CASCADE)
    file = models.FileField(max_length=255)
    cover = models.ImageField(upload_to='cover/', blank=True, null=True)

    view_count = models.IntegerField(default=0, blank=True)

    create_time = models.DateTimeField(auto_now_add=True, blank=True, max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "C_video"


    def increase_view_count(self):
        self.view_count += 1
        self.save(update_fields=['view_count'])



