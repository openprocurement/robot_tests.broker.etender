# -*- coding: utf-8 -

from iso8601 import parse_date
from datetime import datetime, date, time, timedelta
import dateutil.parser


def get_all_etender_dates(initial_tender_data, key, subkey=None):
    tender_period = initial_tender_data.data.tenderPeriod
    start_dt = dateutil.parser.parse(tender_period['startDate'])
    end_dt = dateutil.parser.parse(tender_period['endDate'])
    data = {
        'StartDate': {
            'date': start_dt.strftime("%d-%m-%Y"),
            'time': start_dt.strftime("%H:%M"),
        },
        'EndDate': {
            'date': end_dt.strftime("%d-%m-%Y"),
            'time': end_dt.strftime("%H:%M"),
        },
    }
    if 'enquiryPeriod' in initial_tender_data.data:
        enquiry_period = initial_tender_data.data.enquiryPeriod
        end_period = dateutil.parser.parse(enquiry_period['endDate'])
        data['EndPeriod'] = {
            'date': end_period.strftime("%d-%m-%Y"),
            'time': end_period.strftime("%H:%M"),
        }
    dt = data.get(key, {})
    return dt.get(subkey) if subkey else dt


def convert_date_to_etender_format(isodate):
    iso_dt = parse_date(isodate)
    date_string = iso_dt.strftime("%d-%m-%Y")
    return date_string


def convert_datetime_for_delivery(isodate):
    iso_dt = parse_date(isodate)
    date_string = iso_dt.strftime("%Y-%m-%d %H:%M")
    return date_string


def convert_time_to_etender_format(isodate):
    iso_dt = parse_date(isodate)
    time_string = iso_dt.strftime("%H:%M")
    return time_string


def float_to_string_2f(value):
    return '{:.2f}'.format(value)


def string_to_float(string):
    return float(string)


def change_data(initial_data):
    #TODO: remove redundant hardcoded values
    initial_data['data']['items'][0]['deliveryAddress']['locality'] = u"м. Київ"
    initial_data['data']['items'][0]['deliveryAddress']['region'] = u"Київська область"
    initial_data['data']['procuringEntity']['name'] = u"TenderOwner#"
    return initial_data


def convert_etender_date_to_iso_format(date_time_from_ui):
    new_timedata = datetime.strptime(date_time_from_ui, '%d-%m-%Y, %H:%M')
    new_date_time_string = new_timedata.strftime("%Y-%m-%d %H:%M:%S.%f")
    return new_date_time_string


def convert_common_string_to_etender_string(string):
    dict = get_helper_dictionary()
    for key, val in dict.iteritems():
        if val == string:
            return key
    return string


def convert_etender_string_to_common_string(string):
    dict = get_helper_dictionary()
    return dict.get(string, string)


def get_helper_dictionary():
    return {
        u"кг.": u"кілограм",
        u"грн.": u"UAH",
        u"(включаючи ПДВ)": True,
    }
