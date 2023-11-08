# Correct typo in a file name extension from the wp-settings.php file

exec { 'correct typo in WordPress settings file':
  command => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/' /var/www/html/wp-settings.php",
  path    => '/bin'
}
