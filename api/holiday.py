import calendar
from datetime import date
import holidays

from flask_restful import Resource
from flask import jsonify


class UkraineHolidays(holidays.Ukraine):

    def _populate(self, year):
        self[date(year, 6, 17)] = "Вихідний в честь Трійці"
        self[date(year, 8, 26)] = "Вихідний в честь Дня незалежності України"


class Holiday(Resource):

    def get(self, year, month, day):
        all_holiday = holidays.UA() + UkraineHolidays()
        r_date = '{}-{}-{}'.format(year, month, day)

        if calendar.weekday(year, month, day) in (5, 6):
            is_holiday = True
            comment = 'Вихiдний день'
            day_type = 'weekend'
        elif r_date in all_holiday:
            is_holiday = True
            comment = all_holiday.get(r_date)
            day_type = 'holiday'
        else:
            is_holiday = False
            comment = 'Робочий день'
            day_type = 'workday'

        context = {'is_holiday': is_holiday, 'comment': comment, 'day_type': day_type}
        return jsonify(context)









