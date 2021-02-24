import csv

import sys, io, os
import django

sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "recruit2021.settings")
django.setup()

from accounts.models import MyUser

def parsing():
    users = []
    with open('./resource/멋쟁이사자처럼_서강대_Contact.csv', 'r') as f:
        reader = csv.DictReader(f)

        for i in reader:
            separator_idx = i['학부/학과'].find('/')
            phone_no = "".join(i['연락처'].split('-'))
            if separator_idx != -1:
                users.append({
                'name' : i['이름'],
                'first_major' : i['학부/학과'][0:separator_idx],
                'second_major' : i['학부/학과'][separator_idx+1:], 
                'act_no' : i['가입 기수'],
                'phone' : phone_no,
                'email' : i['이메일']
                })
            else:
                users.append({
                'name' : i['이름'],
                'first_major' : i['학부/학과'],
                'act_no' : i['가입 기수'],
                'phone' : phone_no,
                'email' : i['이메일']
                })
    return users

if __name__ == '__main__':
    users = parsing()

    for i in range(len(users)):
        if "second_major" in users[i]:
            MyUser(
                name = users[i]['name'],
                first_major = users[i]['first_major'],
                second_major = users[i]['second_major'],
                act_no = users[i]['act_no'],
                phone = users[i]['phone'],
                email = users[i]['email'],
            ).save()

        else:    
            MyUser(
                name = users[i]['name'],
                first_major = users[i]['first_major'],
                act_no = users[i]['act_no'],
                phone = users[i]['phone'],
                email = users[i]['email'],
            ).save()


