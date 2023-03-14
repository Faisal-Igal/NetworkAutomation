from netmiko import ConnectHandler #  Import Netmiko

#  Establish SSH connection
net_connect = ConnectHandler(
    device_type="cisco_ios",
    host="",  # IP or Hostname
    username="",
    password="",
    secret="",  # Enable Mode
)

#  Send command to device
command = net_connect.send_command(
    "show ip arp | include .xxxx"
)
print(command)
