

#from salud_mental-educacion.config import PROCESSED_DATA_DIR, RAW_DATA_DIR

import os
import requests
import zipfile
import shutil
def descargar_archivo_xlsx(url, data, folder_name, file_name):
  """Descarga un archivo .xlsx de una URL y lo guarda en la carpeta especificada.
  Args:
    url (str): URL desde donde descargar el archivo.
    data (str): Parámetro de data para la solicitud POST.
    folder_name (str): Nombre de la carpeta donde se guardará el archivo.
    file_name (str): Nombre del archivo que se descargará."""
    # Crear una sesión para manejar cookies y mantener una sesión activa
  session = requests.Session()

    # Crear la carpeta si no existe
  if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"Carpeta '{folder_name}' creada.")

    # Realizar la solicitud POST para descargar el archivo
  response = session.post(url, data={data: ""})

    # Verificar si la respuesta fue exitosa
  if response.status_code == 200:
        # Ruta completa donde se guardará el archivo
        file_path = os.path.join(folder_name, file_name)

        # Guardar el archivo en el sistema
        with open(file_path, "wb") as f:
            f.write(response.content)
        print(f"Archivo '{file_name}' descargado y guardado en '{folder_name}'.")
  else:
        print(f"Error al descargar el archivo '{file_name}'. Código de estado: {response.status_code}")

def descargar_archivo_zip(url, data, folder_name, file_name, subfolder):
    """
    Descarga un archivo .zip de una URL, lo guarda en una carpeta, lo descomprime y extrae archivos .csv, por ultimo elimina el archivo .zip.

    Args:
        url (str): URL desde donde descargar el archivo.
        data (str): Parámetro de data para la solicitud POST.
        folder_name (str): Nombre de la carpeta donde se guardará el archivo.
        file_name (str): Nombre del archivo que se descargará.
        subfolder (str): Subcarpeta donde se guardarán los archivos extraídos.
    """
    # Crear una sesión para manejar cookies y mantener una sesión activa
    session = requests.Session()

    # Crear la carpeta si no existe
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"Carpeta '{folder_name}' creada.")

    # Realizar la solicitud POST para descargar el archivo
    response = session.post(url, data={data: ""})

    # Verificar si la respuesta fue exitosa
    if response.status_code == 200:
        # Ruta completa donde se guardará el archivo .zip
        zip_file_path = os.path.join(folder_name, file_name)

        # Guardar el archivo .zip en el sistema
        with open(zip_file_path, "wb") as f:
            f.write(response.content)
            print(f"Archivo '{file_name}' descargado y guardado en '{folder_name}'.")

        # Descomprimir el archivo .zip y extraer el archivo .csv
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            # Buscar el archivo .csv dentro del .zip
            for zip_info in zip_ref.infolist():
                if zip_info.filename.endswith('.csv'):
                    # Generar la ruta completa para el archivo .csv
                    csv_file_name = file_name.replace('.zip', '.csv')
                    csv_folder_path = os.path.join('..', 'data', 'raw', subfolder)

                    # Crear la carpeta si no existe
                    if not os.path.exists(csv_folder_path):
                        os.makedirs(csv_folder_path)

                    # Ruta completa del archivo .csv extraído
                    csv_file_path = os.path.join(csv_folder_path, csv_file_name)

                    # Extraer el archivo .csv y guardarlo en la carpeta correspondiente
                    with zip_ref.open(zip_info) as source, open(csv_file_path, 'wb') as target:
                        target.write(source.read())
                        print(f"Archivo '{csv_file_name}' extraído y guardado en '{csv_folder_path}'.")

        # Eliminar el archivo .zip después de la extracción
        os.remove(zip_file_path)
        print(f"Archivo '{file_name}' eliminado después de la extracción.")
    else:
        print(f"Error al descargar el archivo '{file_name}'. Código de estado: {response.status_code}")



