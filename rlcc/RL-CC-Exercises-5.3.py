"""
(3) Produce a list of the unique octets (from
    the IP addresses) in mini-access-log.
"""

octet_list = {
    one_octet
    for one_line in open("samplefiles/mini-access-log.txt")
    for one_octet in one_line.split()[0].split(".")
}

print(octet_list)
