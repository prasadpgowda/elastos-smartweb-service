import logging
import requests
import json
import datetime
from flask import jsonify
from flask import request
from flask import Response
from flask_api import FlaskAPI, status, exceptions
from flask_restplus import Resource
from smartweb_service import settings
from smartweb_service.api.restplus import api
from smartweb_service.api.common.common_service import validate_api_key
from smartweb_service.api.common.common_service import getTime

log = logging.getLogger(__name__)

ns = api.namespace('1/service/mainchain', description='Has wallet services')

@ns.route('/createWallet')
class CreateWallet(Resource):

    def get(self):
        """
        Returns the wallet created
        """
        api_key = request.headers.get('api_key')
        api_status = validate_api_key(api_key)
        if not api_status:
            data = {"error message":"API Key could not be verified","status":401, "timestamp":getTime(),"path":request.url}
            return Response(json.dumps(data), 
                status=401,
                mimetype='application/json'
            )

        api_url_base = settings.WALLET_SERVICE_URL + settings.WALLET_API_CREATE
        myResponse = requests.get(api_url_base).json()
        return Response(json.dumps(myResponse), 
                status=myResponse['status'],
                mimetype='application/json'
            )

@ns.route('/getBalance/<string:balance_address>')
class GetBalance(Resource):

    def get(self, balance_address):
        """
        Returns the balance of the provided public address
        """
        api_key = request.headers.get('api_key')
        api_status = validate_api_key(api_key)
        if not api_status:
            data = {"error message":"API Key could not be verified","status":401, "timestamp":getTime(),"path":request.url}
            return Response(json.dumps(data), 
                status=401,
                mimetype='application/json'
            )

        api_url_base = settings.WALLET_SERVICE_URL + settings.WALLET_API_BALANCE + "{}"
        myResponse = requests.get(api_url_base.format(balance_address)).json()
        return Response(json.dumps(myResponse), 
                status=myResponse['status'],
                mimetype='application/json'
            )

@ns.route('/getDPOSVote', methods = ['POST'])
class GetDPOSVote(Resource):

    def post(self):
        """
        Uses private key to vote your producers
        """
        api_key = request.headers.get('api_key')
        api_status = validate_api_key(api_key)
        if not api_status:
            data = {"error message":"API Key could not be verified","status":401, "timestamp":getTime(),"path":request.url}
            return Response(json.dumps(data), 
                status=401,
                mimetype='application/json'
            )

        api_url_base = settings.WALLET_SERVICE_URL + settings.WALLET_API_DPOS_VOTE
        headers = {'Content-type': 'application/json'}
        req_data = request.get_json()
        myResponse = requests.post(api_url_base, data=json.dumps(req_data), headers=headers).json()
        return Response(json.dumps(myResponse), 
                status=myResponse['status'],
                mimetype='application/json'
            )

@ns.route('/getTransactions')
class GetTransactions(Resource):

    def get(self):
        """
        Get a list of transactions
        """
        api_key = request.headers.get('api_key')
        api_status = validate_api_key(api_key)
        if not api_status:
            data = {"error message":"API Key could not be verified","status":401, "timestamp":getTime(),"path":request.url}
            return Response(json.dumps(data), 
                status=401,
                mimetype='application/json'
            )

        api_url_base = settings.WALLET_SERVICE_URL + settings.WALLET_API_TRANSACTIONS
        headers = {'Content-type': 'application/json'}
        req_data = request.get_json()
        myResponse = requests.post(api_url_base, data=json.dumps(req_data), headers=headers).json()
        return Response(json.dumps(myResponse), 
                status=myResponse['status'],
                mimetype='application/json'
            )

@ns.route('/getTransactionHistory/<string:transaction_address>')
class GetTransactionHistory(Resource):

    def get(self, transaction_address):
        """
        Get transaction history
        """
        api_key = request.headers.get('api_key')
        api_status = validate_api_key(api_key)
        if not api_status:
            data = {"error message":"API Key could not be verified","status":401, "timestamp":getTime(),"path":request.url}
            return Response(json.dumps(data), 
                status=401,
                mimetype='application/json'
            )

        api_url_base = settings.WALLET_SERVICE_URL + settings.WALLET_API_TRANSACTION_HISTORY + "{}"
        myResponse = requests.get(api_url_base.format(transaction_address)).json()
        return Response(json.dumps(myResponse), 
                status=myResponse['status'],
                mimetype='application/json'
            )

@ns.route('/transferELA', methods = ['POST'])
class TransferELA(Resource):

    def post(self):
        """
        Transfer ELA
        """
        api_key = request.headers.get('api_key')
        api_status = validate_api_key(api_key)
        if not api_status:
            data = {"error message":"API Key could not be verified","status":401, "timestamp":getTime(),"path":request.url}
            return Response(json.dumps(data), 
                status=401,
                mimetype='application/json'
            )

        api_url_base = settings.WALLET_SERVICE_URL + settings.WALLET_API_TRANSFER
        headers = {'Content-type': 'application/json'}
        req_data = request.get_json()
        myResponse = requests.post(api_url_base, data=json.dumps(req_data), headers=headers).json()
        return Response(json.dumps(myResponse), 
                status=myResponse['status'],
                mimetype='application/json'
            )

@ns.route('/getMnemonic')
class GetMnemonic(Resource):

    def get(self):
        """
        Generates a mnemonic
        """
        api_key = request.headers.get('api_key')
        api_status = validate_api_key(api_key)
        if not api_status:
            data = {"error message":"API Key could not be verified","status":401, "timestamp":getTime(),"path":request.url}
            return Response(json.dumps(data), 
                status=401,
                mimetype='application/json'
            )

        api_url_base = settings.WALLET_SERVICE_URL + settings.WALLET_API_MNEMONIC
        myResponse = requests.get(api_url_base).json()
        return Response(json.dumps(myResponse), 
                status=myResponse['status'],
                mimetype='application/json'
            )

  
