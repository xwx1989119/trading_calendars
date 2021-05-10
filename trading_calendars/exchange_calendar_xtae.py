#
# Copyright 2018 Quantopian, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from datetime import time
import pandas as pd
from pytz import timezone, UTC
from .trading_calendar import TradingCalendar, HolidayCalendar
from .tase_holidays import (Purim, PassoverEve, Passover, Passover2Eve,
                            Passover2, PentecostEve, Pentecost, FastDay,
                            MemorialDay, IndependenceDay, NewYearsEve, NewYear,
                            NewYear2, YomKippurEve, YomKippur, SukkothEve,
                            Sukkoth, SimchatTorahEve, SimchatTorah)

# All holidays are defined as ad-hoc holidays for each year since there is
# currently no support for Hebrew calendar holiday rules in pandas.


class XTAEExchangeCalendar(TradingCalendar):
    """
    Exchange calendar for TASE Stock Exchange.

    Open/close times are continuous trading times valid Mon-Thu for Shares
    Group A. Trading schedule differs on Sundays.

    Open Time: 9:59 AM, Asia/Tel_Aviv (randomly between 9:59 and 10:00).
    Close Time: 5:14 PM, Asia/Tel_Aviv (randomly between 5:14 and 5:15).

    Regularly-Observed Holidays (not necessarily in order):
    - Purim
    - Passover Eve
    - Passover
    - Passover II Eve
    - Passover II
    - Memorial Day
    - Independence Day
    - Pentecost Eve
    - Pentecost
    - Tisha B'Av
    - New Year's Eve
    - New Year
    - New Year II
    - Yom Kippur Eve
    - Yom Kippur
    - Sukkoth Eve
    - Sukkoth
    - Simchat Torah Eve
    - Simchat Torah

    Note these dates are only checked against 2019-2023.

    https://info.tase.co.il/eng/about_tase/corporate/pages/vacation_schedule.aspx

    Daylight Saving Time in Israel comes into effect on the Friday before the
    last Sunday in March, and lasts until the last Sunday in October. During the
    Daylight Saving time period the clock will be UTC+3, and UTC+2 for the rest
    of the year.
    """  # noqa
    start_date = pd.Timestamp('2019-01-01', tz=UTC)

    name = 'XTAE'

    tz = timezone('Asia/Tel_Aviv')

    open_times = (
        (None, time(10, 0)),
    )

    close_times = (
        (None, time(17, 15)),
    )

    @property
    def regular_holidays(self):
        return HolidayCalendar([
            Purim,
            PassoverEve,
            Passover,
            Passover2Eve,
            Passover2,
            MemorialDay,
            IndependenceDay,
            PentecostEve,
            Pentecost,
            FastDay,
            NewYearsEve,
            NewYear,
            NewYear2,
            YomKippurEve,
            YomKippur,
            SukkothEve,
            Sukkoth,
            SimchatTorahEve,
            SimchatTorah
        ])

    @property
    def adhoc_holidays(self):
        return [
            # 2019
            # Election Day
            pd.Timestamp('2019-04-09', tz='Asia/Jerusalem'),
            # Election Day
            pd.Timestamp('2019-09-17', tz='Asia/Jerusalem'),
            # 2020
            # Election Day
            pd.Timestamp('2020-03-02', tz='Asia/Jerusalem'),
            # 2021
            # Election Day
            pd.Timestamp('2021-03-23', tz='Asia/Jerusalem')
        ]

    @property
    def weekmask(self):
        return '1111001'
