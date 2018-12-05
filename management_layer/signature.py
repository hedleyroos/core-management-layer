import base64
import hashlib
import logging
from typing import Dict

from management_layer import mappings

LOGGER = logging.getLogger(__name__)


def compute_signature(account_id: str, account_secret: str, **kwargs: Dict[str, str]) -> str:
    """
    A signature is computed from the account ID and all other parameters to the call
    that creates an event, including those in the body.
    The account secret is appended and the result is hashed, and then base64 encoded.

    The signature is composed as follows:
    1. Take all API call and body parameters and supplement it with "account_id" and the lowercase
       version of the account ID.
    2. Convert al the names and values of the parameters to lowercase.
    3. Concatenate all key, value pairs using an "=", e.g. "account_id=12345"
    4. Sort the results of 3 alphabetically.
    5. Concatenate the results of 4 using "&".
    6. Append the account secret to the result of 5.
    7. Calculate the SHA256 digest of the result of 6.
    8. Base64 the binary digest, using URL-safe encoding (i.e. use "-" instead of "+" and "_"
       instead of "/").
    9. Convert the response to an ASCII string.

    :param account_id: The account ID
    :param account_secret: The account secret
    :param kwargs: The other arguments used in the computation.
    :return: The string signature
    """
    # The parameters to encode is collected as a dictionary. Keys and values are lower-cased.
    params = {
        "account_id": account_id.lower()
    }

    for key, value in kwargs.items():
        params[key.lower()] = str(value).lower()

    # Parameters are sorted based on the key and then concatenated.
    pairs = [f"{key.lower()}={value.lower()}" for key, value in params.items()]
    params_string = "&".join(entry for entry in sorted(pairs))
    to_sign = f"{params_string}{account_secret}".encode("utf8")
    sha256_digest = hashlib.sha256(to_sign).digest()
    signature = base64.urlsafe_b64encode(sha256_digest)
    return signature.decode("ascii")


def has_valid_signature(**kwargs) -> bool:
    """
    Given a dictionary of parameters passed to a URL, check if the signature is valid.
    :param kwargs: A dictionary of arguments
    :return: True if the signature is valid, else False
    """
    result = False
    try:
        account_id = kwargs.pop("account_id")
        credentials = mappings.Mappings.credentials_by_account_id(account_id)
        provided_signature = kwargs.pop("signature")  # Remove signature from signature args
        computed_signature = compute_signature(account_id, credentials["account_secret"], **kwargs)
        return provided_signature == computed_signature
    except KeyError:
        pass

    return result
