class Contact:
  #represents individual contact associated with details
  def __init__(self, name, phone_number):
    self.name = name
    self.phone_number = phone_number

  def __str__(self):
    # returns a string representation of the contact
    return f"{self.name} {self.phone_number}"


# manages the collection of contacts, provides methods to perform CRUD operations
class ContactManager:
  


# Initialize the contact manager
# Parameters: filename (str): The file name where contacts are saved and loaded from.
  def __init__(self, filename='contacts.txt'):
    self.contacts = []    # List to store all contacts.
    self.filename = filename    # File to persist contacts.
    self.load_contacts()    # File to persist contacts.


  def load_contacts(self):
    try:
      with open(self.filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
          name, phone_number = line.strip().split(',')
          self.contacts.append(Contact(name, phone_number))
    except FileNotFoundError:
      pass

  def save_contacts(self):
    with open(self.filename, 'w') as file:
      for contact in self.contacts:
        file.write(f"{contact.name},{contact.phone_number}\n")

  def add_contact(self, name, phone_number):
    self.contacts.append(Contact(name, phone_number))
    self.save_contacts()

  def view_contacts(self):
    for contact in self.contacts:
      print(contact)

  def delete_contact(self, name):
    self.contacts = [contact for contact in self.contacts if contact.name != name]
    self.save_contacts()
  

def main():
  manager = ContactManager()

  while True:
    print("\nContact Manager:")
    print("1. Add contact")
    print("2. View contacts")
    print("3. Delete contact")
    print("4. Exit")


    choice = input("Enter your choice: ")

    #process user's choice
    if choice == '1':
      name = input("Enter name: ")
      phone_number = input("Enter phone number: ")
      manager.add_contact(name, phone_number)
    elif choice == '2':
      manager.view_contacts()
    elif choice == '3':
      name = input("Enter name: ")
      manager.delete_contact(name)
    elif choice == '4':
      break
    else:
      print("Invalid choice, Please try again")

if __name__ == "__main__":
  main()


