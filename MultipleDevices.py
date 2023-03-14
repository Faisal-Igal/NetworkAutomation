from netmiko import ConnectHandler

#  Send Multiple Commands
#  Using For Loop

cisco_1 = {
    "device_type": "cisco_ios",
    "host": "",  #  IP or Hostname
    "username": "",
    "password": "",
    "secret": ""  # Enable password
}
connection = ConnectHandler(**cisco_1)
connection.enable() # Access Priv EXEC Mode

show_command = ['show mac address-table', 'show ip arp', 'show ip arp | include .xxxx'] # Send list of commands

#  For Loop
for command in show_command:
    print(f'\n *** Sending { command } *** \n')
    output = connection.send_command(command)
    print(output)

connection.disconnect()