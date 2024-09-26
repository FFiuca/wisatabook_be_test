import sys, os
import datetime
import calendar

def paginate_model(page, limit=10):
    offset = (page-1)* limit
    next_row = page* limit
    return [offset, next_row]

def messageError(e):
    exc_type, exc_obj, exc_tb = sys.exc_info()
    print('messageError', exc_type, exc_obj, exc_tb)
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)
    print(fname)
    fname= fname[1]
    return "An exception of type {} occured: {}. {}. {}. {}".format(type(e).__name__, e, exc_type, fname, exc_tb.tb_lineno)


def day_of_week(date):
    date_obj = datetime.datetime.strptime(date, "%Y-%m-%d")
    day_of_week = date_obj.weekday()

    return calendar.day_name[day_of_week]
