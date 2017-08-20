"""Docstring goes here."""
import configparser
import logging
import logging.handlers

import kivy.app
import kivy.clock
import kivy.core.window
import kivy.uix.boxlayout
import kivy.uix.button
import kivy.uix.carousel
import kivy.uix.image
import kivy.uix.label
import weather.weatherui
import mbta.mbtaui
import maps.maps

kivy.config.Config.set('graphics', 'resizable', 0)
kivy.config.Config.set('graphics', 'width', 800)
kivy.config.Config.set('graphics', 'height', 480)
kivy.core.window.Window.size = (800, 480)
config = configparser.ConfigParser()


class ToolBar(kivy.uix.boxlayout.BoxLayout):
    """docstring for ToolBar."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pass


class InfoCarousel(kivy.uix.carousel.Carousel):
    """docstring for InfoCarousel."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.loop = True
        self.weather = weather.weatherui.WeatherBox()
        self.add_widget(self.weather)
        self.bus = mbta.mbtaui.BusBox()
        self.add_widget(self.bus)
        self.maps = maps.maps.MapLayout()
        self.add_widget(self.maps)


class InfoBox(kivy.uix.boxlayout.BoxLayout):
    """docstring for InfoBox."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.carousel = InfoCarousel()
        self.add_widget(self.carousel)
        self.toolbar = ToolBar()
        self.add_widget(self.toolbar)


class InfoMaticApp(kivy.app.App):
    """docstring for InfoMaticApp."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pass

    def build(self):
        """Docstring"""
        ib = InfoBox()
        return ib


if __name__ == '__main__':
    InfoMaticApp().run()