def main():
# Carpeta principal
    main_folder = "ENSANUT-CATALOGOS"
    folder_adolescentes = os.path.join('..', 'docs', main_folder, "CATALOGOS ADOLESCENTES")
    folder_adultos = os.path.join('..', 'docs', main_folder, "CATALOGOS ADULTOS")
    adolescentes_cat = [
        {
            "url": "https://ensanut.insp.mx/encuestas/ensa2000/descargas.php",
            "data": "ArchIdMDEtQ29tcG9uZW50ZSBkZSBTQUxVRC8wMy1DdWVzdGlvbmFyaW8gaW5kaXZpZHVhbDogQWRvbGVzY2VudGVzIGRlIDEwIGEgMTkgYcOxb3MgZGUgZWRhZC9BZG9sZXNjZW50ZXMuQ2F0w6Fsb2dvLnhsc3g=",
            "file_name": "ENSANUT-Adolescentes-Catálogo-2000.xlsx"
        },
        {
            "url": "https://ensanut.insp.mx/encuestas/ensanut2006/descargas.php",
            "data": "ArchIdMDEtQ29tcG9uZW50ZSBkZSBTQUxVRC8wNC1DdWVzdGlvbmFyaW8gaW5kaXZpZHVhbDogQWRvbGVzY2VudGVzIGRlIDEwIGEgMTkgYcOxb3MgZGUgZWRhZC9BZG9sZXNjZW50ZXMuQ2F0w6Fsb2dvLnhsc3g=",
            "file_name": "ENSANUT-Adolescentes-Catálogo-2006.xlsx"
        },
        {
            "url": "https://ensanut.insp.mx/encuestas/ensanut2012/descargas.php",
            "data": "ArchIdMDEtQ29tcG9uZW50ZSBkZSBTQUxVRC8wMy1DdWVzdGlvbmFyaW8gaW5kaXZpZHVhbDogQWRvbGVzY2VudGVzIGRlIDEwIGEgMTkgYcOxb3MgZGUgZWRhZC9BZG9sZXNjZW50ZXMuQ2F0w6Fsb2dvLnhsc3g=",
            "file_name": "ENSANUT-Adolescentes-Catálogo-2012.xlsx"
        },
        {
            "url": "https://ensanut.insp.mx/encuestas/ensanut2016/descargas.php",
            "data": "ArchIdMDEtQ29tcG9uZW50ZSBkZSBTQUxVRC8wMi1DdWVzdGlvbmFyaW8gZGUgQWRvbGVzY2VudGVzIGRlIDEyIGEgMTkgQcOxb3MgLSBFbmZlcm1lZGFkZXMgQ3LDs25pY2FzL2Fkb2xfY3JvbmljYXMuQ2F0w6Fsb2dvLnhsc3g=",
            "file_name": "ENSANUT-Adolescentes-Catálogo-2016.xlsx"
        },
        {
            "url": "https://ensanut.insp.mx/encuestas/ensanut2018/descargas.php",
            "data": "ArchIdMDEtQ29tcG9uZW50ZSBkZSBTQUxVRC8wMy1DdWVzdGlvbmFyaW8gZGUgU2FsdWQgZGUgQWRvbGVzY2VudGVzICgxMCBhIDE5IGHDsW9zKS9DU19BRE9MRVNDRU5URVMuQ2F0w6Fsb2dvLnhsc3g=",
            "file_name": "ENSANUT-Adolescentes-Catálogo-2018.xlsx"
        },
        {
            "url": "https://ensanut.insp.mx/encuestas/ensanutcontinua2020/descargas.php",
            "data": "ArchIdMDEtQ29tcG9uZW50ZSBkZSBTQUxVRC8wMy1DdWVzdGlvbmFyaW8gZGUgU2FsdWQgZGUgQWRvbGVzY2VudGVzICgxMCBhIDE5IGHDsW9zKS9hZG9sZXNjZW50ZXNfdmFjX3RhYl9lbnNhbnV0MjAyMF93LkNhdMOhbG9nby54bHN4",
            "file_name": "ENSANUT-Adolescentes-Catálogo-2020.xlsx"
        },
        {
            "url": "https://ensanut.insp.mx/encuestas/ensanutcontinua2021/descargas.php",
            "data": "ArchIdMDEtQ29tcG9uZW50ZSBkZSBTQUxVRC8wMy1DdWVzdGlvbmFyaW8gZGUgc2FsdWQgZGUgYWRvbGVzY2VudGVzICgxMCBhIDE5IGHDsW9zKS9lbnNhZG9sMjAyMV9lbnRyZWdhX3dfMTRfMTJfMjAyMS5DYXTDoWxvZ28ueGxzeA==",
            "file_name": "ENSANUT-Adolescentes-Catálogo-2021.xlsx"
        },
        {
            "url": "https://ensanut.insp.mx/encuestas/ensanutcontinua2022/descargas.php",
            "data": "ArchIdMDEtQ29tcG9uZW50ZSBkZSBTQUxVRC8wMy1DdWVzdGlvbmFyaW8gZGUgc2FsdWQgZGUgYWRvbGVzY2VudGVzICgxMCBhIDE5IGHDsW9zKS9lbnNhZG9sMjAyMl9lbnRyZWdhX3cuQ2F0w6Fsb2dvLnhsc3g=",
            "file_name": "ENSANUT-Adolescentes-Catálogo-2022.xlsx"
        },
        {
            "url": "https://ensanut.insp.mx/encuestas/ensanutcontinua2023/descargas.php",
            "data": "ArchIdMDEtQ29tcG9uZW50ZSBkZSBTQUxVRC8wMy1DdWVzdGlvbmFyaW8gZGUgc2FsdWQgZGUgYWRvbGVzY2VudGVzICgxMCBhIDE5IGHDsW9zKS9hZG9sZXNjZW50ZXNfZW5zYW51dDIwMjNfd19uLkNhdMOhbG9nby54bHN4",
            "file_name": "ENSANUT-Adolescentes-Catálogo-2023.xlsx"
    }
]

