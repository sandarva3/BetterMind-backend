import os
import django
import json
from geminitest import rank_professionals_with_gemini

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()


from solace.models import Prof,User


# prof2 = Prof.objects.get(id=3)
# daniel = Prof.objects.get(id=2)

# prof2data = prof2.profdata.all()
# danieldata = daniel.profdata.all()

# json_data = serializers.serialize('json', profdata)


print("THE DATA IN JSON FORMAT.")
# print(json_data)


profData_list = []
userData_list = []

def fetch(data, Uname, p):
    data_list2 = []
    if p == True:
        for d in data:
            data_dict = {
                'prof id': d.prof.id,
                'questionNo': d.questionNo,
                'question': d.questionText,
                'answer': d.answer
            }
            data_list2.append(data_dict)
        profData_list.append(data_list2)
        
        print(f"DONE for prof: {Uname}")
    else:
        for d in data:
            data_dict = {
                'user id': d.user.id,
                'questionNo': d.questionNo,
                'question': d.questionText,
                'answer': d.answer
            }
            data_list2.append(data_dict)
        userData_list.append(data_list2)

        print(f"DONE for user: {Uname}")


def get_data(Id, p):
    if p == True:
        prof = Prof.objects.get(id=Id)
        profData = prof.profdata.all()
        uname = prof.username
        print(f"Fetching data of Prof: {uname}")
        fetch(profData, uname, p)
    else:
        user = User.objects.get(id=Id)
        userData = user.userdata.all()
        uname = user.username
        print(f"Fetching data of User: {uname}")
        fetch(userData, uname, p)


prof_ids = [2,3,13]
#prof_ids = [2,13]
for pid in prof_ids:
    get_data(pid, p=True)

user_ids = [14]
for uid in user_ids:
    get_data(uid, p=False)


prof_Jsonoutput = json.dumps(profData_list, indent=2)
user_Jsonoutput = json.dumps(userData_list, indent=2)
print("Professionals data = ")
print(prof_Jsonoutput)
print("Users data = ")
print(user_Jsonoutput)

print("SENDING TO Gemini")
matchingProfs = rank_professionals_with_gemini(user_Jsonoutput, prof_Jsonoutput)
print(f"THE RESULT From Gemini: ")
print(matchingProfs)
ids = [int(profId) for profId in matchingProfs.split(",")]
print(f"The Ids are: {ids}")
print("The usernames are: ")
for i in ids:
    object = Prof.objects.get(id=i)
    name = object.username
    print(name)