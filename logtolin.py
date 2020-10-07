import pandas as pd 
#O plano e ter tres variaveis.
#um contador i: encarregado do loop pelas linhas
#um delta: encarregado de ver a variacao
#entre o sinal atual e o anterior
#e um multiplicador n: pra se encarregar das
#mudancas de base quando delta for maior que um valor
#pre-estipulado.

df = pd.read_csv('signal.csv')

#Vou iterar por cada linha de sinal.
total_rows = len(df.signal)
#Inicializando meu contador:
i = 0
new_column = ['lin_signal']
n = 10**(-6) #multiplicador
while (i < (total_rows)):
    delta = 0
    if i > 1: #So para excluir a excecao que ocorrera no primeiro valor
        delta = df.signal[i] - df.signal[i-1]
    if (delta**2 > 300**2):
        n*=10
    new_value = n*df.signal[i]
    new_column.append(new_value)
    i+=1
print(new_column[0:1500])

#A partir daqui vou tentar olhar o grafico para conferir se esta tudo batendo.
import matplotlib.pyplot as plt

#Explicitando o eixo x e y e plotando seus dados.
x = df['time'].iloc[:].values
y = new_column[1:]

plt.plot(x,y)
plt.title('linearized signal')
plt.xlabel('time (s)')
plt.ylabel('linear power signal')
plt.show()


#A partir daqui, estamos nos concentrando em armazenar nossos valores num arquivo chamado data.csv
df = pd.read_csv('signal.csv')
df.to_csv('data.csv', index=False)
df.head()

new_column_pd = pd.Series(new_column[1:])

df2 = pd.read_csv('data.csv')
df2['lin_signal'] = new_column_pd
df2.head()


df2.to_csv('data.csv', index=False)