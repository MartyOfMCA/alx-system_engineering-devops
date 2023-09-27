# Install nginx
package { 'nginx':
  ensure         => 'installed',
  install_option => ['-y']
}

# Modify contents of index page
file { '/var/www/html/index.nginx-debian.html':
  ensure  => 'file',
  content => 'Hello World!',
  require => Package['nginx']
}

# Modify nginx redirection
file { '/etc/nginx/sites-enabled/default':
  ensure  => present,
  content => '
server {
	listen 80 default_server;
	listen [::]:80 default_server;

	root /var/www/html;
	index index.html index.htm index.nginx-debian.html;
	server_name _;

	location / {
		try_files $uri $uri/ =404;
	}

	location /redirect_me {
		return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
	}
}'
}

# Restart nginx service
exec { 'sudo service nginx restart':
  path => 'usr/bin/env'
}