# Segundo bloque (adultos)
    adultos_cat = [
        {
            "url": "https://ensanut.insp.mx/encuestas/ensa2000/descargas.php",
            "data": "ArchIdMDEtQ29tcG9uZW50ZSBkZSBTQUxVRC8wMi1DdWVzdGlvbmFyaW8gaW5kaXZpZHVhbDogQWR1bHRvcyBkZSAyMCBvIG3DoXMgYcOxb3MgZGUgZWRhZC9BZHVsdG9zLkNhdMOhbG9nby54bHN4",
            "file_name": "ENSANUT-Adultos-Catálogo-2000.xlsx"
        },
        {
            "url": "https://ensanut.insp.mx/encuestas/ensanut2006/descargas.php",
            "data": "ArchIdMDEtQ29tcG9uZW50ZSBkZSBTQUxVRC8wMy1DdWVzdGlvbmFyaW8gaW5kaXZpZHVhbDogQWR1bHRvcyBkZSAyMCBvIG3DoXMgYcOxb3MgZGUgZWRhZC9BZHVsdG9zLkNhdMOhbG9nby54bHN4",
            "file_name": "ENSANUT-Adultos-Catálogo-2006.xlsx"
        },
        {
            "url": "https://ensanut.insp.mx/encuestas/ensanut2012/descargas.php",
            "data": "ArchIdMDEtQ29tcG9uZW50ZSBkZSBTQUxVRC8wMi1DdWVzdGlvbmFyaW8gaW5kaXZpZHVhbDogQWR1bHRvcyBkZSAyMCBvIG3DoXMgYcOxb3MgZGUgZWRhZC9BZHVsdG9zLkNhdMOhbG9nby54bHN4",
            "file_name": "ENSANUT-Adultos-Catálogo-2012.xlsx"
        },
        {
            "url": "https://ensanut.insp.mx/encuestas/ensanut2016/descargas.php",
            "data": "ArchIdMDEtQ29tcG9uZW50ZSBkZSBTQUxVRC8wMy1DdWVzdGlvbmFyaW8gZGUgQWR1bHRvcyBkZSAyMCBBw7FvcyBvIE3DoXMvMDEtQ3Vlc3Rpb25hcmlvIGRlIEFkdWx0b3MgZGUgMjAgQcOxb3MgbyBNw6FzIC0gRW5mZXJtZWRhZGVzIENyw7NuaWNhcy9hZHVsX2Nyb25pY2FzLkNhdMOhbG9nby54bHN4",
            "file_name": "ENSANUT-Adultos-Catálogo-2016.xlsx"
        },
        {
            "url": "https://ensanut.insp.mx/encuestas/ensanut2018/descargas.php",
            "data": "ArchIdMDEtQ29tcG9uZW50ZSBkZSBTQUxVRC8wMi1DdWVzdGlvbmFyaW8gZGUgU2FsdWQgZGUgQWR1bHRvcyAoMjAgYcOxb3MgbyBtw6FzKS9DU19BRFVMVE9TLkNhdMOhbG9nby54bHN4",
            "file_name": "ENSANUT-Adultos-Catálogo-2018.xlsx"
        },
        {
            "url": "https://ensanut.insp.mx/encuestas/ensanutcontinua2020/descargas.php",
            "data": "ArchIdMDEtQ29tcG9uZW50ZSBkZSBTQUxVRC8wMi1DdWVzdGlvbmFyaW8gZGUgU2FsdWQgZGUgQWR1bHRvcyAoMjAgYcOxb3MgbyBtw6FzKS9hZHVsdG9zX3ZhY190YWJfZW5zYW51dDIwMjBfdy5DYXTDoWxvZ28ueGxzeA==",
            "file_name": "ENSANUT-Adultos-Catálogo-2020.xlsx"
        },
        {
            "url": "https://ensanut.insp.mx/encuestas/ensanutcontinua2021/descargas.php",
            "data": "ArchIdMDEtQ29tcG9uZW50ZSBkZSBTQUxVRC8wNC1DdWVzdGlvbmFyaW8gZGUgc2FsdWQgZGUgYWR1bHRvcyAoMjAgYcOxb3MgbyBtw6FzKS9lbnNhZHVsMjAyMV9lbnRyZWdhX3dfMTVfMTJfMjAyMS5DYXTDoWxvZ28ueGxzeA==",
            "file_name": "ENSANUT-Adultos-Catálogo-2021.xlsx"
        },
        {
            "url": "https://ensanut.insp.mx/encuestas/ensanutcontinua2022/descargas.php",
            "data": "ArchIdMDEtQ29tcG9uZW50ZSBkZSBTQUxVRC8wNC1DdWVzdGlvbmFyaW8gZGUgc2FsdWQgZGUgYWR1bHRvcyAoMjAgYcOxb3MgbyBtw6FzKS9lbnNhZHVsMjAyMl9lbnRyZWdhX3cuQ2F0w6Fsb2dvLnhsc3g=",
            "file_name": "ENSANUT-Adultos-Catálogo-2022.xlsx"
        },
        {
            "url": "https://ensanut.insp.mx/encuestas/ensanutcontinua2023/descargas.php",
            "data": "ArchIdMDEtQ29tcG9uZW50ZSBkZSBTQUxVRC8wNC1DdWVzdGlvbmFyaW8gZGUgc2FsdWQgZGUgYWR1bHRvcyAoMjAgYcOxb3MgbyBtw6FzKS9hZHVsdG9zX2Vuc2FudXQyMDIzX3dfbi5DYXTDoWxvZ28ueGxzeA==",
            "file_name": "ENSANUT-Adultos-Catálogo-2023.xlsx"
        }
    ]

    adolescentes_data = [
        {
            "url": "https://ensanut.insp.mx/encuestas/ensa2000/descargas.php",
            "data": "ArchIdMDEtQ29tcG9uZW50ZSBkZSBTQUxVRC8wMy1DdWVzdGlvbmFyaW8gaW5kaXZpZHVhbDogQWRvbGVzY2VudGVzIGRlIDEwIGEgMTkgYcOxb3MgZGUgZWRhZC9BZG9sZXNjZW50ZXMuY3N2LmNzdi56aXA=",
            "file_name": "ENSANUT-Adolescentes-Datos-2000.zip"
        },
        {
            "url": "https://ensanut.insp.mx/encuestas/ensanut2006/descargas.php",
            "data": "ArchIdMDEtQ29tcG9uZW50ZSBkZSBTQUxVRC8wNC1DdWVzdGlvbmFyaW8gaW5kaXZpZHVhbDogQWRvbGVzY2VudGVzIGRlIDEwIGEgMTkgYcOxb3MgZGUgZWRhZC9BZG9sZXNjZW50ZXMuY3N2LmNzdi56aXA=",
            "file_name": "ENSANUT-Adolescentes-Datos-2006.zip"
        },
        {
            "url": "https://ensanut.insp.mx/encuestas/ensanut2012/descargas.php",
            "data": "ArchIdMDEtQ29tcG9uZW50ZSBkZSBTQUxVRC8wMy1DdWVzdGlvbmFyaW8gaW5kaXZpZHVhbDogQWRvbGVzY2VudGVzIGRlIDEwIGEgMTkgYcOxb3MgZGUgZWRhZC9BZG9sZXNjZW50ZXMuY3N2LmNzdi56aXA=",
            "file_name": "ENSANUT-Adolescentes-Datos-2012.zip"
        },
        {
            "url": "https://ensanut.insp.mx/encuestas/ensanut2016/descargas.php",
            "data": "ArchIdMDEtQ29tcG9uZW50ZSBkZSBTQUxVRC8wMi1DdWVzdGlvbmFyaW8gZGUgQWRvbGVzY2VudGVzIGRlIDEyIGEgMTkgQcOxb3MgLSBFbmZlcm1lZGFkZXMgQ3LDs25pY2FzL2Fkb2xfY3JvbmljYXMuY3N2LmNzdi56aXA=",
            "file_name": "ENSANUT-Adolescentes-Datos-2016.zip"
        },
        {
            "url": "https://ensanut.insp.mx/encuestas/ensanut2018/descargas.php",
            "data": "ArchIdMDEtQ29tcG9uZW50ZSBkZSBTQUxVRC8wMy1DdWVzdGlvbmFyaW8gZGUgU2FsdWQgZGUgQWRvbGVzY2VudGVzICgxMCBhIDE5IGHDsW9zKS9DU19BRE9MRVNDRU5URVMuY3N2LmNzdi56aXA=",
            "file_name": "ENSANUT-Adolescentes-Datos-2018.zip"
        },
        {
            "url": "https://ensanut.insp.mx/encuestas/ensanutcontinua2020/descargas.php",
            "data": "ArchIdMDEtQ29tcG9uZW50ZSBkZSBTQUxVRC8wMy1DdWVzdGlvbmFyaW8gZGUgU2FsdWQgZGUgQWRvbGVzY2VudGVzICgxMCBhIDE5IGHDsW9zKS9hZG9sZXNjZW50ZXNfdmFjX3RhYl9lbnNhbnV0MjAyMF93LmNzdi5jc3Yuemlw",
            "file_name": "ENSANUT-Adolescentes-Datos-2020.zip"
        },
        {
            "url": "https://ensanut.insp.mx/encuestas/ensanutcontinua2021/descargas.php",
            "data": "ArchIdMDEtQ29tcG9uZW50ZSBkZSBTQUxVRC8wMy1DdWVzdGlvbmFyaW8gZGUgc2FsdWQgZGUgYWRvbGVzY2VudGVzICgxMCBhIDE5IGHDsW9zKS9lbnNhZG9sMjAyMV9lbnRyZWdhX3dfMTRfMTJfMjAyMS5jc3YuY3N2LnppcA==",
            "file_name": "ENSANUT-Adolescentes-Datos-2021.zip"
        },
        {
            "url": "https://ensanut.insp.mx/encuestas/ensanutcontinua2022/descargas.php",
            "data": "ArchIdMDEtQ29tcG9uZW50ZSBkZSBTQUxVRC8wMy1DdWVzdGlvbmFyaW8gZGUgc2FsdWQgZGUgYWRvbGVzY2VudGVzICgxMCBhIDE5IGHDsW9zKS9lbnNhZG9sMjAyMl9lbnRyZWdhX3cuY3N2LmNzdi56aXA=",
            "file_name": "ENSANUT-Adolescentes-Datos-2022.zip"
        },
        {
            "url": "https://ensanut.insp.mx/encuestas/ensanutcontinua2023/descargas.php",
            "data": "ArchIdMDEtQ29tcG9uZW50ZSBkZSBTQUxVRC8wMy1DdWVzdGlvbmFyaW8gZGUgc2FsdWQgZGUgYWRvbGVzY2VudGVzICgxMCBhIDE5IGHDsW9zKS9hZG9sZXNjZW50ZXNfZW5zYW51dDIwMjNfd19uLmNzdi5jc3Yuemlw",
            "file_name": "ENSANUT-Adolescentes-Datos-2023.zip"
        }
    ]

