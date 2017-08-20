"""Docstring goes here."""
import configparser
import datetime
import logging
import logging.handlers

from dateutil import tz
from kivy.app import App
from kivy.clock import Clock
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import AsyncImage
from kivy.uix.label import Label

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 800)
Config.set('graphics', 'height', 480)
Window.size = (800, 480)
config = configparser.ConfigParser()

try:
    assert __name__ == '__main__'
    config.read('weather/weather.conf')
except AssertionError:
    logger = logging.getLogger(__name__)
    config.read('weather/weather.conf')
else:
    MAXLOGSIZE = config.getint('Logging', 'maxlogsize')
    ROTATIONCOUNT = config.getint('Logging', 'rotationcount')
    LOGFILE = config.get('Logging', 'logfile')

    # create logger
    logger = logging.getLogger(__name__)
    # logger.setLevel(logging.INFO)
    logger.setLevel(logging.DEBUG)
    # create file handler which logs even debug messages
    logger_fh = logging.handlers.RotatingFileHandler(LOGFILE,
                                                     maxBytes=MAXLOGSIZE,
                                                     backupCount=ROTATIONCOUNT)
    logger_fh.setLevel(logging.DEBUG)
    # create console handler with a higher log level
    logger_ch = logging.StreamHandler()
    logger_ch.setLevel(logging.ERROR)
    # create formatter and add it to the handlers
    logger_formatter = logging.Formatter('%(asctime)s'
                                         + ' %(levelname)s'
                                         + ' %(name)s[%(process)d]'
                                         + ' %(message)s')
    logger_fh.setFormatter(logger_formatter)
    logger_ch.setFormatter(logger_formatter)
    # add the handlers to the logger
    logger.addHandler(logger_fh)
    logger.addHandler(logger_ch)
finally:
    import weather.weather

deg_cel = u' \N{DEGREE SIGN}C'


class WeatherBoxTitle(Label):
    """docstring for WeatherBox."""

    def __init__(self, **kwargs):
        """Setup that weatherbox."""
        super().__init__(**kwargs)
        try:
            pass
        except Exception as e:
            raise
        finally:
            pass


class WeatherLabel(Label):
    """docstring for WeatherLabel."""

    def __init__(self, **kwargs):
        """Setup that weatherbox."""
        super().__init__(**kwargs)
        try:
            pass
        except Exception as e:
            raise
        finally:
            pass


class TodayLabel(WeatherLabel):
    """docstring for TodayLabel."""

    def __init__(self, **kwargs):
        """Setup that weatherbox."""
        super().__init__(**kwargs)
        try:
            pass
        except Exception as e:
            raise
        finally:
            pass


class TodayHeader(WeatherLabel):
    """docstring for TodayHeader."""

    def __init__(self, **kwargs):
        """Setup that weatherbox."""
        super().__init__(**kwargs)
        try:
            pass
        except Exception as e:
            raise
        finally:
            pass


