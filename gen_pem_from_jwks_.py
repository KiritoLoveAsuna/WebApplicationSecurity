#!/bin/env python3
import requests
import argparse
import sys
import base64
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicNumbers
from cryptography.hazmat.backends import default_backend

def base64url_decode(input):
    """Decode base64url-encoded string to bytes, adding padding as necessary."""
    input += '=' * (4 - (len(input) % 4))
    return base64.urlsafe_b64decode(input)

def jwk_to_pem(jwk):
    """Convert a JWK to a PEM format."""
    n = int.from_bytes(base64url_decode(jwk['n']), 'big')
    e = int.from_bytes(base64url_decode(jwk['e']), 'big')

    public_numbers = RSAPublicNumbers(n=n, e=e)
    public_key = public_numbers.public_key(default_backend())
    pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    return pem

def get_jwks_to_pem(url):
    """Fetch the JWKS from the given URL and convert each key to PEM format."""
    response = requests.get(url)
    response.raise_for_status()  # Raises HTTPError for bad responses
    jwks = response.json()
    keys = jwks['keys']

    # Convert each JWK to PEM and print it
    for jwk in keys:
        pem = jwk_to_pem(jwk)
        print(pem.decode('utf-8'))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Fetch JWKS and convert to PEM")
    parser.add_argument("url", type=str, help="URL to fetch the JWKS from")
    args = parser.parse_args()

    try:
        get_jwks_to_pem(args.url)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
