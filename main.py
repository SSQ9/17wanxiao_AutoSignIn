import time
import json
import requests
import datetime
from campus import CampusCard
from campus.campus_card.rsa_encrypt import chrysanthemum
from qqmail import sendEmail

#petals = chrysanthemum()


def main():
    # sectets字段录入
    sckey, success, failure, result, phone, password, mail, key = [], [], [], [], [], [], [], []
    # 多人循环录入
    while True:
        try:
            users = input()
            info = users.split(',')
            phone.append(info[0])
            password.append(info[1])
            mail.append(info[2])
            key.append(info[3])
            sckey.append(info[4])
        except BaseException:
            break
    for i, j in enumerate(mail):        
        Semail = sendEmail(mail[i], key[0])
        print(Semail)
        print("-----------------------")
    
if __name__ == '__main__':
    main()