class TodayGrid(GridLayout):
    """docstring for TodayGrid."""

    def __init__(self, **kwargs):
        """Setup that weatherbox."""
        super().__init__(**kwargs)
        try:
            self.from_zone = tz.tzutc()
            self.to_zone = tz.tzlocal()
            w = weather.weather.Weather()
            wd = w.today
            self.widgets = {}
            _status = TodayLabel(text=wd.detailed_status)
            self.add_widget(_status)
            self.widgets['detailed_status'] = _status

            _icon = AsyncImage(source=wd.status_icon_url)
            self.add_widget(_icon)
            self.widgets['status_icon_url'] = _icon

            self.add_widget(TodayHeader(text='High'))
            _high_temp = TodayLabel(text=str(wd.temp_high) + deg_cel)
            self.add_widget(_high_temp)
            self.widgets['temp_high'] = _high_temp

            self.add_widget(TodayHeader(text='Low'))
            _low_temp = TodayLabel(text=str(wd.temp_low) + deg_cel)
            self.add_widget(_low_temp)
            self.widgets['temp_low'] = _low_temp

            self.add_widget(TodayHeader(text='Currently'))
            _temperature = TodayLabel(text=str(wd.temperature) + deg_cel)
            self.add_widget(_temperature)
            self.widgets['temperature'] = _temperature

            self.add_widget(TodayHeader(text='Humidity'))
            _humidity = TodayLabel(text=str(wd.humidity) + '%')
            self.add_widget(_humidity)
            self.widgets['humidity'] = _humidity

            self.add_widget(TodayHeader(text='Sunrise'))
            _sunrise = datetime.datetime.fromtimestamp(wd.sunrise_time)
            _sunrise_widget = TodayLabel(
                text=_sunrise.strftime('%I:%M:%S %p'))
            self.add_widget(_sunrise_widget)
            self.widgets['sunrise_time'] = _sunrise_widget

            self.add_widget(TodayHeader(text='Sunset'))
            _sunset = datetime.datetime.fromtimestamp(wd.sunset_time)
            _sunset_widget = TodayLabel(text=_sunset.strftime('%I:%M:%S %p'))
            self.add_widget(_sunset_widget)
            self.widgets['sunset_time'] = _sunset_widget
            weather.weather.logger.info('Today: %s %s %s %s %s %s %s %s %s',
                                        wd.reference_time,
                                        wd.detailed_status, wd.status_icon_url,
                                        str(wd.temp_high),
                                        str(wd.temp_low),
                                        str(wd.temperature),
                                        str(wd.humidity),
                                        _sunrise.strftime('%I:%M:%S %p'),
                                        _sunset.strftime('%I:%M:%S %p'))
            Clock.schedule_interval(self.update, 300)
        except Exception as e:
            raise
        finally:
            pass

    def update(self, dt):
        try:
            w = weather.weather.Weather()
            wd = w.today
            self.widgets['detailed_status'].text = wd.detailed_status
            self.widgets['status_icon_url'].source = wd.status_icon_url
            self.widgets['status_icon_url'].reload()
            self.widgets['temp_high'].text = str(wd.temp_high) + deg_cel
            self.widgets['temp_low'].text = str(wd.temp_low) + deg_cel
            self.widgets['temperature'].text = str(
                wd.temperature) + deg_cel
            self.widgets['humidity'].text = str(wd.humidity) + '%'
            _sunrise = datetime.datetime.fromtimestamp(wd.sunrise_time)
            self.widgets['sunrise_time'].text = _sunrise.strftime(
                '%I:%M:%S %p')
            _sunset = datetime.datetime.fromtimestamp(wd.sunset_time)
            self.widgets['sunset_time'].text = _sunset.strftime(
                '%I:%M:%S %p')
            weather.weather.logger.info(
                'Today Updated: %s %s %s %s %s %s %s %s %s',
                wd.reference_time,
                wd.detailed_status, wd.status_icon_url,
                str(wd.temp_high),
                str(wd.temp_low),
                str(wd.temperature),
                str(wd.humidity),
                _sunrise.strftime('%I:%M:%S %p'),
                _sunset.strftime('%I:%M:%S %p'))
        except Exception as e:
            raise
        finally:
            pass


class TodayBox(BoxLayout):
    """docstring for WeatherBox."""

    def __init__(self, **kwargs):
        """Setup that weatherbox."""
        super().__init__(**kwargs)
        self.bt = WeatherBoxTitle()
        self.bt.text = "Today's Weather"
        self.add_widget(self.bt)
        self.tg = TodayGrid()
        self.add_widget(self.tg)
        try:
            pass
        except Exception as e:
            raise
        finally:
            pass


class ForecastNumeric(WeatherLabel):
    """docstring for TodayLabel."""

    def __init__(self, **kwargs):
        """Setup that weatherbox."""
        super().__init__(**kwargs)
        try:
            pass
        except Exception as e:
            raise
        finally:
            pass


class ForecastDay(WeatherLabel):
    """docstring for TodayLabel."""

    def __init__(self, **kwargs):
        """Setup that weatherbox."""
        super().__init__(**kwargs)
        try:
            pass
        except Exception as e:
            raise
        finally:
            pass


class ForecastHeader(WeatherLabel):
    """docstring for TodayHeader."""

    def __init__(self, **kwargs):
        """Setup that weatherbox."""
        super().__init__(**kwargs)
        try:
            pass
        except Exception as e:
            raise
        finally:
            pass


class ForecastStatus(WeatherLabel):
    """docstring for TodayHeader."""

    def __init__(self, **kwargs):
        """Setup that weatherbox."""
        super().__init__(**kwargs)
        try:
            pass
        except Exception as e:
            raise
        finally:
            pass


class StatusHeader(ForecastStatus):
    """docstring for TodayHeader."""

    def __init__(self, **kwargs):
        """Setup that weatherbox."""
        super().__init__(**kwargs)
        try:
            pass
        except Exception as e:
            raise
        finally:
            pass


