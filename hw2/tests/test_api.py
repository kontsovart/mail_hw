import pytest

from api.mytarget_client import MyTargetClient
from ui.fixtures import *


class TestMyTarget:

    @pytest.fixture(scope='function')
    def api_client(self):
        user = 'qa-python-target@yandex.ru'
        password = 'qazwsx123'

        return MyTargetClient(user, password)

    @pytest.mark.skip(reason='TEMP')
    def test_auth(self, api_client):
        api_client.auth_post()
        response = api_client.get_cabinet_page()
        api_client.get_z_cookie_page()
        print(api_client.session.cookies)
        assert 'qa-python-target@yandex.ru' in response.text

    # @pytest.mark.skip(reason='TEMP')
    def test_new_segment(self, random_string_ascii, api_client):
        resp = api_client.auth_post()
        api_client.get_z_cookie_page()
        api_client.get_segment_page()
        api_client.add_cookie(mc=api_client.session.cookies['mc'],
                              ssdc=api_client.session.cookies['ssdc'],
                              mrcu=api_client.session.cookies['mrcu'],
                              sdcs=api_client.session.cookies['sdcs'],
                              z_token=api_client.session.cookies['z'])
        response = api_client.add_segment_post(random_string_ascii)
        # print(api_client.session.cookies)
        assert 200 == response.status_code

    @pytest.mark.skip(reason='TEMP')
    def test_aaaaaaaaaa(self, api_client):
        resp = api_client.auth_post()
        api_client.get_z_cookie_page()
        api_client.get_segment_page()
        resp = api_client.get_cufuds()
        print(resp.json())
        assert resp.status_code == 200

    @pytest.mark.skip(reason='TEMP')
    def test_bbbbbbbbb(self, api_client):
        resp = api_client.auth_post()
        api_client.get_z_cookie_page()
        api_client.get_segment_page()
        resp = api_client.get_sdfsa()
        print(resp.json())
        assert resp.status_code == 200