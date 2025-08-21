import csv
from datetime import datetime

import requests


class ApiRequester:

    @staticmethod
    async def get_top1000_git_repositories(keyword: str, num_repos: int = 1000):
        headers = {
            "Authorization": f"token "
        }

        base_url = "https://api.github.com/search/repositories"
        all_repos = []
        per_page = 100
        total_pages = (num_repos // per_page)

        try:
            for page in range(1, total_pages + 1):
                params = {
                    "q": keyword,
                    "sort": "stars",
                    "order": "desc",
                    "per_page": per_page,
                    "page": page
                }
                response = requests.get(base_url, headers=headers, params=params)
                response.raise_for_status()

                data = response.json()
                items = data.get("items", [])
                all_repos.extend(items)

            filename = f"repos_{keyword}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
            with open(filename, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow([
                    "name", "full_name", "stars", "language",
                    "created_at", "updated_at", "open_issues", "html_url"
                ])
                for repo in all_repos:
                    writer.writerow([
                        repo.get("name"),
                        repo.get("full_name"),
                        repo.get("stargazers_count"),
                        repo.get("language"),
                        repo.get("created_at"),
                        repo.get("updated_at"),
                        repo.get("open_issues_count"),
                        repo.get("html_url")
                    ])

            return all_repos

        except requests.RequestException as e:
            return None