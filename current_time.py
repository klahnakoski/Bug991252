from datetime import datetime
import string
import random

diff = datetime.utcnow() - datetime(1970, 1, 1)
millis = long(diff.total_seconds()) * 1000L + long(diff.microseconds / 1000)

def random_string(length):
    result = []
    for i in range(0, length):
        result.append(random.Random().choice(string.ascii_letters + string.digits))
    return "".join(result)

with open("subdir/current_time.js", "w") as f:
    f.write("current_time="+str(millis)+";\nvar random_filler=\""+(random_string(2**11))+"\";")


for i in range(100):
    with open("subdir/"+str(i)+".js", "w") as f:
        f.write("var random_filler=\""+(random_string(2**11))+"\";")

