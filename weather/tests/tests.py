"""Testing methods for the Weather class."""
import unittest
import weather


class TestOWMWeatherDict(unittest.TestCase):
    """docstring for TestOWMWeatherDict."""

    def setUp(self):
        """Setup for the tests."""
        try:
            self.weather_keys = ['reference_time', 'sunset_time',
                                 'sunrise_time', 'clouds', 'rain',
                                 'snow', 'wind', 'humidity', 'pressure',
                                 'temperature', 'status', 'detailed_status',
                                 'weather_code', 'weather_icon_name',
                                 'visibility_distance', 'dewpoint',
                                 'humidex', 'heat_index']
            self.weather = weather.Weather()
            self.weatherdict = self.weather.today
        except Exception as e:
            raise
        finally:
            pass

    def test_properties(self):
        self.assertTrue(isinstance(self.weatherdict.temperature, float))
        self.assertTrue(isinstance(self.weatherdict.temp_high, float))
        self.assertTrue(isinstance(self.weatherdict.temp_low, float))


class TestTodayAttributes(unittest.TestCase):
    """docstring for TestTodaysWeather."""

    def setUp(self):
        """Setup for the tests."""
        try:
            self.weather_keys = ['reference_time', 'sunset_time',
                                 'sunrise_time', 'clouds', 'rain',
                                 'snow', 'wind', 'humidity', 'pressure',
                                 'temperature', 'status', 'detailed_status',
                                 'weather_code', 'weather_icon_name',
                                 'visibility_distance', 'dewpoint',
                                 'humidex', 'heat_index']
            self.weather = weather.Weather()
        except Exception as e:
            raise
        finally:
            pass

    def test_today_is_dictionary(self):
        """'today' is a dictionary."""
        try:
            self.assertTrue(isinstance(self.weather.today, dict))
        except Exception as e:
            raise
        finally:
            pass

    def test_today_has_necessary_keys(self):
        """'today' has appropriate keys."""
        try:
            self.assertEqual(self.weather_keys,
                             list(self.weather.today.keys()))
        except Exception as e:
            raise
        finally:
            pass

    def test_reference_time_is_int(self):
        """reference_time is an int."""
        try:
            self.assertTrue(int(self.weather.today['reference_time']))
        except Exception as e:
            raise
        finally:
            pass

    def test_sunset_time_is_int_or_none(self):
        """sunset_time is an int or none."""
        try:
            self.assertTrue(isinstance(self.weather.today['sunset_time'], int)
                            or isinstance(self.weather.today['sunset_time'],
                                          type(None)))
        except Exception as e:
            raise
        finally:
            pass

    def test_sunrise_time_is_int_or_none(self):
        """sunrise_time is an int or none."""
        try:
            self.assertTrue(isinstance(self.weather.today['sunrise_time'], int)
                            or isinstance(self.weather.today['sunrise_time'],
                                          type(None)))
        except Exception as e:
            raise
        finally:
            pass

    def test_clouds_is_int(self):
        """'clouds' is an int."""
        try:
            self.assertTrue(int(self.weather.today['clouds']))
        except Exception as e:
            raise
        finally:
            pass

    def test_rain_is_dictionary(self):
        """'rain' is a dictionary."""
        try:
            self.assertTrue(isinstance(self.weather.today['rain'], dict))
        except Exception as e:
            raise
        finally:
            pass

    def test_snow_is_dictionary(self):
        """'snow' is a dictionary."""
        try:
            self.assertTrue(isinstance(self.weather.today['snow'], dict))
        except Exception as e:
            raise
        finally:
            pass

    def test_wind_is_dictionary(self):
        """'wind' is a dictionary."""
        try:
            self.assertTrue(isinstance(self.weather.today['wind'], dict))
        except Exception as e:
            raise
        finally:
            pass

    def test_humidity_is_int(self):
        """'humidity' is an int."""
        try:
            self.assertTrue(int(self.weather.today['humidity']))
        except Exception as e:
            raise
        finally:
            pass

    def test_pressure_is_dictionary(self):
        """'pressure' is a dictionary."""
        try:
            self.assertTrue(isinstance(self.weather.today['pressure'], dict))
        except Exception as e:
            raise
        finally:
            pass

    def test_temperature_is_dictionary(self):
        """'temperature' is a dictionary."""
        try:
            self.assertTrue(isinstance(self.weather.today['temperature'],
                                       dict))
        except Exception as e:
            raise
        finally:
            pass

    def test_status_is_string(self):
        """'status' is a string."""
        try:
            self.assertTrue(isinstance(self.weather.today['status'], str))
        except Exception as e:
            raise
        finally:
            pass

    def test_detailed_status_is_string(self):
        """detailed_status is a string."""
        try:
            self.assertTrue(isinstance(self.weather.today['detailed_status'],
                                       str))
        except Exception as e:
            raise
        finally:
            pass

    def test_weather_code_is_int(self):
        """weather_code is an int."""
        try:
            self.assertTrue(int(self.weather.today['weather_code']))
        except Exception as e:
            raise
        finally:
            pass

    def test_weather_icon_name_is_string(self):
        """weather_icon_name is a string."""
        try:
            self.assertTrue(isinstance(self.weather.today['weather_icon_name'],
                                       str))
        except Exception as e:
            raise
        finally:
            pass

    def test_dewpoint_is_float_or_none(self):
        """'dewpoint' is a float or None."""
        try:
            self.assertTrue(isinstance(self.weather.today['dewpoint'], float)
                            or isinstance(self.weather.today['dewpoint'],
                                          type(None)))
        except Exception as e:
            raise
        finally:
            pass

    def test_humidex_is_float_or_none(self):
        """'humidex' is a float or None."""
        try:
            self.assertTrue(isinstance(self.weather.today['humidex'], float)
                            or isinstance(self.weather.today['humidex'],
                                          type(None)))
        except Exception as e:
            raise
        finally:
            pass

    def test_heat_index_is_float_or_none(self):
        """'heat_index' is a float or None."""
        try:
            self.assertTrue(isinstance(self.weather.today['heat_index'], float)
                            or isinstance(self.weather.today['heat_index'],
                                          type(None)))
        except Exception as e:
            raise
        finally:
            pass


class TestForecastAttributes(unittest.TestCase):
    """docstring for TestForecast."""

    def setUp(self):
        """Setup for the tests."""
        try:
            self.weather_keys = ['reference_time', 'sunset_time',
                                 'sunrise_time', 'clouds', 'rain',
                                 'snow', 'wind', 'humidity', 'pressure',
                                 'temperature', 'status', 'detailed_status',
                                 'weather_code', 'weather_icon_name',
                                 'visibility_distance', 'dewpoint',
                                 'humidex', 'heat_index']
            self.weather = weather.Weather()
        except Exception as e:
            raise
        finally:
            pass

    def test_forecasts(self):
        """'forecasts' is a dictionary of dictionaries."""
        try:
            self.assertTrue(isinstance(self.weather.forecasts, list))
            for __forecast in self.weather.forecasts:
                with self.subTest(__forecast=__forecast):
                    self.assertTrue(isinstance(__forecast, dict))
                    self.assertEqual(self.weather_keys,
                                     list(__forecast.keys()))
        except Exception as e:
            raise
        finally:
            pass


if __name__ == '__main__':
    unittest.main()
