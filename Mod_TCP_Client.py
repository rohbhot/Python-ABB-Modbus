from pymodbus.client.sync import ModbusTcpClient

client = ModbusTcpClient('192.168.0.100')         # IP address of the server / ABB PLC in this case
conn = client.connect()

if conn:
  request = client.read_holding_registers(11,10)    # Reads the value of 10 holding registers starting form the memory adress directly mapped to 40,000
  print request.registers

  client.write_register(10,200)                     # Write the value 200 to the holding register 10 or 40,010. 
