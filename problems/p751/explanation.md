what is CIDR?
Classless Inter-Domain Routing
192.168.100.14/24 represents the IPv4 address 192.168.100.14 and its associated routing prefix 192.168.100.0, or equivalently, its subnet mask 255.255.255.0, which has 24 leading 1-bits.

Maximize the number of trailing zeros, which will give us the largest block of IP addresses possible and optimal answer.

We can increase the number of trailing zeros by creating a CIDR block that uses all the current trailing zeros available. E.g.

IP address bits:
...0010 = Block of 2 IP addresses available
So we create a block of 2 IP addresses and add that range to the 
IP = ...0010 + 0010 = ...0100
Now a block of 4 IP addresses is available. And so forth.

In the case of the example from the problem:

...0111 = Only 1 IP address available to start. 0 trailing zeros = Block of 1 address available.
After we add 1 to the IP address:
...1000 = 3 trailing zeros = Block of 8 IP addresses available. etc.

1. convert the given IP address to an integer. We need the binary representation so that we can perform some bit operations.
2. check how many trailing zeros there are, i.e. the last bit of One. X & (-X) will give you the last bit of One, which represents the number of trailing zeros.
e.g. 
x = 11010100 
there are 2 trailing zeros, so there are 4 combinations 2^2 (00, 01, 10, 11)
-x = 00101100 (Two's complement)
x & -x = 00000100 = 4

