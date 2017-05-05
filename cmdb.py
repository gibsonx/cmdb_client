import sys
import urllib2
import logging
import json

path_log_file = '/var/log/cmdb.log'
API_ADDR = '10.32.174.152:8080'

logger = logging.getLogger('cmdb_log')
file_handler = logging.FileHandler(path_log_file)
formatter = logging.Formatter('%(asctime)s:%(name)s-->%(levelname)s %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def print_dict(result):
    for k, v in result.iteritems():
        print '%s : %s' % (k, v)

def handle_result(result):
    print result

def http_post(url, data):
    headers = {
        "Content-Type": "application/json",
        "Accept-Charset": "utf-8"
    }
    request = urllib2.Request(url, json.dumps(data), headers)
    try:
        response = urllib2.urlopen(request, timeout=10)
    except urllib2.URLError, e:
        logger.error(e)
    result = json.loads(response.read())
    return handle_result(result)

'''
def send_cmdb_info(dict):
    url = "https://%s/services/IServerInfoVenusService/syncServerInfo" % API_ADDR
    data = {
            "serverInfo":{
               dict
             } 
    }
    logging.info(data)
    return http_post(url, data)
'''

def send_cmdb_info():
    url = "http://%s/services/IServerInfoVenusService/syncServerInfo" % API_ADDR
    data = {
            "serverInfo":{
                "uuid":"36000c29e2a80468665c53df3e89728d3",
                "idc":"金桥",
                "privateIp":"jinqiao",
                "osName":"centos",
                "osVersion":"jinqia",
                "kernelVersion":"v11",
                "cpu":"cpu type",
                "cpuNum":4,
                "ramSize":2048,
                "diskSize":10000,
                "type":2,
                "env":2 
             }
    }
    print url
    logger.info(data)
    return http_post(url, data)

if __name__ == '__main__':
    #get_cmdb_info()
    result = send_cmdb_info()
    print result