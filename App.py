import asyncio
from app.drivers.api_requester import ApiRequester

async def main():
    keyword = "python"
    num_repos = 1000

    api = ApiRequester()
    repos = await api.get_top1000_git_repositories(keyword, num_repos)
    if repos:
        print(f"Total de repositórios coletados: {len(repos)}")
    else:
        print("Erro ao coletar os repositórios.")

    repos100 = await api.get_top100_git_repositories()
    print(f"Total de 100 repositórios coletados: {len(repos100)}")

if __name__ == "__main__":
    asyncio.run(main())
