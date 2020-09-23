# Projeto de Reatímetro
_Desenvolvimento de um sistema de monitoramento da operação de reator nuclear por meio do cálculo de cinética pontual inversa para medição da reatividade em tempo real. Pesquisa financiada pelo CNPQ, feita em colaboração com o IEN (Instituto de Engenharia Nuclear)._
## Arquivos:


* ./imgs: Pasta contendo as imagens para conteúdo explicativo, principalmente para o arquivo README.md do github.

* signal.csv: Arquivo excel que contém a tabela de valores colhidos diretamente da potência do reator. Lembrando que está em escala log. 

* data.csv: Arquivo que conterá as diversas colunas necessárias para a operação completa.

* main.py: se encarrega de puxar todas as outras funções dos outros programas e rodá-los sequencialmente.

* logtolin.py: Faz a conversão do sinal bruto do reator logarítimico para uma escala linear.

* smoother.py: Suaviza a curva de potência do reator para trabalharmos as derivadas e integrais de forma mais precisa.

* historical.py: Trabalha os dados e faz o histórico de potência ponto a ponto.

* reactivity.py: Em última instância, gera os valores de reatividade ponto a ponto e plota o resultado final.