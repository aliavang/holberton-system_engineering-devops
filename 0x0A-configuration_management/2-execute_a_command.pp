# Manifest that kills process named 'killmenow'
exec { 'killmenow':
  path    => '/usr/bin/',
  command => 'pkill killmenow',
}
