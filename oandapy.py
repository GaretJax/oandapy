"""
OANDA API wrapper for OANDA's REST API
"""
import json
import requests


class RequestsMixin(object):
    version = 1

    def _endpoint(self, *segments):
        return '/'.join(['v%d' % self.version] + [str(s) for s in segments])

    def _request(self, method, *segments, **params):
        endpoint = self._endpoint(*segments)
        return self.request(endpoint=endpoint, method=method, params=params)

    def _get(self, *args, **kwargs):
        return self._request('GET', *args, **kwargs)

    def _post(self, *args, **kwargs):
        return self._request('POST', *args, **kwargs)

    def _patch(self, *args, **kwargs):
        return self._request('PATCH', *args, **kwargs)

    def _delete(self, *args, **kwargs):
        return self._request('DELETE', *args, **kwargs)


class EndpointsMixin(object):
    """EndpointsMixin provides a mixin for the API instance

    Parameters that need to be embedded in the API url just need to be passed
    as a keyword argument.

    E.g. oandapy_instance.get_instruments(instruments="EUR_USD")
    """

    # Rates

    def get_instruments(self, account_id, **params):
        """Get an instrument list

        Docs: http://developer.oanda.com/docs/v1/rates/#get-an-instrument-list
        """
        return self._get('instruments', accountId=account_id, **params)

    def get_prices(self, **params):
        """Get current prices

        Docs: http://developer.oanda.com/docs/v1/rates/#get-current-prices
        """
        return self._get('prices', **params)

    def get_history(self, **params):
        """Retrieve instrument history

        Docs: http://developer.oanda.com/docs/v1/rates/#retrieve-instrument-history
        """
        return self._get('candles', **params)

    # Accounts

    def create_account(self, **params):
        """Create an account. Valid only in sandbox.

        Docs: http://developer.oanda.com/docs/v1/accounts/#get-accounts-for-a-user
        """
        return self._post('accounts', **params)

    def get_accounts(self, **params):
        """Get accounts for a user.

        Docs: http://developer.oanda.com/docs/v1/accounts/#get-accounts-for-a-user
        """
        return self._get('accounts', **params)

    def get_account(self, account_id, **params):
        """Get account information

        Docs: http://developer.oanda.com/docs/v1/accounts/#get-account-information
        """
        return self._get('accounts', account_id, **params)

    # Orders

    def get_orders(self, account_id, **params):
        """Get orders for an account

        Docs: http://developer.oanda.com/docs/v1/orders/#get-orders-for-an-account
        """
        return self._get('accounts', account_id, 'orders', **params)

    def create_order(self, account_id, **params):
        """Create a new order

        Docs: http://developer.oanda.com/docs/v1/orders/#create-a-new-order
        """
        return self._post('accounts', account_id, 'orders', **params)

    def get_order(self, account_id, order_id, **params):
        """Get information for an order

        Docs: http://developer.oanda.com/docs/v1/orders/#get-information-for-an-order
        """
        return self._get('accounts', account_id, 'orders', order_id, **params)

    def modify_order(self, account_id, order_id, **params):
        """Modify an existing order

        Docs: http://developer.oanda.com/docs/v1/orders/#modify-an-existing-order
        """
        return self._patch('accounts', account_id, 'orders', order_id,
                           **params)

    def close_order(self, account_id, order_id, **params):
        """Close an order

        Docs: http://developer.oanda.com/docs/v1/orders/#close-an-order
        """
        return self._delete('accounts', account_id, 'orders', order_id,
                            **params)

    # Trades

    def get_trades(self, account_id, **params):
        """Get a list of open trades

        Docs: http://developer.oanda.com/docs/v1/trades/#get-a-list-of-open-trades
        """
        return self._get('accounts', account_id, 'trades', **params)

    def get_trade(self, account_id, trade_id, **params):
        """Get information on a specific trade

        Docs: http://developer.oanda.com/docs/v1/trades/#get-information-on-a-specific-trade
        """
        return self._get('accounts', account_id, 'trades', trade_id, **params)

    def modify_trade(self, account_id, trade_id, **params):
        """Modify an existing trade

        Docs: http://developer.oanda.com/docs/v1/trades/#modify-an-existing-trade
        """
        return self._patch('accounts', account_id, 'trades', trade_id,
                           **params)

    def close_trade(self, account_id, trade_id, **params):
        """Close an open trade

        Docs: http://developer.oanda.com/docs/v1/trades/#close-an-open-trade
        """
        return self._delete('accounts', account_id, 'trades', trade_id,
                            **params)

    # Positions

    def get_positions(self, account_id, **params):
        """Get a list of all open positions

        Docs: http://developer.oanda.com/docs/v1/positions/#get-a-list-of-all-open-positions
        """
        return self._get('accounts', account_id, 'positions', **params)

    def get_position(self, account_id, instrument, **params):
        """Get the position for an instrument

        Docs: http://developer.oanda.com/docs/v1/positions/#get-the-position-for-an-instrument
        """
        return self._get('accounts', account_id, 'positions', instrument,
                         **params)

    def close_position(self, account_id, instrument, **params):
        """Close an existing position

        Docs: http://developer.oanda.com/docs/v1/positions/#close-an-existing-position
        """
        return self._delete('accounts', account_id, 'positions', instrument,
                            **params)

    # Transaction history

    def get_transaction_history(self, account_id, **params):
        """Get transaction history

        Docs: http://developer.oanda.com/docs/v1/transactions/#get-transaction-history
        """
        return self._get('accounts', account_id, 'transactions', **params)

    def get_transaction(self, account_id, transaction_id):
        """Get information for a transaction

        Docs: http://developer.oanda.com/docs/v1/transactions/#get-information-for-a-transaction
        """
        return self._get('accounts', account_id, 'transactions',
                         transaction_id)

    # Forex labs

    def get_eco_calendar(self, **params):
        """Return up to 1 year of economic calendar info

        Docs: http://developer.oanda.com/rest-live/forex-labs/
        """
        endpoint = 'labs/v1/calendar'
        return self.request(endpoint, params=params)

    def get_historical_position_ratios(self, **params):
        """Return up to 1 year of historical position ratios

        Docs: http://developer.oanda.com/rest-live/forex-labs/
        """
        endpoint = 'labs/v1/historical_position_ratios'
        return self.request(endpoint, params=params)

    def get_historical_spreads(self, **params):
        """Return up to 1 year of spread information

        Docs: http://developer.oanda.com/rest-live/forex-labs/
        """
        endpoint = 'labs/v1/spreads'
        return self.request(endpoint, params=params)

    def get_commitments_of_traders(self, **params):
        """Return up to 4 years of Commitments of Traders data from the CFTC

        Docs: http://developer.oanda.com/rest-live/forex-labs/
        """
        endpoint = 'labs/v1/commitments_of_traders'
        return self.request(endpoint, params=params)

    def get_orderbook(self, **params):
        """Return up to 1 year of OANDA Order book data

        Docs: http://developer.oanda.com/rest-live/forex-labs/
        """
        endpoint = 'labs/v1/orderbook_data'
        return self.request(endpoint, params=params)


