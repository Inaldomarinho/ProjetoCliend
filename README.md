# ProjetoCliend
Repositório destinado ao programa desenvolvido sobre encomenda para a clinica CLIEND que se localiza em Natal-RN.

O programa facilita o trabalho de um bioquímico auxiliando na produção de um hemograma completo do paciente a partir poucos dados, realizando todos os cálculos necessários para achar os demais dados e imprimir em formato PDF em uma sub pasta do programa chamada Exames. Nessa pasta o arquivo é salvo como datanomedopaciente.PDF.

O programa foi desenvolvido em PYQT e recebe como entrada o nome do paciente, nome do medico, posto de coleta, data e hora. Além disso o programa para calcular a serie vermelha (hemacias, hemoglobina, VCM, HCM, CHCM) recebe como entrada o valor do hematocrito. Já para calcular a serie branca (leucocitos, mielocitos, metamielocitos, bastoes, segmentados, eosinofilos, basofilos, linfocitos e monocitos) o programa recebe como entrada o valor relativo dos mesmo e calcula o valor absoluto. O programa também recebe como entrada a contagem de plaquetas.

OBS: Por motivo de segurança o programa não gera os valores absolutos da serie branca se o somatório dos valores relativos forem diferente de 100.

O arquivo Mainwindow.ui foi o arquivo utilizado para criar o desing do programa. O arquivo cliend.py consiste no codigo do programa.

Abaixo segue imagens do programa sendo utilizado e o link para o resultado em PDF do exame teste gerado por ele.

Imagem do programa logo apos ser aberto:
![Programa](Images/Programa.png)

Imagem do programa preenchido com entradas:
![Programa com entradas](Images/ProgramaComEntradas.png)

Link para o exame em PDF gerado a partir das entradas da imagem anterior: 
![Exame](https://github.com/Inaldomarinho/ProjetoCliend/blob/master/Exames/24.07.18_Nome%20de%20Teste%20Aleatorio.pdf)


