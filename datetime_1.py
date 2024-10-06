import os
from datetime import datetime
#2
# Sun 10 May 2015 13:54:36 -0700
# Sun 10 May 2015 13:54:36 -0000
# Sat 02 May 2015 19:54:36 +0530
# Fri 01 May 2015 13:54:36 -0000
def time_delta(t1, t2):
    #format specifiers in datetime module's strptime function
    time_format = "%a %d %b %Y %H:%M:%S %z"

    dt1 = datetime.strptime(t1, time_format)
    dt2 = datetime.strptime(t2, time_format)

    #calculating abs difference
    difference = abs((dt1-dt2).total_seconds())  #total_seconds() for only accessing seconds
    return str(int(difference))


if __name__ == '__main__':
    output_path = os.environ.get("OUTPUT_PATH", "default_path.txt")  #setting to default_path.txt in OUPUT_PATH doesnt exist
    fptr = open(output_path, 'w')

    t = int(input())

    for t_itr in range(t):
        #for each test cases, writing two timestamps
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
