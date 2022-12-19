from ratelimiter import RateLimiter
import cloudscraper  # Replaces requests and can get around cloudflare bot check
from lachtertrading.config import TELEGRAM_GROUPID, TELEGRAM_TOKEN


class TelegramAPI:
    # Initialize the class
    def __init__(self, token, host='api.telegram.org', maxcalls=250, period=1):
        ''' Initilization function for the class
            -- maxcalls the max api (web requests) calls to make in a period, int
            -- period the time in seconds a period should last, int
        '''
        self.host = host
        self.maxcalls = maxcalls
        self.period = period
        self.token = token
        self._session = cloudscraper.create_scraper()
        self._ratelimiter = RateLimiter(max_calls=self.maxcalls, period=self.period)

    @property
    def _baseurl(self):
        return 'https://{}/bot{}'.format(self.host, self.token)
    def _get(self, resource, params=None):
        ''' Get Methods '''
        endpoint = '{}/{}'.format(self._baseurl, resource)
        with self._ratelimiter:
            return self._session.get(endpoint, params=params)

    def sendmessage(self, group, message):
        """
        This sends a message to the provided group
        :param group: The group ID to send the message too
        :param message: The message to send
        :return: status of request
        """
        resource = 'sendMessage'
        params = {
            'chat_id': group,
            'text': message
        }
        return self._get(resource, params)

    def getupdates(self):
        resource = 'getUpdates'
        return self._get(resource)


if __name__ == "__main__":
    notify = TelegramAPI(token=TELEGRAM_TOKEN)
    #response = notify.sendmessage(TELEGRAM_GROUPID, 'Test Message!')
    response = notify.getupdates()
    print(response.content)
