import redis
if __name__ == '__main__':
    rediscli = redis.StrictRedis()
    rediscli.lpush('hanjuTV_spider:start_urls','http://www.hanju.cc/hanju/')
    rediscli.lpush('goudaiTV_spider:start_urls','http://www.goudaitv.com/frim/index1.html')
    rediscli.lpush('goudaiTV_spider:start_urls', 'http://www.goudaitv.com/frim/index2.html')
    rediscli.lpush('goudaiTV_spider:start_urls', 'http://www.goudaitv.com/frim/index42.html')
    rediscli.lpush('goudaiTV_spider:start_urls', 'http://www.goudaitv.com/frim/index44.html')