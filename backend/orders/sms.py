import logging
import africastalking
from minicommerce.settings import AT_USERNAME, AT_APIKEY

logger = logging.getLogger(__name__)


class SMS:
    def __init__(self):
        # get app credentials for authorization
        self.username = AT_USERNAME  # username in Africastalking app
        self.api_key = AT_APIKEY  # APIKEY

        # Initialize the SDK
        africastalking.initialize(self.username, self.api_key)

        # Get the SMS service
        self.sms = africastalking.SMS

    def send(self, recipients: list, message: str) -> str | None:
        try:
            # send message
            response = self.sms.send(message, recipients)['SMSMessageData']['Recipients'][0]['status']
            logger.info('Order message sent successfully', extra={'status': response, 'recipients': recipients})
            return response
        except Exception as e:
            logger.exception('Failed to send SMS')
            return None


send_sms = SMS()
