import os
import datetime
import pytz
import re
from pathlib import Path

if __name__ == "__main__":

    eastern=pytz.timezone("US/Eastern")
    et_time=datetime.datetime.now(eastern)
    et_day=et_time.date()

    date=et_day.strftime("%Y/%m/%d")
    path=f'data/{date}'
    cmd=f'rm -rf {path}; mkdir -p {path}'
    os.system(cmd)

    current_path = str(Path.cwd())
    m=re.search('\/([^\/]+)\-option',current_path)
    if(m!=None):
        symbol=m.group(1)
    
    cmd=f'python3 src/yahoo-option.py {symbol} {path}'
    os.system(cmd)

    cmd=f'git add {path}/*.csv'
    os.system(cmd)
