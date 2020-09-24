# Pequeno script para gerar o meu arquivo signal.csv o mais limpo possivel

import csv
path = "/home/lobo/PycharmProjects/Projeto_Reatimetro/historico_linear_versao5ABRIL2020_01.csv"

with open(path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  #Omitindo os titulos dessa tabela, para substituir na nova

    with open("signal.csv", 'w') as new_file:

        csv_writer = csv.writer(new_file)

        csv_writer.writerow(["time", "signal"])
        for line in csv_reader:

            csv_writer.writerow(line[:2])

# Já temos nosso arquivo gerado. Agora, vamos plotá-lo para ver a sua carinha.
from matplotlib import pyplot as plt 
from matplotlib import style
import numpy as np 
import pandas as pd

print('Importei as bibliotecas')

#Abrindo agora para plotar:
data = pd.read_csv('signal.csv', encoding='utf-8').fillna(0)

#Explicitando o eixo x e y e plotando seus dados.
x = data['time'].iloc[:].values
y = data['signal'].iloc[:].values

print(x)
print(y)


plt.plot(x,y)
plt.title('Brute signal from reactor')
plt.xlabel('time (s)')
plt.ylabel('power signal (mV)')
plt.show()