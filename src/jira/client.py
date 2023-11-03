import json
from fastapi import HTTPException
import httpx
from src.jira.utils import get_id_from


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
        projectTypeKey: str,
        projectTemplateKey: str,
        assigneeType: str,
        leadAccountId: str,
    ):
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
            BASE_URL_FOR_JIRA_API.format(get_id_from(resource_id)) + "rest/api/3/project",
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
