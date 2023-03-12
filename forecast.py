from pyowm import OWM
from pyowm.utils.config import get_default_config
from pyowm.utils import timestamps

config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM('4bd23318872cb802ce048987586d32cc', config_dict)
mgr = owm.weather_manager()


def get_weather():
    three_h_forecaster = mgr.forecast_at_place('Moscow, Russia', '3h')
    tomorrow_at_two = timestamps.tomorrow(14, 0)
    weather = three_h_forecaster.get_weather_at(tomorrow_at_two)
    return weather
