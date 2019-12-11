# Manifest to edit SSH config file
file_line { '/etc/ssh/ssh_config':
  ensure => present,
  line   => '#   IdentityFile ~/.ssh/holberton\n#   PasswordAuthentication no\n',
}
