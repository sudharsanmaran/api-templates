import json
from fastapi import HTTPException
import httpx

from src.jira.constants import (
    BASE_URL_FOR_JIRA_API,
)


class JiraClient:
    async def _make_request(self, method, url, headers=None, data=None):
        async with httpx.AsyncClient() as client:
            try:
                response = await client.request(
                    method,
                    url,
                    headers=headers,
                    data=data,
                    timeout=60,
                )

                response.raise_for_status()
                return response.json()
            except httpx.HTTPStatusError as err:
                details = json.loads(err.response.text)
                raise HTTPException(
                    status_code=err.response.status_code,
                    detail=details,
                )

    async def create_project(
        self,
        access_token: str,
        resource_id: str,
        description: str,
        key: str,
        name: str,
        assigneeType: str,
        projectTemplateKey: str,
        projectTypeKey: str,
        leadAccountId: str,
    ):
        access_token = "eyJraWQiOiJmZTM2ZThkMzZjMTA2N2RjYTgyNTg5MmEiLCJhbGciOiJSUzI1NiJ9.eyJqdGkiOiJlZDUxZjkxMy05MTFmLTQ2Y2YtOWU5OC1lZDBmMTUwMGZjZjQiLCJzdWIiOiI3MTIwMjA6YWFhNDhiZjItODNmZi00ZTQ0LTgzNWUtNzBmOGFiZTAwNDdhIiwibmJmIjoxNjk4OTI4OTQ2LCJpc3MiOiJodHRwczovL2F1dGguYXRsYXNzaWFuLmNvbSIsImlhdCI6MTY5ODkyODk0NiwiZXhwIjoxNjk4OTMyNTQ2LCJhdWQiOiJxRmV0eGZIQ21INnlmOHBiZlN5ZzNFMzZkYmV4eXRDTyIsImh0dHBzOi8vaWQuYXRsYXNzaWFuLmNvbS91anQiOiJlNmM1YWZkZi1mMWI2LTQxNWEtYTk1Yy02ZTgzYjYzMDQ2OTciLCJodHRwczovL2F0bGFzc2lhbi5jb20vc3lzdGVtQWNjb3VudEVtYWlsIjoiZGVkYmM4ZDMtMDdmMS00ZTExLTk0NmQtMmMzYmFhMzgwMWMwQGNvbm5lY3QuYXRsYXNzaWFuLmNvbSIsImh0dHBzOi8vaWQuYXRsYXNzaWFuLmNvbS9hdGxfdG9rZW5fdHlwZSI6IkFDQ0VTUyIsImh0dHBzOi8vYXRsYXNzaWFuLmNvbS9maXJzdFBhcnR5IjpmYWxzZSwiaHR0cHM6Ly9hdGxhc3NpYW4uY29tL3ZlcmlmaWVkIjp0cnVlLCJjbGllbnRfaWQiOiJxRmV0eGZIQ21INnlmOHBiZlN5ZzNFMzZkYmV4eXRDTyIsImh0dHBzOi8vYXRsYXNzaWFuLmNvbS9zeXN0ZW1BY2NvdW50SWQiOiI3MTIwMjA6ZGE3NjkzYjYtNDI1Ny00OTdlLWI2MjQtOGU2NDFjZjExM2ViIiwidmVyaWZpZWQiOiJ0cnVlIiwiaHR0cHM6Ly9pZC5hdGxhc3NpYW4uY29tL3Byb2Nlc3NSZWdpb24iOiJ1cy13ZXN0LTIiLCJodHRwczovL2F0bGFzc2lhbi5jb20vZW1haWxEb21haW4iOiJnbWFpbC5jb20iLCJodHRwczovL2F0bGFzc2lhbi5jb20vM2xvIjp0cnVlLCJodHRwczovL2F0bGFzc2lhbi5jb20vb2F1dGhDbGllbnRJZCI6InFGZXR4ZkhDbUg2eWY4cGJmU3lnM0UzNmRiZXh5dENPIiwiaHR0cHM6Ly9pZC5hdGxhc3NpYW4uY29tL3ZlcmlmaWVkIjp0cnVlLCJzY29wZSI6Im1hbmFnZTpqaXJhLWNvbmZpZ3VyYXRpb24gbWFuYWdlOmppcmEtcHJvamVjdCBvZmZsaW5lX2FjY2VzcyByZWFkOmppcmEtdXNlciByZWFkOmppcmEtd29yayB3cml0ZTpqaXJhLXdvcmsiLCJodHRwczovL2lkLmF0bGFzc2lhbi5jb20vcmVmcmVzaF9jaGFpbl9pZCI6InFGZXR4ZkhDbUg2eWY4cGJmU3lnM0UzNmRiZXh5dENPLTcxMjAyMDphYWE0OGJmMi04M2ZmLTRlNDQtODM1ZS03MGY4YWJlMDA0N2EtMWIyOTlmY2ItMTM5NC00OThkLThhMzItMjRiZDM2MzhlYTFmIiwiaHR0cHM6Ly9pZC5hdGxhc3NpYW4uY29tL3Nlc3Npb25faWQiOiI2N2VlOTNlOS1jMzk5LTRiZGEtOWVjNC05MGRlZWU5MWNjNTMiLCJodHRwczovL2F0bGFzc2lhbi5jb20vc3lzdGVtQWNjb3VudEVtYWlsRG9tYWluIjoiY29ubmVjdC5hdGxhc3NpYW4uY29tIn0.vO5PppWN905mYIYoC4j2K8_UATaz6EyrS_S2N1bZ2WRokq8xhpR1a5GR9R3gBxIC5oL8h9RwYUKkEAGLpNTVohZhVVcaZ41Zo2H3mihqluEC2KbDuaPAqmsW_D3j45Mwki3uqoraxVKTUdUGBOJU5zUtftqvfIbO40Lw5WZ3NPiLZQy98Pjx13ZF5pHiTUkp-742qCT5CR7Wflmz6MWUGszLlLbNuYyjc2GgS3ZCu21w5OeWjl6QAtCml4nuP0rsEdM8Idwu4evRejJz2HtLyAWcCciXqv4YY2FxBzMcDJg62dfIu6XlYwPtKE1_jh1auk8MsVPs_X7O0vRVRKNn-w"
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }
        data = {
            "assigneeType": assigneeType,
            "description": description,
            "key": key,
            "name": name,
            "projectTemplateKey": projectTemplateKey,
            "projectTypeKey": projectTypeKey,
            "leadAccountId": leadAccountId,
        }

        response = await self._make_request(
            "POST",
            BASE_URL_FOR_JIRA_API.format(resource_id) + "rest/api/3/project",
            headers=headers,
            data=json.dumps(data),
        )
        return response

    async def get_Jira_user(self, token):
        headers = {"Authorization": f"Bearer {token}"}
        response = await self._make_request(
            "GET",
            "https://api.atlassian.com/me",
            headers=headers,
        )

        return response

    async def get_user_accessible_resources(self, token):
        headers = {"Authorization": f"Bearer {token}"}
        response = await self._make_request(
            "GET",
            "https://api.atlassian.com/oauth/token/accessible-resources",
            headers=headers,
        )
        return response

    async def get_all_project(self, token, resource_id):
        headers = {"Authorization": f"Bearer {token}"}
        response = await self._make_request(
            "GET",
            f"https://api.atlassian.com/ex/jira/{resource_id}/rest/api/3/project/search",
            headers=headers,
        )
        return response


class Client(JiraClient):
    pass
