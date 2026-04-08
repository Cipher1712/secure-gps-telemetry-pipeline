def send_to_serial(data, port="/dev/pts/1"):
    with open(port, "w") as f:
        f.write(data + "\n")