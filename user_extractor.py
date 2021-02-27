import sys, io, os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "recruit2021.settings")
django.setup()

import csv
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from accounts.models import MyUser

def parsing():
    users = []
    with open('./resource/sogang_likelion_contact.csv', 'r',encoding='cp949') as f:
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
                'email' : i['이메일'],
                'team' : i['팀'],
                'position' : i['직책'],
                })
            else:
                users.append({
                'name' : i['이름'],
                'first_major' : i['학부/학과'],
                'act_no' : i['가입 기수'],
                'phone' : phone_no,
                'email' : i['이메일'],
                'team' : i['팀'],
                'position' : i['직책'],
                })
    return users

# main function
users = parsing()

for i in range(len(users)):
    print(users[i]['name'])

    if "second_major" in users[i]:
        MyUser.objects.create_dummy_user(
            email = users[i]['email'],
            password = 'likelion',
            name = users[i]['name'],
            first_major = users[i]['first_major'],
            second_major = users[i]['second_major'],
            act_no = users[i]['act_no'],
            phone = users[i]['phone'],
            team = users[i]['team'],
            position = users[i]['position'],
        )
    else:
        MyUser.objects.create_dummy_user(
            email = users[i]['email'],
            password = 'likelion',
            name = users[i]['name'],
            first_major = users[i]['first_major'],
            act_no = users[i]['act_no'],
            phone = users[i]['phone'],
            team = users[i]['team'],
            position = users[i]['position'],
        )

