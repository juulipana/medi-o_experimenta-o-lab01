import asyncio
import json

from app.drivers.api_requester import ApiRequester
from app.services.graph_service import GraphService, GraphServiceDetails


async def main():
    api = ApiRequester()

    repos = await api.get_top1000_git_repositories("popular", 1000)
    if not repos:
        print("Erro ao coletar os repositórios REST.")
        return

    print(f"Total de repositórios coletados (REST): {len(repos)}")

    GraphService.plot_language_distribution(repos)
    GraphService.plot_repo_age_distribution(repos)
    GraphService.plot_stars_distribution(repos)

    repos_details = []
    for repo in repos[:100]:
        try:
            owner, name = repo["full_name"].split("/")
            details = api.get_repo_details(owner, name)
            if details:
                repos_details.append(details)
        except Exception as e:
            print(f"Erro no repo {repo['full_name']}: {e}")

    print(f"Total de repositórios detalhados (GraphQL): {len(repos_details)}")

    with open("repos_details.json", "w", encoding="utf-8") as f:
        json.dump(repos_details, f, indent=2)

    if repos_details:
        GraphServiceDetails.plot_pull_requests_distribution(repos_details)
        GraphServiceDetails.plot_releases_distribution(repos_details)
        GraphServiceDetails.plot_closed_issues_ratio(repos_details)


if __name__ == "__main__":
    asyncio.run(main())
