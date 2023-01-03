import psutil

# Get the current network stats
bytes_sent = psutil.net_io_counters().bytes_sent
bytes_received = psutil.net_io_counters().bytes_recv

# Print the current send and receive rates
print("Bytes sent:", bytes_sent)
print("Bytes received:", bytes_received)

# Get the list of active network connections
connections = psutil.net_connections()

# Print the list of active connections
print("Active connections:")
for connection in connections:
  # Get the connection details
  laddr = connection.laddr
  raddr = connection.raddr
  status = connection.status
  pid = connection.pid

  # Print the connection details
  print("Local address: {}:{}".format(laddr[0], laddr[1]))
  print("Remote address: {}:{}".format(raddr[0], raddr[1]))
  print("Status:", status)
  print("PID:", pid)
  print()
