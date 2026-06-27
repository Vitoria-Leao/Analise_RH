## importando bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

## lendo o arquivo csv com dados do rh em um dataframe
df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv", header=0)

## criando um histograma de idades dos funcionarios
df['Age'].hist(bins=10,color='gray',edgecolor='black')

## definindo titulo e rotulos dos eixos
plt.title("Distribuição de Idade dos Funcionários - RH",fontweight='bold')
plt.xlabel("Idade",fontweight='bold')
plt.ylabel("Frequência",fontweight='bold')

## salvando o histograma em um arquivo png
plt.savefig('histAge.png', dpi=300, bbox_inches='tight')
plt.close()

## criando um grafico de densidade KDE das idades dos funcionarios
sns.kdeplot(df['Age'], fill=True,color = 'gray')

## definindo titulo e rotulos dos eixos
plt.title("Plot KDE - Idade dos Funcionários",fontweight='bold')
plt.xlabel("Idade",fontweight='bold')
plt.ylabel("Densidade",fontweight='bold')

## salvando o KDE em um arquivo png
plt.savefig('KDEAge.png', dpi=300, bbox_inches='tight')
plt.close()

## criando um boxplot do salario mensal dos funcionarios por departaamento
sns.boxplot(data=df, x="Department", y="MonthlyIncome", palette="Greys")

## definindo titulo e rotulos dos eixos
plt.title("Boxplot - Salário Mensal dos Funcionários",fontweight='bold')
plt.xlabel("Departamento",fontweight='bold')
plt.ylabel("Salário Mensal",fontweight='bold')

## salvando o boxplot em um arquivo png
plt.savefig('boxplotIncome.png', dpi=300, bbox_inches='tight')
plt.close()

## analise de rotatividade de funcionarios
## criando uma coluna binaria correspondendo a rotatividade de funcionarios
df['Attrition_binary'] = [1 if x == 'Yes' else 0 for x in df['Attrition']]

## criando uma matriz de correlacao entre a coluna binaria de rotatividade criada e fatores possivelmente relacionados (idade, salario, tempo de servico)
cor = df[['Attrition_binary','MonthlyIncome','YearsAtCompany','Age','TotalWorkingYears']].corr()

## criando um heatmap da matriz de correlacao 
plt.figure(figsize=(8, 6))
sns.heatmap(cor, annot=True, cmap='coolwarm', fmt=".2f", vmin=-1, vmax=1)

## definindo titulo e rotacionando os rotulos do eixo x
plt.title('Correlação - Fatores Relacionados à Rotatividade de Funcionários', fontweight='bold')
plt.xticks(rotation=45)

## salvando o heatmap em um arquivo png
plt.savefig('heatmapCorr.png', dpi=300, bbox_inches='tight')
plt.close()

## comparacao entre funcionarios desligados e ativos
## separando o df em dois - um para funcionarios ativos e outro para desligados
func_desligados = df[df['Attrition']=='Yes']
func_ativos = df[df['Attrition']=='No'] 
## calculando a media de idade, salario e tempo de empresa para os dois novos dfs
## e arredondando os resultados 
idade_desligados = round(func_desligados['Age'].mean(),2)
idade_ativos = round(func_ativos['Age'].mean(),2)
salario_desligados = round(func_desligados['MonthlyIncome'].mean(),2)
salario_ativos = round(func_ativos['MonthlyIncome'].mean(),2)
tempo_empresa_desligados = round(func_desligados['YearsAtCompany'].mean(),2)
tempo_empresa_ativos = round(func_ativos['YearsAtCompany'].mean(),2)

## criando vetores com os resultados calculados para funcionarios ativos e desligados
Desligados = [idade_desligados, salario_desligados, tempo_empresa_desligados]
Ativos = [idade_ativos, salario_ativos, tempo_empresa_ativos]

## adicionando os vetores em um novo dataframe de comparacao
comparacao = pd.DataFrame({
    'Desligados': Desligados,
    'Ativos': Ativos
},index=['Idade', 'Salário', 'Tempo na Empresa'])

## exibindo o dataframe de comparacao
print(comparacao)

## salvando o dataframe em um arquivo csv
comparacao.to_csv('Comparacao_Desligados_Ativos.csv',index=True)