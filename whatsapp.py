from tokenize import group
import pywhatkit

#for contacts

#phone_no = input("Enter phone number: ")

#pywhatkit.sendwhatmsg(phone_no,"the message", 8,33, 1, True, 2)

#for group

group_id = input("Enter groupe id: ")

pywhatkit.sendwhatmsg_to_group(group_id,"Tessssstttt",8, 41)