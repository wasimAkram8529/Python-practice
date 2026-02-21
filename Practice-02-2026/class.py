class Server:
  def __init__(self, serverID, ip_address):
    self.serverID = serverID
    self.ip_address = ip_address
    self.status = "offline"
    self.memory_usage = 0

  def start(self):
    self.status = "Online"
    print(f"Server ${self.serverID} is started.")

  def stop(self):
    self.status = "Offline"
    print(f"Server ${self.serverID} stopped")

  def restarted(self):
    self.stop()
    self.start()
    print(f"Server ${self.serverID} restarted")

  def update_status(self, new_status):
    self.status = new_status
    print(f"Server ${self.serverID} status updated to ${new_status}")


server1 = Server("SRV001", "192.168.1.100")
server1 = Server("SRV001", "192.168.1.101")

print(server1.status)
server1.start()
server1.stop()
server1.restarted()
server1.update_status("Offline")