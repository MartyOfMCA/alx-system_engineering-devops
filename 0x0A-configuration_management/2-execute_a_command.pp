# Kills a process with a specific name

exec { 'pkill -f killmenow':
  path    => '/usr/bin/'
}
