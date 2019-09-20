import memcache

mc = memcache.Client(["129.28.49.20:11211"],debug=True)

def set(key,value,timeout=300):
    return mc.set(key=key,val=value,time=timeout)


def get(key):
    return mc.get(key)

def delete(key):
    return mc.delete(key)

