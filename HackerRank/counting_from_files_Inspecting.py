"""
Given a file that contains http log requests
a line consists of hostname,
  -,
  -,(hyphens are missing values)
  timestamp,
  the request e.g. GET /images/dog/pic.jpg
  HTTP response code
  number of bytes sent in response

  . create a function to create a unique list of hostnames with number
  of requests.
"""
filename = "host_access_log_00.txt"

# counts
counts = {}
with open(filename, 'r') as f:
    for line in f:
        host = line.split()[0] # first part is hostname
        # start count from 0 is first time seen
        counts[host] = counts.get(host, 0) + 1

# output file
output_filename = "records_" + filename
with open(output_filename, "w") as out:
    for host, count in counts.items():
        out.write(f"{host} {count}\n")