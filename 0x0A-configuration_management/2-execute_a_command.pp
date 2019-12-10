# Manifest that kills process named 'killmenow'
exec { 'killmenow':
  path    => 'usr/bin/pkill',
  command => 'pkill killmenow',
}
