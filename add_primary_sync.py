import bigsuds

b = bigsuds.BIGIP(hostname = '192.168.122.31',username = 'admin', password = '',)
b.GlobalLB.Globals.set_auto_sync_state("STATE_ENABLED")
b.GlobalLB.Globals.set_sync_named_configuration_state("STATE_ENABLED")
