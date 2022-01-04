names = ['Aavani','Akmaludheen','Anchu','Anju','Archana','Hiba','Irene','Priya','Sachin','Adeeb','Safna','Venkidesh ','Athulya','Aishwarya','Ananthakrishnan','Fakrudeen','ROHITH ','Vishnupriya']

email = ['aavanibaiju18@gmail.com',
'akmalvk6@gmail.com',
'anchupnair@gmail.com ',
'anju.bj98@gmail.com',
'archanamohan098@gmail.com',
'delta.hiba5@gmail.com',
'irenemmthw@gmail.com',
'priya1997klm@gmail.com',
'sachindas512@gmail.com',
'deebt.mec@gmail.com',
'safnake@gmail.com ',
'kvenkidesh@gmail.com',
'athulyacprakash@gmail.com',
'aish.thamburangal@gmail.com',
'ananthakrisb@gmail.com',
'fakrudeenj1994@gmail.com',
'rohithrudra88@gmail.com',
'vishnupriya9562@gmail.com']

import random

names_copy = names[:]
flag = 0
while flag == 0:
    flag = 1
    for i in range(len(names_copy)):
        if names_copy[i] == names[i]:
            random.shuffle(names_copy)
            flag = 0
            break
for i in range(len(names)):
    print(email[i])

import smtplib

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("sender Mail here", "password here")
for i in range(len(names)):
    msg = "subject:Secret Santa \n\nHi {},\n You are assigned as secret santa to give present to {}\n you can spent upto 150 Rs\n Planned to be on Jan 3 2022\n Be sure to bring your Gift!!!\n\nTeam AlphaGo".format(names[i],names_copy[i])
    server.sendmail("cetartificialintelligence@gmail.com", email[i], msg)

server.quit()