import bigsuds
import time

b = bigsuds.BIGIP(hostname = '192.168.122.31',username = 'admin', password = '',)
b.System.Failover.set_offline_release()
time.sleep(5)
print b.System.Failover.get_failover_state()
