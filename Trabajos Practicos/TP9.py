#Ejercicio 1
"""class Person:
    def __init__(self, name = None, age = None, id = None):
        self.name = name
        self.age = age
        self.id = id
        
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        if type(name) == str:
            self.name = name
        else:
            raise ValueError("El nombre debe ser una cadena de texto.")
    
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        if type(age) == int and age > 0:
           self.age = age
        else:
            raise ValueError("La edad debe ser un numero entero positivo.")
        
    def get_id(self):
        return self.id
    
    def set_id(self, id):
        if type(id) == str and len(id) == 8:
           self.id = id
        else:
            raise ValueError("El DNI debe ser una cadena de 8 caracteres.")
        self.id = id
        
    def show(self):
        print("Nombre:", self.name)
        print("Edad:", self.age)
        print("DNI:", self.id)
        
    def is_of_age(self):
        if self.age >= 18:
            return True
        else:
            return False
        
person1 = Person()
person1.set_name("Florencia")    
person1.set_age(18)
person1.set_id("46476116")

person2 = Person()
person2.set_name("Carla")    
person2.set_age(15)
person2.set_id("49872212")

print("Persona 1: ")
person1.show()
print(f"Es mayor de edad", person1.is_of_age())

print("")
print("Persona 2: ")
person2.show()
print(f"Es mayor de edad", person2.is_of_age())"""
  
#Ejercicio 2

#Ejercicio 3


#Ejercicio 4
"""class agenda:
    def __init__(self, name = None, phone_number = None, email = None):
        self.name = name
        self.phone_number = phone_number
        self.email = email
    
    @property
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
    
    @property
    def get_phone_number(self):
        return self.phone_number
    
    def set_phone_number(self, phone_number):
        self.phone_number = phone_number
    
    @property
    def get_email(self):
        return self.email
    
    def set_email(self, email):
        self.email = email
    
contacts_list = []
option = 0


while option != 5:     
    print("\nMenú:\n1. Añadir contacto\n2. Lista de contactos\n3. Buscar contacto\n4. Editar contacto\n5. Cerrar agenda")
    option = int(input("Segun el menú ingrese la opcion que desea realizar: "))
    add_contact = "si"
    
    if option == 1:
        while add_contact.lower() == "si":
            contacts = agenda()
            contacts.set_name(input("\nIngrese el nombre del contacto: "))
            contacts.set_phone_number(input("Ingrese el numero de telefono: "))
            contacts.set_email(input("Ingrese el email del contacto: "))
            
            contacts_list.append(contacts)
            
            add_contact = input("Desea agregar otro contacto?(si/no): ")
            
    elif option == 2:
        if len(contacts_list) > 0:
            print("\nAgenda: ")
            for contacts in contacts_list:
                print("Nombre:", contacts.get_name)
                print("Telefono:", contacts.get_phone_number)
                print("Email:", contacts.get_email)
                print("-----------------------------")
        else:
            print("Primero debe cargar los datos en la agenda")
    
    elif option == 3:
        if len(contacts_list) > 0:
            found = False
            search_contact = input("\nIngrese el nombre del contacto que quiere buscar: ")
            for contacts in contacts_list:
                if contacts.get_name.lower() == search_contact.lower():
                    number = contacts.get_phone_number
                    found = True
                    break
            if found == False:
                print("El contacto que busca no se encuentra en la agenda") 
            else:
                print(f"El numero de telefono de {search_contact} es {number}")           
        else:
            print("Primero debe cargar los datos en la agenda")
    
    elif option == 4:
        if len(contacts_list) > 0:
            modify_contact = "si"
            while modify_contact.lower() == "si":
                contact_to_modify = input("\nIngrese el nombre del contacto que quiere modificar: ")
                for contacts in contacts_list:
                    if contacts.get_name.lower() == contact_to_modify.lower():
                        
                        contacts.set_name(input("Ingrese el nuevo nombre del contacto: "))
                        contacts.set_phone_number(input("Ingrese el nuevo numero de telefono: "))
                        contacts.set_email(input("Ingrese el nuevo email del contacto: "))
                        
                        print("El contacto se modifico.")
                        break
                else:
                    print("La persona buscada no se encuentra en la agenda")
                    break
                        
                modify_contact = input("Desea modificar otro contacto?(si/no): ")
        else:
                print("Primero debe cargar los datos en la agenda")"""