"""Docstring goes here."""
import configparser
import json

from pyowm import OWM


class Weather(object):
    """docstring for Weather."""

    def __init__(self, **kwargs):
        """Set up the Weather object."""
        super().__init__(**kwargs)
        try:
            self.config = configparser.ConfigParser()
            self.config.read('weather.conf')
            APIKEY = self.config.get('OpenWeatherMap', 'apikey')
            self.owm = OWM(APIKEY)
            self.__observation = self.owm.weather_at_place('Boston,US')
            self.__forecaster = self.owm.daily_forecast('Boston,US')
            self.today = json.loads(self.__observation.get_weather().to_JSON())
            self.__forecast = self.__forecaster.get_forecast()
            self.forecasts = []
            for fc in self.__forecast.get_weathers():
                self.forecasts.append(json.loads(fc.to_JSON()))
        except Exception as e:
            raise
        finally:
            pass

    def update(self):
        """Update the weather information."""
        try:
            self.__observation = self.owm.weather_at_place('Boston,US')
            self.__forecaster = self.owm.daily_forecast('Boston,US')
            self.today = json.loads(self.__observation.get_weather().to_JSON())
            self.forecasts = []
            for fc in self.__forecast.get_weathers():
                self.forecasts.append(json.loads(fc.to_JSON()))
        except Exception as e:
            raise
        finally:
            pass
