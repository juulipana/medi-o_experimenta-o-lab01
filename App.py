import asyncio
from app.drivers.api_requester import ApiRequester
from app.services.graph_service import GraphService

async def main():
    keyword = "popular"
    num_repos = 1000

    api = ApiRequester()
    repos = await api.get_top1000_git_repositories(keyword, num_repos)
    if repos:
        print(f"Total de repositórios coletados: {len(repos)}")

        GraphService.plot_language_distribution(repos)
        GraphService.plot_repo_age_distribution(repos)
        GraphService.plot_stars_distribution(repos)
    else:
        print("Erro ao coletar os repositórios.")

    repos100 = await api.get_top100_git_repositories()
    if repos100:
        print(f"Total de 100 repositórios coletados: {len(repos100)}")
    else:
        print("Erro ao coletar os 100 repositórios.")

if __name__ == "__main__":
    asyncio.run(main())
