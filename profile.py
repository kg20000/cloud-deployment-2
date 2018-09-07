"""This is a trivial example of a gitrepo-based profile; The profile source code and other software, documentation, etc. are stored in in a publicly accessible GIT repository (say, github.com). When you instantiate this profile, the repository is cloned to all of the nodes in your experiment, to `/local/repository`. 

This particular profile is a simple example of using a single raw PC. It can be instantiated on any cluster; the node will boot the default operating system, which is typically a recent version of Ubuntu.

Instructions:
Wait for the profile instance to start, then click on the node in the topology and choose the `shell` menu item. 
"""

# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg

# Create a portal context.
pc = portal.Context()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()
 
# Add a raw PC to the request.
# Create four nodes
node-1 = request.XenVM("node1")
node-2 = request.XenVM("node2")
node-3 = request.XenVM("node3")
node-4 = request.XenVM("node4")

#Set the disk image to CENTOS for each node
node-1.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:CENTOS7-64-STD"
node-2.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:CENTOS7-64-STD"
node-3.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:CENTOS7-64-STD"
node-4.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:CENTOS7-64-STD"

#Set specific IP Address for each node
iface1 = node-1.addInterface("if1")
iface1.component_id = "eth1"
iface1.addAddress(rspec.IPv4Address("192.168.1.1", "255.255.255.0"))

iface2 = node-2.addInterface("if2")
iface2.component_id = "eth2"
iface2.addAddress(rspec.IPv4Address("192.168.1.2", "255.255.255.0"))

iface3 = node-3.addInterface("if3")
iface3.component_id = "eth3"
iface3.addAddress(rspec.IPv4Address("192.168.1.3", "255.255.255.0"))

iface4 = node-4.addInterface("if4")
iface4.component_id = "eth4"
iface4.addAddress(rspec.IPv4Address("192.168.1.4", "255.255.255.0"))

#link all nodes
link = request.LAN("lan")
link.addInterface(iface1)
link.addInterface(iface2)
link.addInterface(iface3)
link.addInterface(iface4)

#Only set an IP for the first node
node-1.routable_control_ip = "true"

# Install and execute a script that is contained in the repository.
node-1.addService(pg.Execute(shell="sh", command="/local/repository/silly.sh"))

# Print the RSpec to the enclosing page.
pc.printRequestRSpec(request)

