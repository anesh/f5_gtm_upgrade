import bigsuds

b = bigsuds.BIGIP(hostname = '192.168.122.31',username = 'admin', password = '',)
#STATE_DISABLED
b.GlobalLB.Globals.set_auto_sync_state("STATE_DISABLED")
b.GlobalLB.Globals.set_sync_named_configuration_state("STATE_DISABLED")
b.GlobalLB.Globals.set_sync_group_name("test_anesh")
