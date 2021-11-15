çimport math
import time

start_time = time.time_ns()

print (2**3)
print(math.pow(2,3))

end_time = time.process_time()

final_time = end_time-start_time

print(final_time)
