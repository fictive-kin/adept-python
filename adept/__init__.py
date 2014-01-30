# -*- coding: utf-8 -*-
import hashlib
import hmac
from urllib import quote as urlquote
from .errors import OperationError, AccountError


class Adept(object):

    def __init__(self, account_id, account_key, cloudfront_hostname, default_bucket=None):
        if account_id is not None:
            self.account_id = account_id
        else:
            raise AccountError('Please provide a valid account ID')
        
        if account_key is not None:
            self.account_key = account_key
        else:
            raise AccountError('Please provide a valid account key')

        if cloudfront_hostname is not None:
            self.cloudfront_hostname = cloudfront_hostname
        else:
            raise AccountError('Please provide a valid CloudFront hostname')

        if default_bucket is not None:
            self.default_bucket = default_bucket


    def _generate_hash(self, path):
        request_hash = hmac.new(
            self.account_key,
            path,
            hashlib.sha1
        )
        return request_hash.hexdigest()


    def generate_url(self, bucket=None, asset_key=None, asset_url=None, operations=['identity'], secure=True):
        """
        Given an S3 key and bucket/URL, perform given image operations on an image and return the URL.
        """
        if len(operations) < 1:
            raise OperationError('You didn\'t provide any operations to perform on the image')

        protocol = 'https://' if secure else 'http://'
        base_url = '%s%s' % (protocol, self.cloudfront_hostname)

        if asset_key is not None:
            if bucket is None:
                if self.default_bucket is None:
                    raise OperationError('No S3 bucket has been provided.')
                else:
                    bucket = self.default_bucket

            path = '/%s/%s/%s/%s' % (
                bucket,
                asset_key,
                '/'.join(operations),
                self.account_id,
            )

            request_hash = self._generate_hash(path)

            adept_url = ('%s%s/%s' % (
                base_url,
                path,
                request_hash)
            )

        elif asset_url is not None:

            path = '/loader/%s/%s' % (
                '/'.join(operations),
                self.account_id
            )
            loader_uri = '%s?url=%s' % (path, asset_url)
            request_hash = self._generate_hash(loader_uri)

            adept_url = '%s%s/%s?url=%s' % (
                base_url,
                path,
                request_hash,
                urlquote(asset_url)
            )
        else:
            raise OperationError("Asset key or URL must be provided")

        return adept_url
