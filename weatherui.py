"""Docstring goes here."""
import datetime
import pprint

from dateutil import tz
from kivy.app import App
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import AsyncImage
from kivy.uix.label import Label

import weather

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 800)
Config.set('graphics', 'height', 480)
Window.size = (800, 480)

deg_cel = u'\N{DEGREE SIGN}C'


class TodayTitle(Label):
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
    """docstring for WeatherBox."""

    def __init__(self, **kwargs):
        """Setup that weatherbox."""
        super().__init__(**kwargs)
        try:
            self.from_zone = tz.tzutc()
            self.to_zone = tz.tzlocal()
            w = weather.Weather()
            wd = w.today
            _status = TodayHeader(text=wd.detailed_status)
            self.add_widget(_status)
            _icon = AsyncImage(source=wd.status_icon_url)
            self.add_widget(_icon)
            self.add_widget(TodayHeader(text='High'))
            _high_temp = TodayLabel(text=str(wd.temp_high) + deg_cel)
            self.add_widget(_high_temp)
            self.add_widget(TodayHeader(text='Low'))
            _low_temp = TodayLabel(text=str(wd.temp_low) + deg_cel)
            self.add_widget(_low_temp)
            self.add_widget(TodayHeader(text='Currently'))
            _current_temp = TodayLabel(text=str(wd.temperature) + deg_cel)
            self.add_widget(_current_temp)
            self.add_widget(TodayHeader(text='Humidity'))
            _humidity = TodayLabel(text=str(wd.humidity) + '%')
            self.add_widget(_humidity)
            self.add_widget(TodayHeader(text='Sunrise'))
            _sunrise = datetime.datetime.fromtimestamp(wd.sunrise_time)
            _sunrise_widget = TodayLabel(
                text=_sunrise.strftime('%I:%M:%S %p'))
            self.add_widget(_sunrise_widget)
            self.add_widget(TodayHeader(text='Sunset'))
            _sunset = datetime.datetime.fromtimestamp(wd.sunset_time)
            _sunset_widget = TodayLabel(text=_sunset.strftime('%I:%M:%S %p'))
            self.add_widget(_sunset_widget)
            self.data = [_status, _icon, _high_temp, _low_temp, _current_temp,
                         _humidity, _sunrise_widget, _sunset_widget]
        except Exception as e:
            raise
        finally:
            pass


class TodayBox(BoxLayout):
    """docstring for WeatherBox."""

    def __init__(self, **kwargs):
        """Setup that weatherbox."""
        super().__init__(**kwargs)
        tl = TodayTitle()
        tl.text = "Today's Weather"
        self.add_widget(tl)
        tg = TodayGrid()
        self.add_widget(tg)
        try:
            pass
        except Exception as e:
            raise
        finally:
            pass


class ForecastBox(BoxLayout):
    """docstring for WeatherBox."""

    def __init__(self, **kwargs):
        """Setup that weatherbox."""
        super().__init__(**kwargs)
        tl = TodayTitle()
        tl.text = "Weekly Forecast"
        self.add_widget(tl)
        try:
            pass
        except Exception as e:
            raise
        finally:
            pass


class WeatherBox(BoxLayout):
    """docstring for WeatherBox."""

    def __init__(self, **kwargs):
        """Setup that weatherbox."""
        super().__init__(**kwargs)
        tb = TodayBox()
        self.add_widget(tb)
        fb = ForecastBox()
        self.add_widget(fb)
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
