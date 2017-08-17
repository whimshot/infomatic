"""Testing methods for the Weather class."""
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
    assert isinstance(weatherdict['temperature'], dict)
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


def test_clouds(weatherdict):
    """Is the reference_time a valid int value."""
    assert isinstance(weatherdict['clouds'], int)
    assert isinstance(weatherdict.clouds, int)
    assert 0 <= weatherdict.clouds <= 100


def test_rain(weatherdict):
    """Is the rain a dict."""
    assert isinstance(weatherdict['rain'], dict)
    assert isinstance(weatherdict.rain,
                      float) or isinstance(weatherdict.rain, type(None))


def test_snow(weatherdict):
    """Is the snow a dict."""
    assert isinstance(weatherdict['snow'], dict)
    assert isinstance(weatherdict.snow,
                      float) or isinstance(weatherdict.snow, type(None))


def test_wind(weatherdict):
    """Is the wind a dict."""
    assert isinstance(weatherdict['wind'], dict)
    assert isinstance(weatherdict.wind, dict)


def test_humidity(weatherdict):
    """Test the pressure."""
    assert isinstance(weatherdict['humidity'], int)
    assert isinstance(weatherdict.humidity, int)
    assert 0 <= weatherdict.humidity <= 100


def test_pressure(weatherdict):
    """Test the pressure."""
    assert isinstance(weatherdict['pressure'], dict)
    assert isinstance(weatherdict.pressure, float)


def test_wind(weatherdict):
    """Test the wind."""
    assert isinstance(weatherdict['wind'], dict)
    assert isinstance(weatherdict.wind_speed, float)
    assert isinstance(weatherdict.wind_deg, float)
    assert 0 <= weatherdict.wind_deg <= 360


def test_status(weatherdict):
    """Test the status."""
    assert isinstance(weatherdict['status'], str)
    assert isinstance(weatherdict.status, str)


def test_detailed_status(weatherdict):
    """Test the detailed_status."""
    assert isinstance(weatherdict['detailed_status'], str)
    assert isinstance(weatherdict.detailed_status, str)


def test_status_icon_url(weatherdict):
    """Test the status_icon_url."""
    assert isinstance(weatherdict['weather_icon_name'], str)
    assert isinstance(weatherdict.status_icon_url, str)
