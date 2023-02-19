from datetime import datetime, timedelta

n =datetime.now().replace(microsecond=0)
d = timedelta(1)
s = n - d
diff = n - s
print(diff.total_seconds())