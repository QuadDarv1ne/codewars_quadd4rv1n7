'''
[ Count IP Addresses ]

Implement a function that receives two IPv4 addresses, and returns the number of addresses between them (including the first one, excluding the last one).

All inputs will be valid IPv4 addresses in the form of strings. The last address will always be greater than the first one.

Examples:
* With input "10.0.0.0", "10.0.0.50"  => return   50 
* With input "10.0.0.0", "10.0.1.0"   => return  256 
* With input "20.0.0.10", "20.0.1.0"  => return  246
'''


def ip_to_int(ip):
    # Convert an IP address to an integer
    octets = ip.split('.')
    return sum(int(octet) << (8 * (3 - i)) for i, octet in enumerate(octets))

def ips_between(start, end):
    # Convert the IPs to integers
    start_int = ip_to_int(start)
    end_int = ip_to_int(end)
    
    # Return the number of IP addresses between the start and end (exclusive of the end)
    return end_int - start_int


# TODO: Заметки
## Автор: Дуплей Максим Игоревич / Dupley Maxim Igorevich
## Дата: 30.11.2024
