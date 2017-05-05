import sys
import os
import re
import subprocess 
import hashlib

#对字典取子集
def sub_dict(form_dict, sub_keys, default=None): 
    return dict([(k, form_dict.get(k.strip(), default)) for k in sub_keys.split(',')]) 

#读取cpuinfo信息 
# dmidecode -t 4 
def read_cpuinfo(): 
    cpu_stat = [] 
    with open('/proc/cpuinfo', 'r') as f: 
        data = f.read() 
        for line in data.split('\n\n'): 
            cpu_stat.append(line) 
    return cpu_stat[-2]


#读取fdisk信息 
def read_fdisk(): 
    p = subprocess.Popen('fdisk -l', stdout=subprocess.PIPE, shell=True) 
    out = p.communicate()[0] 
    info = [] 
    for i in out.split('\n\n'): 
        for x in i.splitlines(): 
            if x: 
                info.append(x) 
    return info

#读取dmidecode信息 
def read_dmidecode(): 
    p = subprocess.Popen('dmidecode -t 1', stdout=subprocess.PIPE, shell=True) 
    return p.communicate()[0] 
#读取ifconfig信息 
def read_ifconfig(): 
    p = subprocess.Popen('ifconfig', stdout=subprocess.PIPE, shell=True) 
    return p.communicate()[0] 
#返回cpu信息：CPU型号、颗数、核数 
def get_cpuinfo(data): 
    cpu_info = {} 
    for i in data.splitlines(): 
        k, v = [x.strip() for x in i.split(':')] 
        cpu_info[k] = v 
        
    cpu_info['physical id'] = str(int(cpu_info.get('physical id')) + 1) 
    return sub_dict(cpu_info, 'model name,physical id,cpu cores')


def get_uuid()
    os.system(dmidecode -t system | grep uuid)
    
    return uuid

def get_indentity(data): 
    match_serial = re.compile(r"Serial Number: .*", re.DOTALL) 
    match_uuid = re.compile(r"UUID: .*", re.DOTALL) 
    if match_serial.search(data): 
        serial = match_serial.search(data).group() 
    if match_uuid.search(data): 
        uuid = match_uuid.search(data).group() 
    if serial: 
        serial_md5 = hashlib.md5(serial).hexdigest() 
        return serial_md5 
    elif uuid: 
        uuid_md5 = hashlib.md5(uuid).hexdigest() 
        return uuid_md5 


def get_cmdb_info()
    uuid=
    dict = {}
       dict['uuid']=''  
    print dict
