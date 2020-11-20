server {
  listen 80;
  listen [::]:80;
  server_name SERVER_IP_ADDRESS;

  location / {
    proxy_pass http://unix:/home/ubuntu/mc714-avaliacao-1/app.sock;
  }
}