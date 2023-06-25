import ipaddress

print(ipaddress.ip_address('192.168.0.1'))
print(ipaddress.ip_address('2001:db8::'))
print(ipaddress.ip_network('192.168.0.0/28'))

print(ipaddress.IPv4Address('192.168.0.1'))
print(ipaddress.IPv4Address(3232235521))
print(ipaddress.IPv4Address(b'\xC0\xA8\x00\x01'))

print(ipaddress.IPv6Address('2001:db8::1000'))
print(ipaddress.IPv6Address('ff02::5678'))