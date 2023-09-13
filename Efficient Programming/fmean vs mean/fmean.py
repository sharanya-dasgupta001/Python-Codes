import time as tm
import statistics as st
start = tm.time()
ls=[20]*50000
avg=st.fmean(ls)
end = tm.time()
print(end-start)
'''
$ python3 time_mean.py
0.015282869338989258
$ python3 time_fmean.py
0.0004906654357910156
'''
