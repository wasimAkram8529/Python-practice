class Server:
  def __init__(self, server_id, ip_address):
    self.server_id = server_id
    self.ip_address = ip_address
    self.status = "Offline"
    self.memory_usage = 0

  def start(self):
    self.status = "Online"
    print(f"Server {self.server_id} started...")

  def stop(self):
    self.status = "Offline"
    print(f"Server {self.server_id} stopped...")

  def restart(self):
    self.stop()
    self.start()
    print(f"Server {self.server_id} restarted...")

  def status_update(self, new_status):
    self.status = new_status
    print(f"Server {self.server_id} status updated to {self.status}.")

server1 = Server("SRV001", "192.168.1.100")    
server2 = Server("SRV002", "192.168.1.101")

print(server1.status)
server1.start()
print(server1.status)
server1.status_update("busy")