from proxy import PROXIES, FREE_PROXIES
from agents import AGENTS
import logging as log

import random


class CustomHttpProxyFromMysqlMiddleware(object):
    proxies = FREE_PROXIES

    def process_request(self, request, spider):
        # TODO implement complex proxy providing algorithm
        if self.use_proxy(request):
            p = random.choice(self.proxies)
            try:
                request.meta['proxy'] = "http://%s" % p['ip_port']
                print(request.meta['proxy'])
            except Exception as e:
                #log.msg("Exception %s" % e, _level=log.CRITICAL)
                log.critical("Exception %s" % e)

    def use_proxy(self, request):
        """
        using direct download for depth <= 2
        using proxy with probability 0.3
        """
        #if "depth" in request.meta and int(request.meta['depth']) <= 2:
        #    return False
        #i = random.randint(1, 10)
        #return i <= 2
        return True



class CustomHttpProxyMiddleware(object):

    def process_request(self, request, spider):
        # TODO implement complex proxy providing algorithm
        if self.use_proxy(request):
            p = random.choice(PROXIES)
            try:
                request.meta['proxy'] = "http://%s" % p['ip_port']
            except Exception as e:
                #log.msg("Exception %s" % e, _level=log.CRITICAL)
                log.critical("Exception %s" % e)

    def use_proxy(self, request):
        """
        using direct download for depth <= 2
        using proxy with probability 0.3
        """
        #if "depth" in request.meta and int(request.meta['depth']) <= 2:
        #    return False
        #i = random.randint(1, 10)
        #return i <= 2
        return True


class CustomUserAgentMiddleware(object):
    def process_request(self, request, spider):
        agent = random.choice(AGENTS)
        request.headers['User-Agent'] = agent
