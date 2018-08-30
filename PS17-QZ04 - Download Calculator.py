# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download 
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

#print 2 ** 10      # one kilobit, kb
#print 2 ** 10 * 8  # one kilobyte, kB

#print 2 ** 20      # one megabit, Mb
#print 2 ** 20 * 8  # one megabyte, MB

#print 2 ** 30      # one gigabit, Gb
#print 2 ** 30 * 8  # one gigabyte, GB

#print 2 ** 40      # one terabit, Tb
#print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size 
# is given in megabytes (MB).

def download_time(file_size, file_unit, bandwidth, band_unit):
    
    file_bit_size = bit_size(file_size, file_unit)
    bandwidth_bit_size = bit_size(bandwidth, band_unit)
    
    time = float(file_bit_size) / bandwidth_bit_size
    
    return convert_seconds(time)
    
def bit_size(size, unit):
    
    units  = ["kb", "kB", "Mb", "MB", "Gb", "GB", "Tb", "TB"]
    values = [1024, 8192, 1048576, 8388608, 1073741824, 8589934592, 1099511627776, 8796093022208]
    
    bit_size = size * values[units.index(unit)]
 
    return bit_size

def convert_seconds(time):
    
    seconds = time % 60
    time -= seconds
    
    minutes = int((time % 3600) / 60)
    time -= minutes * 60
    
    hours = int(time / 3600)
    
    convertion = time_formating(hours, minutes, seconds)
    
    return convertion

def time_formating(hours, minutes, seconds):
    
    # Hours
    
    formated_time = str(hours)
    
    if hours == 1:
        formated_time += " hour, "
    else:
        formated_time += " hours, "
        
    # Minutes
    
    formated_time += str(minutes)
    
    if minutes == 1:
        formated_time += " minute, "
    else:
        formated_time += " minutes, "
        
    # Seconds
    
    formated_time += str(seconds)
    
    if seconds == 1:
        formated_time += " second, "
    else:
        formated_time += " seconds, "
        
    return formated_time

print(download_time(1024,'kB', 1, 'MB'))
#>>> 0 hours, 0 minutes, 1 second

print(download_time(1024,'kB', 1, 'Mb'))
#>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print(download_time(13,'GB', 5.6, 'MB'))
#>>> 0 hours, 39 minutes, 37.1428571429 seconds

print(download_time(13,'GB', 5.6, 'Mb'))
#>>> 5 hours, 16 minutes, 57.1428571429 seconds

print(download_time(10,'MB', 2, 'kB'))
#>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print(download_time(10,'MB', 2, 'kb'))
#>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable

print(download_time(11, 'GB', 5, 'MB'))
#>>> 0 hours, 37 minutes, 32.8 seconds