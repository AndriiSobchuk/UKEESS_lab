TASK: Create HTTPS server: Create a Flask server that communicates over HTTPS. The server should accept requests from clients over HTTPS and respond with a JSON payload containing a greeting message and the client's IP address.

Description:

Here we have three files:
- cert.pem and key.pem which main purpose is to provide work for HTTPS protocol; we can use any other keys, but we should determine in final.py file;
- final.py file which runs flask server and communicates over HTTPS. It contains "hello" function where we are getting json reply with text message and out public IP address. After we will run this code we can check it in browser `https://<server_ip>/` or in console (e.g. `curl https://<server_ip>/` 
