
# Internal Imports
from app.client import (
    CompanyClient,
    CreateCompanyResponse,
    DeactivateCompanyResponse,
    ReactivateCompanyResponse,
)


class Company:
    """Company is a interface to interact with the CompanyClient without the need to know the gRPC details.

    :param address: The address of the gRPC server.
    """

    def __init__(self, address: str):
        self.address = address
        self.client = CompanyClient(self.address)

    def create(
        self,
        token: str,
        company_id: str,
        company_name: str,
        trade_name: str,
        legal_entity_registration: str
    ) -> CreateCompanyResponse:
        """Create a company. This method will call the CreateCompany RPC.

        :param token: The access token to authenticate the user.
        :param company_id: The ID of the company.
        :param company_name: The name of the company.
        :param trade_name: The trade name of the company.
        :param legal_entity_registration: The legal entity registration number of the company. Brazilian CNPJ.
        :return: The response from the CreateCompany RPC.
        """
        return self.client.create_company(
            token,
            company_id,
            company_name,
            trade_name,
            legal_entity_registration,
        )

    def deactivate(
        self,
        token: str,
        company_id: str,
        reason: str,
    ) -> DeactivateCompanyResponse:
        """Deactivate a company. This method will call the DeactivateCompany RPC.

        :param token: The access token to authenticate the user.
        :param company_id: The ID of the company.
        :param reason: The reason to deactivate the company.
        :return: The response from the DeactivateCompany RPC.
        """
        return self.client.deactivate_company(token, company_id, reason)

    def reactivate(
        self,
        token: str,
        company_id: str,
        reason: str
    ) -> ReactivateCompanyResponse:
        """Reactivate a company. This method will call the ReactivateCompany RPC.

        :param token: The access token to authenticate the user.
        :param company_id: The ID of the company.
        :param reason: The reason to reactivate the company.
        :return: The response from the ReactivateCompany RPC.
        """
        return self.client.reactivate_company(token, company_id, reason)
