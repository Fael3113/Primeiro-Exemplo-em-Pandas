#Exemplo de Manipulação de dados usando Python Pandas 
# 6/02/2023 
# Autor:Poyatos e galera
import pandas as pd

combustiveis_df = pd.read_csv("precos-semestrais-ca-2022-01.csv", on_bad_lines='skip')