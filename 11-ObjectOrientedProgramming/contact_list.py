
class Contact_List:
    def __init__(self):
        self.contacts = []
        
    def add_contacts(self, contact_object):
        self.contacts.append(contact_object)
        
    def display_contacts(self):
        print("--- Smartphone Contact List ---")
        # Loop through the array and print each contact's details
        for c in self.contacts:
            print(f"{c.name:15} {c.email:25} {c.telephone}")
    
    