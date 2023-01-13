from datetime import datetime, timedelta
import random

def get_random_time():
 # get the current time
 now = datetime.now()
 # set the time range, one week before and after
 start_time = now - timedelta(weeks=1)
 end_time = now + timedelta(weeks=1)
 # generate a random time within the range
 random_time = start_time + timedelta(seconds=random.randint(0, int((end_time - start_time).total_seconds())))
 random_time_iso = random_time.isoformat()
 print('random_time_iso ...' , random_time_iso)
 return random_time_iso