# Simple-Proxy-Server
A simple proxy server that understands simple GET-requests, it handles all kinds of objects - not just HTML pages, but 
also images. 
it has Error Handling feature when it a page is not found it send 404 error.

it caches websites When the proxy gets a request, it checks if the requested object is cached, and if yes, it returns the object from the cache, 
without contacting the server. If the object is not cached, the proxy retrieves the object from the server, 
returns it to the client and caches a copy for future requests

supports URL Filter where a list of websites are blocked the proxyserver prevents user from accessing them and returns an error page 
with a message that says “This URL is blocked”

### To run the proxy server
open cmd and direct it to where the file is for example if its on desktop write "cd desktop".
then write

```
python proxyserver.py (your ip address)
```
Note this proxy works python 2
