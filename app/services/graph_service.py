import matplotlib.pyplot as plt
from datetime import datetime

class GraphService:

    @staticmethod
    def plot_language_distribution(repos: list, show: bool = False, out_file: str = None):
        """Mostra e salva a distribuição das linguagens mais usadas."""
        languages = [repo['language'] for repo in repos if repo['language']]
        
        if not languages:
            print("Nenhuma linguagem encontrada nos repositórios.")
            return
        
        from collections import Counter
        language_counts = Counter(languages)
        top_languages = dict(language_counts.most_common(10))

        plt.figure(figsize=(10, 6))
        plt.bar(top_languages.keys(), top_languages.values(), color='skyblue')
        plt.title("Top 10 Linguagens nos Repositórios Populares")
        plt.xlabel("Linguagem")
        plt.ylabel("Quantidade de Repositórios")
        plt.xticks(rotation=45)
        plt.tight_layout()

        if not out_file:
            out_file = f"languages_distribution_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        plt.savefig(out_file, dpi=300)
        if show:
            plt.show()
        plt.close()

    @staticmethod
    def plot_repo_age_distribution(repos: list, show: bool = False, out_file: str = None):
        """Mostra e salva a idade dos repositórios em anos."""
        ages = []
        for repo in repos:
            if repo.get('created_at'):
                created_at = datetime.fromisoformat(repo['created_at'].replace('Z','+00:00'))
                age = (datetime.now(datetime.utcnow().astimezone().tzinfo) - created_at).days / 365
                ages.append(age)

        if not ages:
            print("Nenhuma data de criação válida encontrada.")
            return

        plt.figure(figsize=(10, 6))
        plt.hist(ages, bins=20, color='orange', edgecolor='black')
        plt.title("Distribuição da Idade dos Repositórios")
        plt.xlabel("Idade (anos)")
        plt.ylabel("Quantidade de Repositórios")
        plt.tight_layout()

        if not out_file:
            out_file = f"repos_age_distribution_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        plt.savefig(out_file, dpi=300)
        if show:
            plt.show()
        plt.close()

    @staticmethod
    def plot_stars_distribution(repos: list, show: bool = False, out_file: str = None):
        """Mostra e salva a distribuição de estrelas nos repositórios."""
        stars = [repo['stargazers_count'] for repo in repos if 'stargazers_count' in repo]

        if not stars:
            print("Nenhuma informação de stars encontrada.")
            return

        plt.figure(figsize=(10, 6))
        plt.hist(stars, bins=30, color='green', edgecolor='black')
        plt.title("Distribuição de Estrelas nos Repositórios")
        plt.xlabel("Quantidade de Stars")
        plt.ylabel("Número de Repositórios")
        plt.tight_layout()

        if not out_file:
            out_file = f"stars_distribution_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        plt.savefig(out_file, dpi=300)
        if show:
            plt.show()
        plt.close()

class GraphServiceDetails:

    @staticmethod
    def plot_pull_requests_distribution(repos: list):
        prs = [repo["pullRequests"]["totalCount"] for repo in repos]
        plt.figure(figsize=(10,6))
        plt.hist(prs, bins=30, color="blue", edgecolor="black")
        plt.title("Distribuição de Pull Requests Aceitas")
        plt.xlabel("Quantidade de PRs Aceitas")
        plt.ylabel("Número de Repositórios")
        plt.tight_layout()
        plt.savefig("pull_requests_distribution.png", dpi=300)
        plt.close()

    @staticmethod
    def plot_releases_distribution(repos: list):
        releases = [repo["releases"]["totalCount"] for repo in repos]
        plt.figure(figsize=(10,6))
        plt.hist(releases, bins=20, color="purple", edgecolor="black")
        plt.title("Distribuição de Releases")
        plt.xlabel("Quantidade de Releases")
        plt.ylabel("Número de Repositórios")
        plt.tight_layout()
        plt.savefig("releases_distribution.png", dpi=300)
        plt.close()

    @staticmethod
    def plot_closed_issues_ratio(repos: list):
        ratios = []
        for repo in repos:
            total = repo["openIssues"]["totalCount"] + repo["closedIssues"]["totalCount"]
            if total > 0:
                ratios.append(repo["closedIssues"]["totalCount"] / total)

        plt.figure(figsize=(10,6))
        plt.hist(ratios, bins=20, color="green", edgecolor="black")
        plt.title("Proporção de Issues Fechadas")
        plt.xlabel("Percentual de Issues Fechadas")
        plt.ylabel("Número de Repositórios")
        plt.tight_layout()
        plt.savefig("closed_issues_ratio.png", dpi=300)
        plt.close()