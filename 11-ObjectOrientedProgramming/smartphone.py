from contact import Contact
from contact_list import Contact_List

def main():
    # i. Create an object representing a contact list
    my_smartphone_contacts = Contact_List()

    # ii. Create Contact objects and add them to the list
    # Data from: John Brown, Anna May, George Small, Paola Big
    my_smartphone_contacts.add_contacts(Contact("John Brown", "brown@onet.pl", "555234000"))
    my_smartphone_contacts.add_contacts(Contact("Anna May", "am@o2.pl", "232000199"))
    my_smartphone_contacts.add_contacts(Contact("George Small", "smallg@google.pl", "222999100"))
    my_smartphone_contacts.add_contacts(Contact("Paola Big", "bigpaola@poczta.pl", "100200300"))

    # iii. Display the final contact list
    my_smartphone_contacts.display_contacts()

if __name__ == "__main__":
    main()