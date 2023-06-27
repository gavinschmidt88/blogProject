from django import template

register = template.Library()


@register.filter
def filter_by_created_by(posts, user_id):
    return posts.filter(created_by_id=user_id)
