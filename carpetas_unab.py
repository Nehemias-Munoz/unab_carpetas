import os
path_name = "/Users/nehemiasmunoz/Library/CloudStorage/OneDrive-UNIVERSIDADANDRESBELLO/Unab/Tercer trimestre"
folder_num = 14
os.chdir(path_name)
for i in range(1, folder_num):
    folder_name = "semana_{:02}".format(i)
    if not folder_name in os.listdir(path_name):
        try:
            os.mkdir(folder_name)
            os.chdir(folder_name)
            os.mkdir("clase")
            os.mkdir("recursos")
            os.mkdir("evaluacion")
            os.chdir(path_name)
        except OSError:
            print(f"Error en la creacion del directorio {folder_name}.")
        else:
            print(f"Se ha creado el directorio {folder_name} correctamente.")
    else:
        print(f"El directorio {folder_name} ya existe.")
