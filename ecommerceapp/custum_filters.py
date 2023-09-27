from django import template
import json


register = template.Library()

@register.filter
def star_rating(value):
    try:
        value = int(value)
        return '★' * value + '☆' * (5 - value)
    except ValueError:
        return value


@register.filter
def extract_room_names(items_json):
    try:
        # Parse the JSON data
        items = json.loads(items_json)
        
        # Extract and join room names
        room_names = [item.get('roomName', '') for item in items]
        return ', '.join(room_names)
    except:
        return ''
