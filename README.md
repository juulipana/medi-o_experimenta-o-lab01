# Medição e Experimentação de Software

## Professor 
- Danilo de Quadros Maia Filho

## Alunos
- Juliana Parreiras Guimarães da Cunha
- Pedro Henrique Marques de Oliveira

## Laboratório 01

Neste laboratório, estudamos as principais características de sistemas populares open-source. O objetivo é analisar como esses projetos são desenvolvidos, com que frequência recebem contribuições, com que frequência lançam novas versões, entre outras características.  

## Metodologia

Para realizar o trabalho, vamos seguir os seguintes passos:

- Definição das Questões de Pesquisa e Hipóteses Iniciais – Identificamos perguntas sobre maturidade, contribuições, atualizações, releases, linguagens e issues nos repositórios populares.
- Coleta de Dados – Utilizamos a API GraphQL para uma amostra inicial de 100 repositórios e a API REST do GitHub para coletar dados dos 100 e 1.000 repositórios mais populares relacionados à palavra-chave "popular".
- Atributos Analisados – Extraímos informações relevantes para responder às questões.
- Tratamento e Análise de Dados – Usamos Python e a biblioteca Pandas para organizar os dados, calcular métricas e gerar gráficos que possibilitem testar as hipóteses.
- Conclusão Parcial e Planejamento Futuro – Identificamos quais perguntas podem ser respondidas com os dados atuais e quais exigem coleta adicional para estudos futuros.

É importante ressaltar que, apesar de em geral termos usados os mil primeiros repositórios como base, para os gráficos de releases, issues fechadas e pull requests, usamos os 100 primeiros para pegar com mais detalhes as informações.

## Sprint 01  
Consulta GraphQL para 100 repositórios (com dados/métricas necessários para responder às RQs) + requisição automática.  

## Sprint 02  
### Primeira versão do relatório  
Nessa etapa, coletamos os dados dos mil repositórios mais populares relacionados à palavra-chave "popular" no GitHub. Para isso, utilizamos a API REST do GitHub e analisamos os seguintes atributos:  

- Data de criação do repositório (`created_at`)  
- Tempo desde a última atualização (`updated_at`)  
- Linguagem principal (`language`)  
- Número de estrelas (`stars`)  
- Issues abertas (`open_issues`)  

Com esses dados, concluímos a fase de coleta e elaboramos as primeiras hipóteses para responder às questões de pesquisa. O próximo passo é calcular métricas e gerar gráficos que confirmem ou refutem as hipóteses a seguir:  

---

### Questões de Pesquisa (RQs) e Hipóteses  

**RQ 01.** Sistemas populares são maduros/antigos?  
*Hipótese:* Acreditamos que a maioria será de projetos mais novos, ligados a tecnologias recentes.  

**RQ 02.** Sistemas populares recebem muita contribuição externa?  
*Hipótese:* Sim, pois projetos open-source tendem a crescer mais rápido com a ajuda da comunidade.  

**RQ 03.** Sistemas populares lançam releases com frequência?  
*Hipótese:* Não, já que muitos projetos open-source não publicam releases com tanta frequência.  

**RQ 04.** Sistemas populares são atualizados com frequência?  
*Hipótese:* Não, pois geralmente evitam atualizações constantes para não atrapalhar o desenvolvimento da comunidade.  

**RQ 05.** Sistemas populares são escritos nas linguagens mais populares?  
*Hipótese:* Sim, porque tecnologias mais conhecidas costumam interessar mais desenvolvedores.  

**RQ 06.** Sistemas populares possuem um alto percentual de issues fechadas?  
*Hipótese:* Sim, já que tendem a ser sistemas mais consolidados.  

---

### Etapa final: Análise de Gráficos e Conclusões
Para esta etapa, optamos por utilizar a biblioteca 'Pandas' de python para gerar os gráficos. 

## Gráficos Gerados

<img width="3000" height="1800" alt="languages_distribution_20250827_214514" src="https://github.com/user-attachments/assets/e1584b4e-956e-42fb-823c-459c624984b5" />

<img width="3000" height="1800" alt="repos_age_distribution_20250827_214515" src="https://github.com/user-attachments/assets/93cef1bc-b89c-44df-9176-c8483d4fb33e" />

<img width="3000" height="1800" alt="stars_distribution_20250827_214515" src="https://github.com/user-attachments/assets/17a8efca-90cd-4f3c-80eb-deb7aaf8c4fd" />

<img width="3000" height="1800" alt="image" src="https://github.com/user-attachments/assets/f3fe6417-ec6e-48c0-8cc0-d3cf7518670a" />

<img width="3000" height="1800" alt="image" src="https://github.com/user-attachments/assets/972cf7e4-7170-493b-8080-ae6ad90f656d" />

<img width="3000" height="1800" alt="image" src="https://github.com/user-attachments/assets/fa65d731-4eef-4268-b9d3-2a3c16631947" />

---

## Conclusão

**RQ 01.** Sistemas populares são maduros/antigos?
*Conclusão:* Não. O gráfico de idade mostra que a maior parte dos repositórios populares está em uma fase de maturidade média, com a maioria tendo entre 2 e 10 anos. Isso sugere que a popularidade está mais relacionada a repositórios já bem consolidados.

**RQ 02.** Sistemas populares recebem muita contribuição extrepositórios populares, é possível ver que os sistemas populares recebem e aceitam muitas contribuições externas. A média de Pull Requests Fechados é significativamente mais alta do que a de Pull Requests Abertos, mostrando que um grande volume de código proposto por colaboradores externos é revisado e integrado.

**RQ 03.** Sistemas populares lançam releases com frequência?
*Conclusão:* Com base no gráfico de releases, que indica uma quantidade bastante alta de releases nos primeiros casos e, em comparação com a outra metade do gráfico que exibe uma média bem baixa, podemos concluir que sistemas populares lançam releases com uma frequência média.

**RQ 04.** Sistemas populares são atualizados com frequência?
Conclusão: O gráfico de releases mostra que a maioria dos repositórios tem poucas releases. No entanto, ele também exibe uma pequena quantidade de repositórios que possuem um número bem alto de releases (mais de 400). O fato de existirem projetos com essa frequência de lançamentos pode nos mostrar que os projetos mais ativos e populares tendem a ter um alto número de releases.

**RQ 05.** Sistemas populares são escritos nas linguagens mais populares?
*Conclusão:* Sim. O gráfico de de linguagens populares mostra que Python, JavaScript e Java são as linguagens predominantes nos repositórios da amostra. Estas são classificadas entre as linguagens de programação mais populares do mundo, validando a ideia de que a popularidade de um projeto está ligada à popularidade da sua linguagem.

**RQ 06.** Sistemas populares possuem um alto percentual de issues fechadas?
*Conclusão:* Sim. O gráfico de issues mostra que, para repositórios populares, o número de issues fechadas é proporcionalmente alto em relação ao número de issues abertas. Isso mostra que a maioria das issues que surgem nesses repositórios acaba sendo resolvida e fechada.

### Agradecimentos e Próximos Passos

Agradecemos ao professor Danilo pelo apoio e disponibilidade durante o laboratório.
