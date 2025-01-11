import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from solace.models import Prof, ProfData

questions = [
    "What's your name?",
    "What's your fav color?",
    "How old are you?",
    "What's your father name?",
    "What's your mother name?",
    "What's your grandpa name?",
    "What's your grandma name?",
    "Where do you live?",
    "Where's your original hometown?",
    "FINE?"
]

answers = [
    "My name is A.",
    "My fav color is blue.",
    "I'm 20.",
    "My dad name is B.",
    "My mom name is C",
    "My grandpa name is D",
    "My grandma name is E",
    "I live in ktm",
    "My original hometown is Sharanpur",
    "Kind of, right now."
]

prof2 = Prof.objects.get(id=3)
daniel = Prof.objects.get(id=2)
for i in range(0, 10):
    print(f"Data Entered: {i}")
    ProfData.objects.create(prof=prof2,
            questionNo=i,
            questionText=questions[i],
            answer=answers[i]
        )
    ProfData.objects.create(prof=daniel,
            questionNo=i,
            questionText=questions[i],
            answer=answers[i]
        )

print("DONE")