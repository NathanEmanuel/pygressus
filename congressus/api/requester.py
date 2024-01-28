import requests
from enum import Enum

from api.base_client import BaseClient
from api.paginated_response import PaginatedResponse
from models.group_membership import GroupMembership
from models.member import Member
from models.webhook import ConceptualWebhook


class HTTPMethod(Enum):
    GET = 0
    POST = 1
    PUT = 2
    DELETE = 3


class Requester:
    """
    Intended as a base class for requester components. Can be instatiated but this
    generally should be limited to development- and testing environments.
    """

    def __init__(self, client: BaseClient) -> None:
        """
        Requires the client to be injected so the requester component can obtain the API domain and -key.
        """
        self.domain = client.get_domain()
        self.auth_header = {"Authorization": f"Bearer {client.get_key()}"}

    def authorized_request(
        self,
        path: str,
        method: HTTPMethod = HTTPMethod.GET,
        params: dict = dict(),
        payload: dict = dict(),
        headers: dict = dict(),
    ) -> dict:
        """
        Returns the response to an HTTP request.
        Throws error on bad status code.
        Path must start with a /
        """
        url = self.domain + path
        headers.update(self.auth_header)

        match method:
            case HTTPMethod.GET:
                response = requests.get(url, params=params, headers=headers)
            case HTTPMethod.POST:
                response = requests.post(url, json=payload, headers=headers)
            case HTTPMethod.DELETE:
                response = requests.delete(url, headers=headers)
                return response

            case _:
                raise ValueError("Unsupported HTTP method")

        response.raise_for_status()

        return response.json()


class MemberRequester(Requester):
    BASE_PATH = "/v30/members"

    def list(self, page=None, page_size=None, order=None) -> PaginatedResponse:
        path = self.BASE_PATH
        params = {"page": page, "page_size": page_size, "order": order}
        return PaginatedResponse(**self.authorized_request(path, params=params))

    def create():
        pass

    def retrieve(self, id: int) -> Member:
        path = self.BASE_PATH + f"/{id}"
        return Member(**self.authorized_request(path))

    def update():
        pass

    def delete():
        pass

    def search(self, term, page=None, page_size=None, order=None) -> PaginatedResponse:
        path = self.BASE_PATH + "/search"
        params = {"term": term, "page": page, "page_size": page_size, "order": order}
        return PaginatedResponse(**self.authorized_request(path, params=params))


class GroupMembershipRequester(Requester):
    BASE_PATH = "/v30/groups/memberships"

    def list(self, page=None, page_size=None, order=None) -> PaginatedResponse:
        params = {"page": page, "page_size": page_size, "order": order}
        return PaginatedResponse(**self.authorized_request(self.BASE_PATH, params=params))

    def create(self, gms: GroupMembership):
        pass

    def retrieve(self, id: int):
        pass

    def update(self, id: int, gms: GroupMembership):
        pass

    def delete(self, id: int):
        pass


class WebhookRequester(Requester):
    BASE_PATH = "/v30/webhooks"

    def list(self, page=None, page_size=None, order=None):
        path = self.BASE_PATH
        params = {"page": page, "page_size": page_size, "order": order}
        return PaginatedResponse(**self.authorized_request(path, params=params))

    def create(self, new: ConceptualWebhook):
        path = self.BASE_PATH
        payload = {
            "url": new.url,
            "headers": new.headers,
            "signal": str(new.signal),
            "technical_contact_email": new.technical_contact_email,
            "http_basic_auth_enabled": new.http_basic_auth_enabled,
        }
        headers = {"Content-Type": "application/json"}
        return self.authorized_request(path, method=HTTPMethod.POST, payload=payload, headers=headers)

    def retrieve(self):
        pass

    def update(self):
        pass

    def delete(self, id: int):
        path = f"{self.BASE_PATH}/{id}"
        return self.authorized_request(path, method=HTTPMethod.DELETE)

    def list_calls(self):
        pass
