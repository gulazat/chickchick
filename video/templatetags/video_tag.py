from django import template

from ..models import Video,Category,Tag

register = template.Library()

@register.simple_tag
def get_recent_entries(num=4):
    return Video.objects.all().order_by('-create_time')[:num]

@register.simple_tag
def get_popular_entries(num=4):
    return Video.objects.all().order_by('-view_count')[:num]
#
@register.simple_tag
def get_categories():
    return Category.objects.all()




@register.simple_tag
def get_tags():
    return Tag.objects.all()



@register.simple_tag
def get_whole_content(num = 16):
    return Video.objects.all().order_by('category')[:num]


@register.simple_tag
def get_whole_tag(num = 8):
    return Video.objects.all().order_by('tag_id')[:num]