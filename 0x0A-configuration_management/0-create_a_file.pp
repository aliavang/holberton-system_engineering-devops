# Create file in /tmp with permission 0744, owner and group www-data
file {'/tmp/holberton':
  ensure  => present,
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
