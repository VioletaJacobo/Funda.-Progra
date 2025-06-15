def load_file():

    filepath= input("Ingrese la ruta del archivo: ")
    file= open(filepath, "r", encoding="utf-8")
    lines  = file.readlines()
    file.close()

    return lines
    
    
my_file = load_file()
print(my_file)