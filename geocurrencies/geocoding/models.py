import json
import logging
import requests
from django.conf import settings
from pycountry import countries
from timezonefinder import TimezoneFinder

from .settings import *

GEOCODER_GOOGLE_URL = 'https://maps.googleapis.com/maps/api'

from ..countries.models import Country

tf = TimezoneFinder(in_memory=True)


class Geocoder:

    def __new__(cls, coder_type=None, *args, **kwargs):
        try:
            selected_api = settings.GEOCODING_SERVICE
        except AttributeError:
            selected_api = GEOCODING_SERVICE

        if not coder_type:
            coder_type = selected_api
        if coder_type == 'pelias' and settings.GEOCODER_PELIAS:
            return PeliasGeoCoder(*args, **kwargs)
        elif coder_type == 'google' and settings.GEOCODER_GOOGLE:
            return GoogleGeocoder(*args, **kwargs)
        else:
            raise ValueError("Invalid geocoder")

    def search(self, address, language=None, bounds=None, region=None, components=""):
        """
        :params text: address to search for
        :params language: optional, language of result
        :params bounds: optional, limit results to bounds
        :params region: optional, limit results to region
        :params components: optional, a components filter with elements separated by a pipe (|)
        :returns: Country
        """
        raise NotImplementedError("Use specific implementation")

    def reverse(self, lat, lng):
        """
        :params lat: latitude
        :params lng: longitude
        """
        raise NotImplementedError("Use specific implementation")

    def parse_countries(self, data):
        """
        :params data: geocoding / reverse geocoding result
        :returns: Country instance
        """
        raise NotImplementedError("Use specific implementation")

    def countries(self, data):
        """
        :params data: json response from geocoding / reverse geocoding service
        """
        countries = []
        alphas = self.parse_countries(data=data)
        for alpha in alphas:
            try:
                if len(alpha) == 2:
                    country = Country(alpha)
                elif len(alpha) == 3:
                    country = Country(alpha[0:2])
                else:
                    country = Country(alpha)
            except KeyError:
                continue
            countries.append(country)
        return countries






