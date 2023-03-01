from datetime import datetime, timedelta


def get_formatted_date(date_posted):
    now = datetime.now()
    hours = int(''.join([num for num in date_posted if num.isdigit()]))
    time = now - timedelta(hours=hours)
    time = time.strftime('%d/%m/%Y')
    return time
