import radar
import datetime

# Basic usage
print(radar.random_datetime())

# Specify date range
specifiedDate = radar.random_date(
    start = datetime.datetime(year=2000, month=5, day=24),
    stop = datetime.datetime(year=2013, month=5, day=24)
)
print(specifiedDate)