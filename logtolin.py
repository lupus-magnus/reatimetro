import pandas as pd 
#O plano é ter três variáveis.
#um contador i: encarregado do loop pelas linhas
#um delta: encarregado de ver a variação
#entre o sinal atual e o anterior
#e um multiplicador n: pra se encarregar das
#mudanças de base quando delta for maior que um valor
#pré-estipulado.

df = pd.read_csv('signal.csv')

#Vou iterar por cada linha de sinal.
total_rows = len(df.signal)
#Inicializando meu contador:
i = 0
new_column = ['lin_signal']
n = 1 #multiplicador
while (i < (total_rows)):
    delta = 0
    if i > 1: #Só para excluir a exceção que ocorrerá no primeiro valor
        delta = df.signal[i] - df.signal[i-1]
    if (delta**2 > 300**2):
        n*=10
    new_value = n*df.signal[i]
    new_column.append(new_value)
    i+=1
print(new_column[0:1500])

#A partir daqui vou tentar olhar o gráfico para conferir se está tudo batendo.
import matplotlib.pyplot as plt

#Explicitando o eixo x e y e plotando seus dados.
x = df['time'].iloc[:].values
y = new_column[1:]

plt.plot(x,y)
plt.title('linearized signal')
plt.xlabel('time (s)')
plt.ylabel('linear power signal')
plt.show()
