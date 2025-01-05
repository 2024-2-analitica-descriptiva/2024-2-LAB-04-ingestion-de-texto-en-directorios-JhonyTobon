# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""
import os
import zipfile
import pandas as pd

zip_file_path = 'files/input.zip'
extract_to = 'files/'

os.makedirs (extract_to, exist_ok=True)

with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extract_to)

def pregunta_01():

    data = []

    directories = ['train', 'test']

    for directory in directories:
        for target in ['negative','positive','neutral']:
            target_path = os.path.join('files','input', directory, target)

            if not os.path.exists(target_path):
                print(f'El directorio {target_path} no existe.')
                continue

            for file_name in os.listdir(target_path):
                if file_name.endswith('.txt'):
                    file_path = os.path.join(target_path, file_name)


                    with open(file_path,'r', encoding='utf-8') as file:
                        content = file.read().strip()

                    data.append({
                        'phrase': content,  
                        'target': target,
                        'dataset': directory   
                    })

    df = pd.DataFrame(data)

    return df

df = pregunta_01()

output_dir = 'files/output'
os.makedirs(output_dir, exist_ok=True)
    
df_train = df[df['dataset'] == 'train']
df_test = df[df['dataset'] == 'test']

df_train = df_train.drop(columns=['dataset'])
df_test = df_test.drop(columns= ['dataset'])

df_train.to_csv(os.path.join(output_dir, 'train_dataset.csv'), index = False)
df_test.to_csv(os.path.join(output_dir, 'test_dataset.csv'), index = False)


"""
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * target: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """
