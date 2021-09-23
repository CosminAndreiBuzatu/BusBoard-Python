import requests


class PostCode:


    def __init__(self, postcode):
        self.postcode = postcode

    def getPostcodeInfo(self):
        r = requests.get(f'https://api.postcodes.io/postcodes/{self.postcode}')
        response = r.json()
        return response

    def getCoordonate(self):
        r = self.getPostcodeInfo()
        longitude = r['result']['longitude']

        latitude = r['result']['latitude']
        return longitude, latitude
