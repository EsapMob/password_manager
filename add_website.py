

# créer une fonction pour 
# pouvoir créer un nouveau tuple contenant (website, id, password) et qu'il soit ajouté à la liste
# par exemple saved_password = ([kamas.fr, leskamas, kamas124], [groslolo.com, groslolo, groslolo123])

new_data = []
main_storage = []

def create_password():
    while True:
        add_data = input("Enter informations (or 'save' to stop):\n") 
        if add_data.lower() == 'save':
            break
        new_data.append(add_data)
    print("[INFO] Your news informations:", new_data)

create_password()


def store_password():
    new_storage = input("Do you want to save new_data in main_storage? ('y' or 'no'):\n")
    if new_storage.lower() == 'y':
        main_storage.append(new_data)
        print("[INFO] Data has been saved in main_storage", main_storage)
    
    if not new_storage.lower() == 'y':
        print("[INFO] Nothing was saved.")

    new_data.clear()
    print("[INFO] New_data has been clear", new_data)

store_password()








