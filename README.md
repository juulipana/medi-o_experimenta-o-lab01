# Medição e Experimentação de Software

## Laboratório 01

Neste laboratório, vamos estudar as principais características de sistemas populares  open-source. Dessa forma, vamos analisar como eles são desenvolvidos, com que  frequência recebem contribuição externa, com qual frequência lançam releases, entre  outras características.

## Sprint 01 
Consulta graphql para 100 repositórios (com todos os dados/métricas necessários para responder as RQs) + requisição automática

## Sprint 02
# Primeira versão do gelatório
Nessa primeira etapa, coletamos os dados dos primeiros mil repositórios mais populares relacionados à palavra-chave 'popular' no GitHub. Fizemos uma consulta para a API REST do GitHub, procurando analisar os seguintes dados:

* Criação do repositório (created_at)
* Tempo desde a última atualização (updated_at)
* Linguagem principal (language)
* Número de estrelas (stars)
* Issues abertas (open_issues)

Com isso, concluímos a coleta de dados e elaboramos as primeiras hipóteses que servirão para responder aos requisitos. O próximo passo será calcular métricas e gerar gráficos que vão ou não de acordo com as propostas a seguir:

**RQ 01.** Sistemas populares são maduros/antigos?
* Hipótese inicial: Acreditamos que a maioria dos sistemas populares serão novos e que abordam tecnologias recentes no campo da tecnologia.

**RQ 02.** Sistemas populares recebem muita contribuição externa?
* Hipótese inicial: Acreditamos que sim, pois sistemas OpenSource costumam crescer mais rapidamente devido a contribuições da comunidade.

**RQ 03.** Sistemas populares lançam releases com frequência?
* Hipótese inicial: Não, pois sistemas OpenSorce não costumam lançar muitas releases.

**RQ 04.** Sistemas populares são atualizados com frequência?
* Hipótese inicial: Não, pois sistemas OpenSorce não costumam lançar muitas atualizações para não desestabilizar a comunidade em torno do sistema..

**RQ 05.** Sistemas populares são escritos nas linguagens mais populares?
* Hipótese inicial: Sim, pois tecnologias de ponta costumam ser mais populares entre o público de tecnologia/desenvolvedores.

**RQ 06.** Sistemas populares possuem um alto percentual de issues fechadas?
* Hipótese inicial: Sim, pois são sistemas prontos.
