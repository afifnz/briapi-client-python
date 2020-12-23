import datetime
import pytest

from briapi_client_python.briva import Briva

CLIENT_SECRET = 'LpPGW8vR9NDA64me'
CLIENT_ID = 'jB4CieGKH9uDE11DZR6jsscFoTZo8cPh'

now = datetime.datetime.now()
yesterday = now - datetime.timedelta(days=1)


def generate_instance():
    briva = Briva(client_secret=CLIENT_SECRET, client_id=CLIENT_ID)
    return briva

def generate_parameters():
    expired_date = datetime.datetime.now() + datetime.timedelta(days=1)
    parameters = {
	    "institutionCode": "j104408",
	    "brivaNo": "77777",
	    "custCode": "0812199121",
	    "nama": "Aminarti Dini",
	    "amount": "1000000",
	    "keterangan": "",
	    "expiredDate": expired_date.strftime("%Y-%m-%d %H:%M:%S")
    }
    return parameters

def test_token():
    briva = generate_instance()
    token = briva.token()
    assert token['status'] == 'approved'
    pytest.token = token.get('access_token')

def test_create():
    briva = generate_instance()
    parameters = generate_parameters()
    response = briva.create(parameters=parameters)
    assert response['status'] == True
    assert response['responseCode'] == '00'
    return response

def test_get():
    briva = generate_instance()
    parameters = generate_parameters()
    del parameters['nama']
    del parameters['amount']
    del parameters['keterangan']
    del parameters['expiredDate']
    response = briva.get(parameters=parameters)
    assert response['status'] == True
    assert response['responseCode'] == '00'
    return response

def test_status():
    briva = generate_instance()
    parameters = generate_parameters()
    del parameters['nama']
    del parameters['amount']
    del parameters['keterangan']
    del parameters['expiredDate']
    response = briva.status(parameters=parameters)
    assert response['status'] == True
    assert response['responseCode'] == '00'
    assert response['data']['statusBayar'] == 'N'
    return response

def test_status_update():
    briva = generate_instance()
    parameters = generate_parameters()
    del parameters['nama']
    del parameters['amount']
    del parameters['keterangan']
    del parameters['expiredDate']
    parameters['statusBayar'] = 'Y'
    response = briva.status_update(parameters=parameters)
    assert response['status'] == True
    assert response['responseCode'] == '00'
    assert response['data']['statusBayar'] == 'Y'
    return response

def test_update():
    briva = generate_instance()
    parameters = generate_parameters()
    parameters['nama'] = 'Dini Aminarti'
    response = briva.update(parameters=parameters)
    assert response['status'] == True
    assert response['responseCode'] == '00'
    assert response['data']['nama'] == 'Dini Aminarti'
    return response

def test_delete():
    briva = generate_instance()
    parameters = generate_parameters()
    del parameters['nama']
    del parameters['amount']
    del parameters['keterangan']
    del parameters['expiredDate']
    response = briva.delete(parameters=parameters)
    assert response['status'] == True
    assert response['responseCode'] == '00'
    return response

def test_report():
    briva = generate_instance()
    parameters = generate_parameters()
    del parameters['nama']
    del parameters['amount']
    del parameters['keterangan']
    del parameters['expiredDate']
    del parameters['custCode']
    parameters['startDate'] = yesterday.strftime('%Y%m%d')
    parameters['endDate'] = now.strftime('%Y%m%d')
    response = briva.report(parameters=parameters)
    assert response['status'] == True
    assert response['responseCode'] == '00'
    return response

def test_report_time():
    briva = generate_instance()
    parameters = generate_parameters()
    del parameters['nama']
    del parameters['amount']
    del parameters['keterangan']
    del parameters['expiredDate']
    del parameters['custCode']
    parameters['startDate'] = now.strftime('%Y-%m-%d')
    parameters['startTime'] = '00:00'
    parameters['endDate'] = now.strftime('%Y-%m-%d')
    parameters['endTime'] = '23:59'
    response = briva.report_time(parameters=parameters)
    assert response['status'] == True
    assert response['responseCode'] == '00'
    return response
