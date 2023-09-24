# Change SSH configuration file

exec { 'first_update':
  command => 'echo "    IdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config',
  path	  => '/usr/bin'
}

exec { 'second_update':
  command => 'echo "    PasswordAuthentication no" >> /etc/ssh/ssh_config',
  path	  => '/usr/bin'
}
