from django import template
import random

register = template.Library()

quotes = [
    'Once upon a midnight dreary, while I pondered, weak and weary...',
    'Ah, distinctly I remember, it was in the bleak December...',
    'Eagerly I wished the morrow; vainly had I sought to borrow...',
    'And the silken, sad, uncertain rustling of each purple curtain...',
]
photos = [
    'decor_photo1.jpg',
    'decor_photo2.jpg',
    'decor_photo3.jpg',
    'decor_photo4.jpg',
    'decor_photo5.jpg',
]

@register.inclusion_tag('side.html')
def sidebar():
    quotendx = random.randrange(0,3)
    photondx = random.randrange(0,4)
    return { 'quote': quotes[quotendx], 'photo' : photos[photondx] }
