from flatlib import const
from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos

AY_FAGAN_BRADLEY = "Ayanamsa Fagan Bradley"
import swisseph
from flatlib import const
SWE_AYANAMSAS = {const.AY_KRISHNAMURTI}

date = Datetime('2015/03/13', '17:00', '+00:00')
pos = GeoPos('38n32', '8w54')
chart = Chart(date, pos)
chart = Chart(date, pos, mode=const.AY_KRISHNAMURTI)

# Get a copy of the chart in the sidereal zodiac
sid_chart = chart.to_sidereal_zodiac(const.AY_LAHIRI)
print(sid_chart.get(const.SATURN))
# Get objects and houses from the chart
sun = chart.get(const.SUN)
house3 = chart.get(const.HOUSE3)