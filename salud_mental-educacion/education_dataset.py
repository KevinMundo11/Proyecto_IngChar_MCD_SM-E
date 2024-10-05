import os
import requests
import zipfile
from io import BytesIO
from datetime import datetime

data_path='./data/raw'
links_folder_path='./references/links'
descriptions_folder_path='./references/descriptions'

def get_name(url):
    indices=[index for index in range(len(url)) if url[index]=="/"]
    last_slash=indices[-1]
    file_name_with=url[last_slash+1:]
    indices=[index for index in range(len(file_name_with)) if file_name_with[index]=="."]
    last_point=indices[-1]
    file_name_without=file_name_with[last_point+1:]
    return {'with':file_name_with,'without':file_name_without}

def download_and_extract_zip(url):
    # Creamos el directorio de extracción en caso de no existir
    file_name=get_name(url)['without']
    extract_to=f"{data_path}/{file_name}"

    os.makedirs(extract_to, exist_ok=True)

    # Descargamos el archivo zip
    response = requests.get(url)
    if response.status_code == 200:
        # Abrimos y extraemos el contenido
        with zipfile.ZipFile(BytesIO(response.content)) as z:
            z.extractall(extract_to)
            print(f'El contenido de {url} se extrajo a {extract_to}')
    else:
        print(f'Error al descargar {url}, status code: {response.status_code}')

def download_excel(url):
    # Creamos el directorio de extracción en caso de no existir
    os.makedirs(data_path, exist_ok=True)
    # Se hace una petición GET al url
    response = requests.get(url)
    

    if response.status_code == 200:
        file_name=get_name(url)['with']
        file_path=f"{data_path}/{file_name}"
        # Se guarda el contenido
        with open(file_path, 'wb') as f:
            f.write(response.content)
        print(f'Descarga completa:{url}')
        print(f'Archivo guardado:{file_path}')
    else:
        print('Error al intentar descargar el archivo, status code:', response.status_code)

def get_file_type(url):
    file_name=get_name(url)['with']
    indices=[index for index in range(len(file_name)) if file_name[index]=="."]
    last_point=indices[-1]
    return file_name[last_point+1:]

def write_description(url,data_source_txt_name,download_date):
    #Se consigue el nombre de la fuente para poder leer los archivos de texto
    data_source=data_source_txt_name.split('_')[0] 
    with open(f"{descriptions_folder_path}/{data_source}_description.txt",'r') as file:
        descripcion=file.read()

    string=f"""
           Nombre:{data_source}\n
           Fecha de descarga:{download_date}\n
           Descripción:{descripcion}\n

           """
    os.makedirs(f"{data_path}/detailed_descriptions", exist_ok=True)
    with open(f"{data_path}/detailed_descriptions/{data_source}_details.txt",'w') as file:
        file.write(string)

# Lista de enlaces a descargar: 

links={}
for link_txt_file in os.listdir(links_folder_path):
    links_file_path=f"{links_folder_path}/{link_txt_file}"
    with open(file=links_file_path,mode='r') as txt_file:
        content=txt_file.read()
    links[link_txt_file]=(content.split('\n'))


# Las descargas a './data/raw':


os.makedirs(f"{data_path}/descriptions", exist_ok=True)

for data_source,link_list in links.items():
    print(data_source)
    for link in link_list:
        file_type=get_file_type(link)
        if file_type in ['xls']:
            download_excel(link)
            download_date = datetime.now().strftime("%Y-%m-%d")
            write_description(link,data_source,download_date)
        elif file_type=='zip':
            download_and_extract_zip(link)
            download_date = datetime.now().strftime("%Y-%m-%d")
            write_description(link,data_source,download_date)
        
        