class ForecastGrid(GridLayout):
    """docstring for TodayHeader."""

    def __init__(self, **kwargs):
        """Setup that weatherbox."""
        super().__init__(**kwargs)
        try:
            self.add_widget(ForecastHeader(text=''))
            self.add_widget(ForecastHeader(text=''))
            self.add_widget(ForecastHeader(text='High'))
            self.add_widget(ForecastHeader(text='Low'))
            self.add_widget(ForecastHeader(text='Pressure'))
            self.add_widget(StatusHeader(text='Forecast'))
            w = weather.weather.Weather()
            self.grid = []
            for wd in w.forecasts:
                _row = {}
                _date = datetime.datetime.fromtimestamp(wd.reference_time)
                _day = ForecastDay(text=_date.strftime('%A'))
                self.add_widget(_day)
                _row['reference_time'] = _day

                _icon = AsyncImage(source=wd.status_icon_url)
                self.add_widget(_icon)
                _row['status_icon_url'] = _icon

                _high_temp = ForecastNumeric(text=str(wd.temp_high) + deg_cel)
                self.add_widget(_high_temp)
                _row['temp_high'] = _high_temp

                _low_temp = ForecastNumeric(text=str(wd.temp_low) + deg_cel)
                self.add_widget(_low_temp)
                _row['temp_low'] = _low_temp

                _pressure = ForecastNumeric(text=str(wd.pressure))
                self.add_widget(_pressure)
                _row['pressure'] = _pressure

                _detailed_status = ForecastStatus(text=wd.detailed_status)
                self.add_widget(_detailed_status)
                _row['detailed_status'] = _detailed_status
                self.grid.append(_row)
                weather.weather.logger.info('Forecast: %s %s %s %s %s %s %s',
                                            wd.reference_time,
                                            _date.strftime(
                                                '%A'), wd.status_icon_url,
                                            str(wd.temp_high),
                                            str(wd.temp_low),
                                            str(wd.pressure),
                                            wd.detailed_status)
            Clock.schedule_interval(self.update, 3600)
        except Exception as e:
            raise
        finally:
            pass

    def update(self, dt):
        try:
            _w = weather.weather.Weather()
            _forecasts = _w.forecasts
            for wd, row in zip(_forecasts, self.grid):
                _date = datetime.datetime.fromtimestamp(wd.reference_time)
                _day = ForecastDay(text=_date.strftime('%A'))
                row['reference_time'].text = _date.strftime('%A')
                row['status_icon_url'].source = wd.status_icon_url
                row['status_icon_url'].reload()
                row['temp_high'].text = str(wd.temp_high) + deg_cel
                row['temp_low'].text = str(wd.temp_low) + deg_cel
                row['pressure'].text = str(wd.pressure)
                row['detailed_status'].text = wd.detailed_status
                weather.weather.logger.info('Forecast: %s %s %s %s %s %s %s',
                                            wd.reference_time,
                                            _date.strftime('%A'),
                                            wd.status_icon_url,
                                            str(wd.temp_high),
                                            str(wd.temp_low),
                                            str(wd.pressure),
                                            wd.detailed_status)
        except Exception as e:
            raise
        finally:
            pass


class ForecastBox(BoxLayout):
    """docstring for WeatherBox."""

    def __init__(self, **kwargs):
        """Setup that weatherbox."""
        super().__init__(**kwargs)
        try:
            self.bt = WeatherBoxTitle()
            self.bt.text = "Weekly Forecast"
            self.add_widget(self.bt)
            self.fg = ForecastGrid()
            self.add_widget(self.fg)

        except Exception as e:
            raise
        finally:
            pass


class WeatherBox(BoxLayout):
    """docstring for WeatherBox."""

    def __init__(self, **kwargs):
        """Setup that weatherbox."""
        super().__init__(**kwargs)
        self.tb = TodayBox()
        self.add_widget(self.tb)
        self.fb = ForecastBox()
        self.add_widget(self.fb)
        try:
            pass
        except Exception as e:
            raise
        finally:
            pass


class WeatherApp(App):
    """docstring for WeatherApp."""

    def build(self):
        """Build the app."""
        try:
            wb = WeatherBox()
            return wb
        except Exception as e:
            raise
        finally:
            pass


if __name__ == '__main__':
    WeatherApp().run()
