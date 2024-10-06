import africastalking
from minicommerce.settings import AT_USERNAME, AT_APIKEY


class SMS:
    def __init__(self):
        # get app credentials for authorization
        self.username = AT_USERNAME  # username in Africastalking app
        self.api_key = AT_APIKEY  # APIKEY

        # Initialize the SDK
        africastalking.initialize(self.username, self.api_key)

        # Get the SMS service
        self.sms = africastalking.SMS

    def send(self, recipients: list, message: str) -> str:
        try:
            # send message
            response = self.sms.send(message, recipients)['SMSMessageData']['Recipients'][0]['status']
            print(f"Order message sent successful with status: {response}")
            # return response
        except Exception as e:
            print(str(e))


send_sms = SMS()
