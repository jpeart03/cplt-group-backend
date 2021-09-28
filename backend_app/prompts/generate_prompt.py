from .personal_prompts import personal_prompts
from .professional_prompts import professional_prompts
import random

def generate_prompt(relationship_type='professional'):
    if relationship_type == 'personal':
        prompt = random.choice(personal_prompts)
    else:
        prompt = random.choice(professional_prompts)

    return prompt