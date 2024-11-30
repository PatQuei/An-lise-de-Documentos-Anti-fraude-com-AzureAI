from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from ultils.config import Config
import fields

def analize_credit_card(card_url):

        credential = AzureKeyCredential(Config.KEY)
        document_Client = DocumentIntelligenceClient(Config.ENDPOINT, credential)

        card_info = document_Client.begin_analyze_document(
            "prebuilt-creditCard", AnalyzeDocumentRequest(url_source=card_url))


        result = card_info.result()

        return {
                "card_name": fields.get('CardHolderName', {}).get('content'),
                "card_number": fields.get('CardNumber', {}).get('content'),
                "expired_date": fields.get('expirationDate', {}).get('content'),
                "bank_name": fields.get('CIssuingBank', {}).get('content'),
        }
   