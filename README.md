# Medição e Experimentação de Software

## Professor 
- Danilo de Quadros Maia Filho

## Alunos
- Juliana Parreiras Guimarães da Cunha
- Pedro Henrique Marques de Oliveira

## Laboratório 01

Neste laboratório, estudamos as principais características de sistemas populares open-source. O objetivo é analisar como esses projetos são desenvolvidos, com que frequência recebem contribuições, com que frequência lançam novas versões, entre outras características.  

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
