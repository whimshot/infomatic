"""Docstring goes here."""
import atexit
import configparser
import logging
import logging.handlers
import os

import kivy.app
import kivy.clock
import kivy.core.window
import kivy.uix.boxlayout
import kivy.uix.button
import kivy.uix.carousel
import kivy.uix.image
import kivy.uix.label
import kivy.uix.togglebutton

import maps.maps
import mbta.mbtaui
import weather.weatherui

kivy.config.Config.set('graphics', 'resizable', 0)
kivy.config.Config.set('graphics', 'width', 800)
kivy.config.Config.set('graphics', 'height', 480)
kivy.core.window.Window.size = (800, 480)
config = configparser.ConfigParser()

config = configparser.ConfigParser()

try:
    assert __name__ == '__main__'
    config.read('infomatic.conf')
except AssertionError:
    logger = logging.getLogger(__name__)
    config.read('infomatic.conf')
else:
    pass
finally:
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


pid = str(os.getpid())
pidfile = "/tmp/healthstats.pid"
with open(pidfile, 'w') as pf:
    pf.write(pid)


def cleanup():
    """Cleanup the pid file."""
    if os.path.isfile(pidfile):
        os.unlink(pidfile)


atexit.register(cleanup)    # Register with atexit


class TglBtn(kivy.uix.togglebutton.ToggleButton):
    """The Carousel to hold our information slides."""

    def __init__(self, **kwargs):
        """Build that Weather Slide."""
        super().__init__(**kwargs)
        try:
            self.logger = \
                logging.getLogger('InfoBox.'
                                  + self.__class__.__name__)

            self.logger.debug("Creating an instance of " +
                              self.__class__.__name__)
            self.text = 'Scroll'
        except Exception:
            self.logger.exception("Caught exception.")
        finally:
            pass

    def toggle(self):
        """Toggle that button."""
        try:
            if self.state == 'normal':
                self.text = 'Scroll'
            else:
                self.text = 'Scrolling'
        except Exception:
            raise
        finally:
            pass


class TglBtn(kivy.uix.togglebutton.ToggleButton):
    """The Carousel to hold our information slides."""

    def __init__(self, **kwargs):
        """Build that Weather Slide."""
        super(TglBtn, self).__init__(**kwargs)
        try:
            self.logger = \
                logging.getLogger('InfoBox.'
                                  + self.__class__.__name__)

            self.logger.debug("Creating an instance of " +
                              self.__class__.__name__)
            self.text = 'Scroll'
        except Exception:
            self.logger.exception("Caught exception.")
        finally:
            pass

    def toggle(self):
        """Toggle that button."""
        try:
            if self.state == 'normal':
                self.text = 'Scroll'
            else:
                self.text = 'Scrolling'
        except Exception:
            raise
        finally:
            pass


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

    def next_slide_please(self, dt):
        """Go to the next slide in the carousel."""
        try:
            if self.parent.toolbar.toggle.state == 'down':
                self.load_next(mode='next')
        except Exception:
            logger.exception("Failed to load next slide.")
        finally:
            pass


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
        kivy.clock.Clock.schedule_interval(ib.carousel.next_slide_please, 10)
        return ib


if __name__ == '__main__':
    InfoMaticApp().run()
