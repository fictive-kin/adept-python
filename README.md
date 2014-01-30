## Adept 

### Installation

`pip install git+ssh://git@github.com/fictivekin/adept-python.git`

### Using the package

Import the Adept class from the package, pass through your account credentials

```
from adept import Adept
a = Adept(
    accound_id='9b5dd41deff8ae7e3767fc6566cb25ff3ca66438',
    account_key='251692b3899f1e30fe4b7037185488aad37c46f8',
    cloudfront_hostname='some.cloudfront.host.com'
)
```

You can then generate a URL for given image operations on an S3 asset (and specified bucket) or image URL.

An example using an S3 asset:

```
operations = ['maxwidth-400', 'cropcenter-400x300']
a.generate_url(
    bucket='gimmebar-assets',
    asset_key='526fc2761c899.jpg',
    operations=operations,
)
```
