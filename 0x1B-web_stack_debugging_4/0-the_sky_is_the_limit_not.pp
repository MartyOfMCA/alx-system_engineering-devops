# Modify nginx worker_rlimit_nofile property

exec {'sed -i s/15/1000/ /etc/default/nginx && sudo service nginx restart':
  path => '/bin'
}
