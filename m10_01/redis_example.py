import redis
from redis_lru import RedisLRU
import timeit

client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client)


def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


@cache
def fibonacci_cache(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_cache(n - 1) + fibonacci_cache(n - 2)


# start_time = timeit.default_timer()
# fibonacci(38)
# print(f'Duration: {timeit.default_timer() - start_time}')
#
# start_time = timeit.default_timer()
# fibonacci_cache(138)
# print(f'Duration: {timeit.default_timer() - start_time}')

client.set('foo', 'bar')
client.set('baz', 100)

print(client.get('foo').decode())
print(int(client.get('baz').decode()))