# Segundo bloque (adultos)
    adultos_data = [
        {
            "url": "https://ensanut.insp.mx/encuestas/ensa2000/descargas.php",
            "data": "ArchIdMDEtQ29tcG9uZW50ZSBkZSBTQUxVRC8wMi1DdWVzdGlvbmFyaW8gaW5kaXZpZHVhbDogQWR1bHRvcyBkZSAyMCBvIG3DoXMgYcOxb3MgZGUgZWRhZC9BZHVsdG9zLmNzdi5jc3Yuemlw",
            "file_name": "ENSANUT-Adultos-Datos-2000.zip"
        },
        {
            "url": "https://ensanut.insp.mx/encuestas/ensanut2006/descargas.php",
            "data": "ArchIdMDEtQ29tcG9uZW50ZSBkZSBTQUxVRC8wMy1DdWVzdGlvbmFyaW8gaW5kaXZpZHVhbDogQWR1bHRvcyBkZSAyMCBvIG3DoXMgYcOxb3MgZGUgZWRhZC9BZHVsdG9zLmNzdi5jc3Yuemlw",
            "file_name": "ENSANUT-Adultos-Datos-2006.zip"
        },
        {
            "url": "https://ensanut.insp.mx/encuestas/ensanut2012/descargas.php",
            "data": "ArchIdMDEtQ29tcG9uZW50ZSBkZSBTQUxVRC8wMi1DdWVzdGlvbmFyaW8gaW5kaXZpZHVhbDogQWR1bHRvcyBkZSAyMCBvIG3DoXMgYcOxb3MgZGUgZWRhZC9BZHVsdG9zLmNzdi5jc3Yuemlw",
            "file_name": "ENSANUT-Adultos-Datos-2012.zip"
        },
        {
            "url": "https://ensanut.insp.mx/encuestas/ensanut2016/descargas.php",
            "data": "ArchIdMDEtQ29tcG9uZW50ZSBkZSBTQUxVRC8wMy1DdWVzdGlvbmFyaW8gZGUgQWR1bHRvcyBkZSAyMCBBw7FvcyBvIE3DoXMvMDEtQ3Vlc3Rpb25hcmlvIGRlIEFkdWx0b3MgZGUgMjAgQcOxb3MgbyBNw6FzIC0gRW5mZXJtZWRhZGVzIENyw7NuaWNhcy9hZHVsX2Nyb25pY2FzLmNzdi5jc3Yuemlw",
            "file_name": "ENSANUT-Adultos-Datos-2016.zip"
        },
        {
            "url": "https://ensanut.insp.mx/encuestas/ensanut2018/descargas.php",
            "data": "ArchIdMDEtQ29tcG9uZW50ZSBkZSBTQUxVRC8wMi1DdWVzdGlvbmFyaW8gZGUgU2FsdWQgZGUgQWR1bHRvcyAoMjAgYcOxb3MgbyBtw6FzKS9DU19BRFVMVE9TLmNzdi5jc3Yuemlw",
            "file_name": "ENSANUT-Adultos-Datos-2018.zip"
        },
        {
            "url": "https://ensanut.insp.mx/encuestas/ensanutcontinua2020/descargas.php",
            "data": "ArchIdMDEtQ29tcG9uZW50ZSBkZSBTQUxVRC8wMi1DdWVzdGlvbmFyaW8gZGUgU2FsdWQgZGUgQWR1bHRvcyAoMjAgYcOxb3MgbyBtw6FzKS9hZHVsdG9zX3ZhY190YWJfZW5zYW51dDIwMjBfdy5jc3YuY3N2LnppcA==",
            "file_name": "ENSANUT-Adultos-Datos-2020.zip"
        },
        {
            "url": "https://ensanut.insp.mx/encuestas/ensanutcontinua2021/descargas.php",
            "data": "ArchIdMDEtQ29tcG9uZW50ZSBkZSBTQUxVRC8wNC1DdWVzdGlvbmFyaW8gZGUgc2FsdWQgZGUgYWR1bHRvcyAoMjAgYcOxb3MgbyBtw6FzKS9lbnNhZHVsMjAyMV9lbnRyZWdhX3dfMTVfMTJfMjAyMS5jc3YuY3N2LnppcA==",
            "file_name": "ENSANUT-Adultos-Datos-2021.zip"
        },
        {
            "url": "https://ensanut.insp.mx/encuestas/ensanutcontinua2022/descargas.php",
            "data": "ArchIdMDEtQ29tcG9uZW50ZSBkZSBTQUxVRC8wNC1DdWVzdGlvbmFyaW8gZGUgc2FsdWQgZGUgYWR1bHRvcyAoMjAgYcOxb3MgbyBtw6FzKS9lbnNhZHVsMjAyMl9lbnRyZWdhX3cuY3N2LmNzdi56aXA=",
            "file_name": "ENSANUT-Adultos-Datos-2022.zip"
        },
        {
        "url": "https://ensanut.insp.mx/encuestas/ensanutcontinua2023/descargas.php",
        "data": "ArchIdMDEtQ29tcG9uZW50ZSBkZSBTQUxVRC8wNC1DdWVzdGlvbmFyaW8gZGUgc2FsdWQgZGUgYWR1bHRvcyAoMjAgYcOxb3MgbyBtw6FzKS9hZHVsdG9zX2Vuc2FudXQyMDIzX3dfbi5jc3YuY3N2LnppcA==",
        "file_name": "ENSANUT-Adultos-Datos-2023.zip"
        }
    ]
# Descargar catalogos para adolescentes
    for item in adolescentes_cat:
        descargar_archivo_xlsx(item["url"], item["data"], folder_adolescentes, item["file_name"])

# Descargar catalogos para adultos
    for item in adultos_cat:
        descargar_archivo_xlsx(item["url"], item["data"], folder_adultos, item["file_name"])
# Descargar datos para adolescentes
    for item in adolescentes_data:
        descargar_archivo_zip(item["url"], item["data"], 'ENSANUT-DATOS/DATOS ADOLESCENTES', item["file_name"], 'DATOS ADOLESCENTES')

# Descargar datos para adultos
    for item in adultos_data:
        descargar_archivo_zip(item["url"], item["data"], 'ENSANUT-DATOS/DATOS ADULTOS', item["file_name"], 'DATOS ADULTOS')
    if os.path.exists('ENSANUT-DATOS') and os.path.isdir('ENSANUT-DATOS'):
    # Borra la carpeta y su contenido
        shutil.rmtree('ENSANUT-DATOS')
        print(f'La carpeta "ENSANUT-DATOS" ha sido borrada.')
    else:
        print(f'La carpeta "ENSANUT-DATOS" no existe.')
    
if __name__ == "__main__":
    main()
