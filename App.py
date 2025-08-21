import asyncio

from app.drivers.api_requester import ApiRequester


async def main():
    keyword = "python"
    num_repos = 1000
    repos = await ApiRequester.get_top1000_git_repositories(keyword, num_repos)
    if repos:
        print(f"Total de repositórios coletados: {repos}")
    else:
        print("Erro ao coletar os repositórios.")

if __name__ == "__main__":
    asyncio.run(main())
