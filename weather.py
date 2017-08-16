"""Docstring goes here."""
import configparser
import json

from pyowm import OWM


class OWMWeatherDict(dict):
    """docstring for OWMWeatherDict."""

    def __setattr__(self, name, value):
        super().__setattr__(name, value)

    @property
    def temperature(self):
        pass

    @temperature.getter
    def temperature(self):
        _temp = float(format(self['temperature']['temp'] - 273.15, '.2f'))
        return _temp

    @property
    def temp_high(self):
        pass

    @temp_high.getter
    def temp_high(self):
        _temp = float(format(self['temperature']['temp_max'] - 273.15, '.2f'))
        return _temp

    @property
    def temp_low(self):
        pass

    @temp_low.getter
    def temp_low(self):
        _temp = float(format(self['temperature']['temp_min'] - 273.15, '.2f'))
        return _temp

    @property
    def reference_time(self):
        pass

    @reference_time.getter
    def reference_time(self):
        return self['reference_time']

    @property
    def sunset_time(self):
        pass

    @sunset_time.getter
    def sunset_time(self):
        return self['sunset_time']

    @property
    def sunrise_time(self):
        pass

    @sunrise_time.getter
    def sunrise_time(self):
        return self['sunrise_time']


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
            self.today = OWMWeatherDict(json.loads(
                self.__observation.get_weather().to_JSON()))
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


if __name__ == '__main__':
    w = Weather()
    print(w.today)
    print(w.today.temperature)
