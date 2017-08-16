"""Testing methods for the Weather class."""
import unittest
import pytest
import datetime
now = datetime.datetime.now()
then = now - datetime.timedelta(days=90)


@pytest.fixture
def weatherdict():
    import weather
    weather = weather.Weather()
    return weather.today


@pytest.fixture
def weatherdictkeys():
    _weather_keys = ['reference_time', 'sunset_time',
                     'sunrise_time', 'clouds', 'rain',
                     'snow', 'wind', 'humidity', 'pressure',
                     'temperature', 'status', 'detailed_status',
                     'weather_code', 'weather_icon_name',
                     'visibility_distance', 'dewpoint',
                     'humidex', 'heat_index']
    return _weather_keys


def test_is_dictionary(weatherdict, weatherdictkeys):
    """Is today a dictionary."""
    assert isinstance(weatherdict, dict)
    assert list(weatherdict.keys()) == weatherdictkeys


def test_tempuratures(weatherdict):
    """Are the temperatures valid float values."""
    assert isinstance(weatherdict.temperature, float)
    assert -100 <= weatherdict.temperature <= 60
    assert isinstance(weatherdict.temp_high, float)
    assert -100 <= weatherdict.temp_low <= 60
    assert isinstance(weatherdict.temp_low, float)
    assert -100 <= weatherdict.temp_low <= 60


def test_reference_time(weatherdict):
    """Is the reference_time a valid int value."""
    assert isinstance(weatherdict['reference_time'], int)
    assert isinstance(weatherdict.reference_time, int)
    assert weatherdict.reference_time > int(then.strftime('%s'))


def test_sunset_time(weatherdict):
    """Is the sunset_time a valid int value."""
    assert isinstance(weatherdict['sunset_time'], int) or isinstance(
        weatherdict['sunset_time'], type(None))
    assert isinstance(weatherdict.sunset_time, int) or isinstance(
        weatherdict.sunset_time, type(None))
    assert weatherdict.sunset_time > int(
        then.strftime('%s')) or weatherdict.sunset_time is None


def test_sunrise_time(weatherdict):
    """Is the sunrise_time a valid int value."""
    assert isinstance(weatherdict['sunrise_time'], int) or isinstance(
        weatherdict['sunrise_time'], type(None))
    assert isinstance(weatherdict.sunrise_time, int) or isinstance(
        weatherdict.sunrise_time, type(None))
    assert weatherdict.sunrise_time > int(
        then.strftime('%s')) or weatherdict.sunrise_time is None

# def test_sunset_time_is_int_or_none(self):
#     """sunset_time is an int or none."""
#     try:
#         self.assertTrue(isinstance(self.weather.today['sunset_time'], int)
#                         or isinstance(self.weather.today['sunset_time'],
#                                       type(None)))
#     except Exception as e:
#         raise
#     finally:
#         pass
#
#
# def test_sunrise_time_is_int_or_none(self):
#     """sunrise_time is an int or none."""
#     try:
#         self.assertTrue(isinstance(self.weather.today['sunrise_time'], int)
#                         or isinstance(self.weather.today['sunrise_time'],
#                                       type(None)))
#     except Exception as e:
#         raise
#     finally:
#         pass
#
#
# def test_clouds_is_int(self):
#     """'clouds' is an int."""
#     try:
#         self.assertTrue(int(self.weather.today['clouds']))
#     except Exception as e:
#         raise
#     finally:
#         pass
#
#
# def test_rain_is_dictionary(self):
#     """'rain' is a dictionary."""
#     try:
#         self.assertTrue(isinstance(self.weather.today['rain'], dict))
#     except Exception as e:
#         raise
#     finally:
#         pass
#
#
# def test_snow_is_dictionary(self):
#     """'snow' is a dictionary."""
#     try:
#         self.assertTrue(isinstance(self.weather.today['snow'], dict))
#     except Exception as e:
#         raise
#     finally:
#         pass
#
#
# def test_wind_is_dictionary(self):
#     """'wind' is a dictionary."""
#     try:
#         self.assertTrue(isinstance(self.weather.today['wind'], dict))
#     except Exception as e:
#         raise
#     finally:
#         pass
#
#
# def test_humidity_is_int(self):
#     """'humidity' is an int."""
#     try:
#         self.assertTrue(int(self.weather.today['humidity']))
#     except Exception as e:
#         raise
#     finally:
#         pass
#
#
# def test_pressure_is_dictionary(self):
#     """'pressure' is a dictionary."""
#     try:
#         self.assertTrue(isinstance(self.weather.today['pressure'], dict))
#     except Exception as e:
#         raise
#     finally:
#         pass
#
#
# def test_temperature_is_dictionary(self):
#     """'temperature' is a dictionary."""
#     try:
#         self.assertTrue(isinstance(self.weather.today['temperature'],
#                                    dict))
#     except Exception as e:
#         raise
#     finally:
#         pass
#
#
# def test_status_is_string(self):
#     """'status' is a string."""
#     try:
#         self.assertTrue(isinstance(self.weather.today['status'], str))
#     except Exception as e:
#         raise
#     finally:
#         pass
#
#
# def test_detailed_status_is_string(self):
#     """detailed_status is a string."""
#     try:
#         self.assertTrue(isinstance(self.weather.today['detailed_status'],
#                                    str))
#     except Exception as e:
#         raise
#     finally:
#         pass
#
#
# def test_weather_code_is_int(self):
#     """weather_code is an int."""
#     try:
#         self.assertTrue(int(self.weather.today['weather_code']))
#     except Exception as e:
#         raise
#     finally:
#         pass
#
#
# def test_weather_icon_name_is_string(self):
#     """weather_icon_name is a string."""
#     try:
#         self.assertTrue(isinstance(self.weather.today['weather_icon_name'],
#                                    str))
#     except Exception as e:
#         raise
#     finally:
#         pass
#
#
# def test_dewpoint_is_float_or_none(self):
#     """'dewpoint' is a float or None."""
#     try:
#         self.assertTrue(isinstance(self.weather.today['dewpoint'], float)
#                         or isinstance(self.weather.today['dewpoint'],
#                                       type(None)))
#     except Exception as e:
#         raise
#     finally:
#         pass
#
#
# def test_humidex_is_float_or_none(self):
#     """'humidex' is a float or None."""
#     try:
#         self.assertTrue(isinstance(self.weather.today['humidex'], float)
#                         or isinstance(self.weather.today['humidex'],
#                                       type(None)))
#     except Exception as e:
#         raise
#     finally:
#         pass
#
#
# def test_heat_index_is_float_or_none(self):
#     """'heat_index' is a float or None."""
#     try:
#         self.assertTrue(isinstance(self.weather.today['heat_index'], float)
#                         or isinstance(self.weather.today['heat_index'],
#                                       type(None)))
#     except Exception as e:
#         raise
#     finally:
#         pass
