import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()


from solace.models import Prof


# prof2 = Prof.objects.get(id=3)
# daniel = Prof.objects.get(id=2)

# prof2data = prof2.profdata.all()
# danieldata = daniel.profdata.all()

# json_data = serializers.serialize('json', profdata)


print("THE DATA IN JSON FORMAT.")
# print(json_data)
data_list1 = []

def fetch(profdata, profUname):
    data_list2 = []
    for data in profdata:
        data_dict = {
            'prof id': data.prof.id,
            'questionNo': data.questionNo,
            'question': data.questionText,
            'answer': data.answer
        }
        data_list2.append(data_dict)

    print(f"DONE for prof: {profUname}")
    data_list1.append(data_list2)

def get_data(profId):
    prof = Prof.objects.get(id=profId)
    profData = prof.profdata.all()
    print(f"Fetching data of Prof: {profId}")
    fetch(profData, prof.username)




json_output = json.dumps(data_list1, indent=5)
print("THE OUTPUT IS = ")
print(json_output)