#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import docker
client = docker.from_env()

#print (client.containers.list())

for cont in client.containers.list():
    print (cont)
    
container = client.containers.get('bc966f571c')
print (container)
    
"""  
#client.containers.list()
print(client.containers.list('NAMES'))


for cont in client.containers():
    print(cont)
    

#client.containers.run("ubuntu:latest", "echo hello world")

"""