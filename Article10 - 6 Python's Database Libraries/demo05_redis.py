import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)

r.set('foo', 'bar')
print(r.get('foo'))

r.set('Company', 'Embarcadero Technologies')
print(r.get('Company'))