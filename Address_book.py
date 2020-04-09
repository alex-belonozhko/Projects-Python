import pickle
class PersonalData:
    def dump(self, dict):
        with open("PersonalData", 'wb') as PD:
            pickle.dump(dict, PD)

    def load(self):
        with open("PersonalData", 'rb') as PD:
            return pickle.load(PD)

print("What do you want to do ?: Enter \"1\": to watch contacts, \"2\": add new, \"3\": change contact,\"4\": find number, \"4\": delete")
Choose = int(input())
PD = PersonalData()
if Choose == 1:
    print(PD.load())
elif Choose == 2:
    DictContacts = PD.load()
    Name = input("Enter name: ")
    while Name in DictContacts.keys():
        print("Contact with such name already exist, please repeat: \n")
        Name = input("Enter name :\n")
    Number = input("Enter number :\n")
    DictContacts[Name] = Number
    PD.dump(DictContacts)
    print("Contact added successfully")
elif Choose == 3:
    DictContacts = PD.load()
    print(DictContacts.keys())
    Name = input("Enter name contact to change: \n")
    while Name not in DictContacts.keys():
        print("The contact you entered no exist, please repeat: \n")
        Name = input("Enter name contact to change: \n")
    Choose = int(input("Enter \"1\" to change the name, or \"2\" change number: \n"))
    if Choose == 1:
            NewName = input("Enter new name: \n")
            DictContacts[NewName] = DictContacts[Name]
            del DictContacts[Name]
            PD.dump(DictContacts)
            print("Contact successfully changed")
    elif Choose == 2:
        NewNumber = input("Enter new number: \n")
        del DictContacts[Name]
        DictContacts[Name] = NewNumber
        PD.dump(DictContacts)
        print("Number successfully changed")
elif Choose == 4:
    DictContacts = PD.load()
    print(DictContacts.keys())
    Name = input("Enter contact: ")
    while Name not in DictContacts.keys():
        print("The contact you entered no exist, please repeat: \n")
        Name = input("Enter name contact to change: \n")
    print(DictContacts[Name])
elif Choose == 5:
    DictContacts = PD.load()
    print(DictContacts.keys())
    Name = input("Enter name contact to delete: \n")
    while Name not in DictContacts.keys():
        print("The contact you entered no exist, please repeat: \n")
        Name = input("Enter name contact to change: \n")
    del DictContacts[Name]
    PD.dump(DictContacts)
    print("Contact successfully deleted")