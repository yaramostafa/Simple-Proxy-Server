# Simple-Proxy-Server
A simple proxy server that understands simple GET-requests, it handles all kinds of objects - not just HTML pages, but 
also images. 
it has Error Handling feature when it a page is not found it send 404 error.

It caches websites When the proxy gets a request, it checks if the requested object is cached, and if yes, it returns the object from the cache, 
without contacting the server. If the object is not cached, the proxy retrieves the object from the server, 
returns it to the client and caches a copy for future requests

Supports URL Filter where a list of websites are blocked the proxyserver prevents user from accessing them and returns an error page 
with a message that says “This URL is blocked”

## To run the proxy server
open cmd and direct it to where the file is for example if its on desktop write "cd desktop".
then write

```
python proxyserver.py (your ip address)
```
Note this proxy works python 2

example 
![image](https://user-images.githubusercontent.com/89746218/211193648-a2a805bf-a03b-4ab2-9539-4ba5e54e290c.png)

reading from cache
![image](https://user-images.githubusercontent.com/89746218/211193668-564d469f-e963-4b61-b8da-99cfce3b8c40.png)

cache files

![image](https://user-images.githubusercontent.com/89746218/211285340-c4dd4d69-9f30-4fdc-ad24-adebb8aee849.png)

