# wrenchpot


## Description

This is a Python-based fake SSH server designed to capture login attempts from clients. It uses the `paramiko` library to create a fully functional SSH interface that **never allows successful login**, logging all usernames and passwords for analysis or threat monitoring purposes.

It prints a retro-style banner and startup information, then listens for incoming SSH connections on port **22**.

---

##  WARNING

**For educational or research purposes only.**  
Running a fake SSH server on a public network may be illegal or unethical without explicit authorization. Always comply with your local laws and organization's policies.

---

## Features

-  Stylized banner with timestamp
-  Fake SSH interface using `paramiko`
-  Logs all username/password login attempts
-  Multithreaded to handle multiple connections
-  Automatically generates a 2048-bit RSA key

---

## Requirements

- Python 3.x
- `paramiko`
- `cryptography`
- `colorama`

### Install dependencies

```bash
pip install paramiko cryptography colorama

Usage
 Run the server

sudo python3 wrench.py

     Port 22 requires elevated privileges. Use sudo.

The server will start listening on all interfaces (0.0.0.0) on port 22. Each incoming SSH connection will be handled in a separate thread, and all credentials attempted will be printed to the console.
Sample Output

connection: 192.168.1.10:55322
admin:123456
user:password

Code Structure

    SSH_server class: Inherits from paramiko.ServerInterface to reject all authentication attempts.

    handle_connection(): Sets up and handles a single client connection.

    main(): Sets up the socket server and starts listening for connections.

Legal Notice

This software is provided "as is" without warranty of any kind. The authors are not responsible for any damage or legal issues arising from misuse.

Use responsibly and ethically.
