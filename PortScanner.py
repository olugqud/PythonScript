# Define the target host and the range of ports to be scanned
target_host = input("Enter target host IP: ")
start_port = int(input("Enter start port number: "))
end_port = int(input("Enter end port number: "))

# Loop through each port and attempt to connect to the target host
for port in range(start_port, end_port+1):
    # Create a new socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Set a timeout to prevent hanging on failed connections
    client.settimeout(0.1)
    # Attempt to connect to the target host on the current port
    try:
        client.connect((target_host, port))
        print(f"Port {port} is open!")
    except:
        pass
    # Close the socket connection
    client.close()