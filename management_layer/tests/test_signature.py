import calendar
import time
from unittest import TestCase
from unittest.mock import patch

from management_layer.signature import compute_signature, has_valid_signature


class TestSignature(TestCase):

    def test_compute_signature(self):
        expected_signature = "ZCY_btOyu-9dACWWOFILDeOEcSs3SsjtNoM2e5hRW-4="
        account_id = "eibahchiefeuchaesheiQuo1leegh9pa"
        account_secret = "OhThufoh0eetheewoochah5sheegh1ye"

        params = {
            "some": "arbitrary",
            "argument": "1",
            "typically_obtained": "from_a_request"
        }

        computed_signature = compute_signature(account_id, account_secret, **params)
        self.assertEqual(computed_signature, expected_signature)

    @patch.multiple("management_layer.mappings.Mappings",
                    _account_id_to_credentials_map={
                        "eibahchiefeuchaesheiQuo1leegh9pa": {
                            "account_secret": "OhThufoh0eetheewoochah5sheegh1ye"
                        }
                    })
    def test_has_valid_signature(self):
        params = {
            "account_id": "eibahchiefeuchaesheiQuo1leegh9pa",
            "some": "arbitrary",
            "argument": "1",
            "typically_obtained": "from_a_request",
            "nonce": "thisisanonce",
            # Note that we do not set an expiry for this test, on order
            # to keep the computation static.
            # "expiry": str(calendar.timegm(time.gmtime()) + 600),
            "signature": "n-Yb8cHz-Hs3ZLv0tlKhkxAAcpYFo-QKDqq6jxywO0A="
        }

        self.assertTrue(has_valid_signature(**params))

        # Unknown account ID
        params = {
            "account_id": "unknown",
            "some": "arbitrary",
            "argument": "1",
            "typically_obtained": "from_a_request",
            "signature": "ZCY_btOyu-9dACWWOFILDeOEcSs3SsjtNoM2e5hRW-4="
        }

        self.assertFalse(has_valid_signature(**params))

        # Missing account ID
        params = {
            "some": "arbitrary",
            "argument": "1",
            "typically_obtained": "from_a_request",
            "signature": "ZCY_btOyu-9dACWWOFILDeOEcSs3SsjtNoM2e5hRW-4="
        }

        self.assertFalse(has_valid_signature(**params))

        # Missing signature
        params = {
            "account_id": "unknown",
            "some": "arbitrary",
            "argument": "1",
            "typically_obtained": "from_a_request",
        }

        self.assertFalse(has_valid_signature(**params))

        # Invalid signature
        params = {
            "account_id": "unknown",
            "some": "arbitrary",
            "argument": "1",
            "typically_obtained": "from_a_request",
            "signature": "foobar"
        }

        self.assertFalse(has_valid_signature(**params))
