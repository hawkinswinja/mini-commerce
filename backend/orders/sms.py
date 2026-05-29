import logging
import africastalking
from opentelemetry import trace
from opentelemetry.trace import Status, StatusCode
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
        # Tracer for SMS operations
        self.tracer = trace.get_tracer(__name__)

    def send(self, recipients: list, message: str) -> str | None:
        # Create a span that represents the outbound SMS operation
        with self.tracer.start_as_current_span("sms.send", attributes={
            'sms.recipients': str(recipients),
            'sms.message_length': len(message),
        }) as span:
            try:
                # send message
                response = self.sms.send(message, recipients)['SMSMessageData']['Recipients'][0]['status']
                span.set_attribute('sms.status', str(response))
                logger.info('Order message sent successfully', extra={'status': response, 'recipients': recipients})
                return response
            except Exception as e:
                # record exception and mark span as error
                span.record_exception(e)
                span.set_status(Status(StatusCode.ERROR, str(e)))
                logger.exception('Failed to send SMS')
                return None


send_sms = SMS()
