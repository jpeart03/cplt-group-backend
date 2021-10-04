from .personal_prompts import personal_prompts
from .professional_prompts import professional_prompts
import random

def generate_prompt(relationship_type='Professional'):
    if relationship_type == 'Personal':
        prompt = random.choice(personal_prompts)
    else:
        prompt = random.choice(professional_prompts)

    return prompt