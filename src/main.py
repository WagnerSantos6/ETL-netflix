import pandas as pd
import os
import glob

# caminho para ler os arquivos
path = 'src\\data\\raw'

# lista os arquivos
docs = glob.glob(os.path.join(path , '*.xlsx'))

if not docs:
    print("Nenhum arquivo encontrado")
else:
    # criando um dataframe para armazenar uma tabela na memória e guardar o conteúdo dos arquivos
    df = []

    # percorrer a lista de arquivos para ler
    for doc in docs:
        try:
            # dataframe temporário para armazenar
            dft = pd.read_excel(doc)

        except Exception as e:
           print(f"Não foi possível ler o arquivo {doc}: {e}")

