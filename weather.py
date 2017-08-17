"""Docstring goes here."""
import configparser
import json
import pprint

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

    @property
    def humidity(self):
        pass

    @humidity.getter
    def humidity(self):
        return self['humidity']

    @property
    def pressure(self):
        pass

    @pressure.getter
    def pressure(self):
        _pressure = float(self['pressure']['press'])
        return _pressure

    @property
    def rain(self):
        pass

    @rain.getter
    def rain(self):
        if any(self['rain']):
            _rain = float(self['rain']['3h'])
            return _rain
        else:
            return None

    @property
    def snow(self):
        pass

    @snow.getter
    def snow(self):
        if any(self['snow']):
            _snow = float(self['snow']['3h'])
            return _snow
        else:
            return None

    @property
    def clouds(self):
        pass

    @clouds.getter
    def clouds(self):
        _clouds = int(self['clouds'])
        return _clouds

    @property
    def wind_speed(self):
        pass

    @wind_speed.getter
    def wind_speed(self):
        _wind_speed = float(self['wind']['speed'])
        return _wind_speed

    @property
    def wind_deg(self):
        pass

    @wind_deg.getter
    def wind_deg(self):
        _wind_deg = float(self['wind']['deg'])
        return _wind_deg

    @property
    def status(self):
        pass

    @status.getter
    def status(self):
        _status = self['status'].title()
        return _status

    @property
    def detailed_status(self):
        pass

    @detailed_status.getter
    def detailed_status(self):
        _detailed_status = self['detailed_status'].title()
        return _detailed_status

    @property
    def status_icon_url(self):
        pass

    @status_icon_url.getter
    def status_icon_url(self):
        _status_icon_url = 'http://openweathermap.org/img/w/' + \
            self['weather_icon_name'] + '.png'
        return _status_icon_url


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
    pp = pprint.PrettyPrinter(indent=4)
    w = Weather()
    pp.pprint(w.today)
    pp.pprint(w.today.temperature)
