import bigsuds

volume = ""
b = bigsuds.BIGIP(hostname = '192.168.122.31',username = 'admin', password = '',)
listsoftware = b.System.SoftwareManagement.get_all_software_status()
for image in listsoftware:
  if image['active'] == 1:
    print "currently in use:"
    print image['installation_id']['install_volume']    
  if image['active'] == 0:
    print "not active on below"
    volume = image['installation_id']['install_volume']
    print volume

version ="16.0.1.1"  
build ="0.0.6"
product= "BIG-IP"
reboot= "true"
retry= "false"

image_list= b.System.SoftwareManagement.get_software_image_list()
image_val_list = b.System.SoftwareManagement.get_software_image(image_list)
for val in image_val_list:
  if val['version'] == version and val['build'] == build:
    print "going to install "
    if volume:
      print version,build,"on "+volume
      create_volume= "false"
      b.System.SoftwareManagement.install_software_image_v2(volume,product,version,build,create_volume,reboot,retry)
    else:
      print "creating a new volume HD1.2"
      volume = "HD1.2"
      create_volume= "true"
      b.System.SoftwareManagement.install_software_image_v2(volume,product,version,build,create_volume,reboot,retry)
