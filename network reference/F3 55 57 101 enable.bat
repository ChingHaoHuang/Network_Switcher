REM use route print to find interface number of intel NIC
REM route print | findstr /I intel
REM route add -p 0.0.0.0 mask 0.0.0.0 192.168.1.1 if 2 metric 10
route add 10.7.0.0 mask 255.255.0.0 172.23.51.254 if 2 metric 20
route add 10.20.0.0 mask 255.255.0.0 172.23.51.254 if 2 metric 20


route add 172.16.0.0 mask 255.255.0.0 172.23.51.254 if 2 metric 20
route add 172.19.0.0 mask 255.255.0.0 172.23.51.254 if 2 metric 20
route add 172.20.0.0 mask 255.255.0.0 172.23.51.254 if 2 metric 20
route add 172.21.0.0 mask 255.255.0.0 172.23.51.254 if 2 metric 20
route add 172.22.0.0 mask 255.255.0.0 172.23.51.254 if 2 metric 20
route add 172.23.0.0 mask 255.255.0.0 172.23.51.254 if 2 metric 20
route add 172.24.0.0 mask 255.255.0.0 172.23.51.254 if 2 metric 20
route add 172.25.0.0 mask 255.255.0.0 172.23.51.254 if 2 metric 20
route add 172.28.0.0 mask 255.255.0.0 172.23.51.254 if 2 metric 20

pause