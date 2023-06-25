import uuid

# Make a UUID based on the host ID and current time
print(uuid.uuid1())

# Make a UUID using an MD5 hash of a namespace UUID and a name
print(uuid.uuid3(uuid.NAMESPACE_DNS, 'pythongui.org'))

# Make a random UUID
print(uuid.uuid4())

# Make a UUID using a SHA-1 hash of a namespace UUID and a name
print(uuid.uuid5(uuid.NAMESPACE_DNS, 'pythongui.org'))