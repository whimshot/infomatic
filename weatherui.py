"""Docstring goes here."""
import pprint

from kivy.app import App
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

import weather

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 800)
Config.set('graphics', 'height', 480)
Window.size = (800, 480)


class WeatherLabel(Label):
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


class WeatherBox(BoxLayout):
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


class WeatherApp(App):
    """docstring for WeatherApp."""

    def build(self):
        """Build the app."""
        try:
            w = weather.Weather()
            pp = pprint.PrettyPrinter(indent=4)
            foo = pp.pformat(w.today)
            wl = WeatherLabel()
            wl.text = foo
            wb = WeatherBox()
            wb.add_widget(wl)
            return wb
        except Exception as e:
            raise
        finally:
            pass


if __name__ == '__main__':
    WeatherApp().run()
