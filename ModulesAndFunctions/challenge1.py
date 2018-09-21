#!/usr/local/bin/python3

import time
from time import time as time_timer
from time import perf_counter as perf_timer
from time import monotonic as mono_timer
from time import process_time as proc_timer

print("'time' info: " + str(time.get_clock_info('time')))
print("'perf_counter' info: " + str(time.get_clock_info('perf_counter')))
print("'monotonic' info: " + str(time.get_clock_info('monotonic')))
print("'process_time' info: " + str(time.get_clock_info('process_time')))
print()
start_time = time_timer()
start_perf = perf_timer()
start_mono = mono_timer()
start_proc = proc_timer()
print(start_time, start_perf, start_mono, start_proc)
end_time = time_timer()
end_perf = perf_timer()
end_mono = mono_timer()
end_proc = proc_timer()
print(end_time, end_perf, end_mono, end_proc)
