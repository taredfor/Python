from datetime import datetime
import pytz
fmt = '%d-%m-%Y %H:%M:%S'
tz = pytz.timezone('Europe/London')
current_time = datetime.now(tz).strftime(fmt)
print(current_time)