class API(EndpointsMixin, RequestsMixin, object):
    """Provides functionality for access to core OANDA API calls"""

    environments = {
        'sandbox': 'http://api-sandbox.oanda.com',
        'practice': 'https://api-fxpractice.oanda.com',
        'live': 'https://api-fxtrade.oanda.com',
    }

    def __init__(self, environment='practice', access_token=None,
                 headers=None):
        """Instantiate an instance of OandaPy's API wrapper

        :param environment: (optional) Provide the environment for oanda's REST
                            api, either 'sandbox', 'practice', or 'live'.
                            Default: practice
        :param access_token: (optional) Provide a valid access token if you
                             have one. This is required if the environment is
                             not sandbox.
        """

        self.api_url = self.environments[environment]
        self.access_token = access_token
        self.client = requests.Session()

        # Personal token authentication
        if self.access_token:
            self.client.headers['Authorization'] = (
                'Bearer ' + self.access_token)

        if headers:
            self.client.headers.update(headers)

    def request(self, endpoint, method='GET', params=None):
        """Return dict of response from OANDA's open API

        :param endpoint: (required) OANDA API endpoint (e.g. v1/instruments)
        :type endpoint: string
        :param method: (optional) Method of accessing data, either GET or POST.
                       (default GET)
        :type method: string
        :param params: (optional) Dict of parameters (if any) accepted by the
                       OANDA API endpoint you are trying to access
                       (default None)
        :type params: dict or None
        """

        url = '%s/%s' % (self.api_url, endpoint)

        method = method.lower()
        params = params or {}

        func = getattr(self.client, method)

        request_args = {}
        if method == 'get':
            request_args['params'] = params
        else:
            request_args['data'] = params

        try:
            response = func(url, **request_args)
        except requests.RequestException as e:
            print(str(e))

        content = response.json()

        # error message
        if response.status_code >= 400:
            raise OandaError(content)

        return content


class Streamer(object):
    """Provide functionality for HTTPS Streaming

    Docs: http://developer.oanda.com/docs/v1/stream/#rates-streaming
    """

    environments = {
        'practice': 'https://stream-fxpractice.oanda.com/v1/prices',
        'live': 'https://stream-fxtrade.oanda.com/v1/prices',
    }

    def __init__(self, environment='practice', access_token=None):
        """Instantiates an instance of OandaPy's streaming API wrapper.

        :param environment: (optional) Provide the environment for oanda's REST
                            api, either 'practice', or 'live'.
                            (default: practice)
        :param access_token: (optional) Provide a valid access token if you
                             have one. This is required if the environment is
                             not sandbox.
        """

        self.api_url = self.environments[environment]
        self.access_token = access_token
        self.client = requests.Session()
        self.client.stream = True
        self.connected = False

        # Personal token authentication
        if self.access_token:
            self.client.headers['Authorization'] = (
                'Bearer ' + self.access_token)

    def start(self, ignore_heartbeat=True, **params):
        """Start the stream with the given parameters

        :param accountId: (Required) The account that prices are
                          applicable for.
        :param instruments: (Required) A (URL encoded) comma separated list of
                            instruments to fetch prices for.
        :param ignore_heartbeat: (optional) Whether or not to display the
                                 heartbeat. Default: True
        """
        self.connected = True

        request_args = {}
        request_args['params'] = params

        while self.connected:
            response = self.client.get(self.api_url, **request_args)

            if response.status_code != 200:
                self.on_error(response.content)

            for line in response.iter_lines(90):
                if not self.connected:
                    break

                if line:
                    data = json.loads(line.decode("utf-8"))
                    if not (ignore_heartbeat and "heartbeat" in data):
                        self.on_success(data)

    def on_success(self, data):
        """Called when data is successfully retrieved from the stream

        Override this to handle your streaming data.
        :param data: response object sent from stream
        """
        pass

    def on_error(self, data):
        """Called when stream returns non-200 status code

        Override this to handle your streaming data.
        :param data: error response object sent from stream
        """
        pass

    def disconnect(self):
        """Manually disconnect the streaming client"""
        self.connected = False


class OandaError(Exception):
    """Generic error class to catch oanda response errors"""

    def __init__(self, error_response):
        msg = "OANDA API returned error code %s (%s)" % (
            error_response['code'], error_response['message'])
        super(OandaError, self).__init__(msg)
