from datetime import datetime

diff = datetime.utcnow() - datetime(1970, 1, 1)
millis = long(diff.total_seconds()) * 1000L + long(diff.microseconds / 1000)

with open("current_time.js", "w") as f:
    f.write("var current_time="+str(millis)+";")
