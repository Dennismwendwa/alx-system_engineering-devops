# This script changes nginx limit

exec { 'Nginx limit':
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  path    => 'usr/local/bin/:/bin/',
}

exec { 'reload nginx':
  command => '/etc/init.d/nginx restart',
  path    => '/etc/init.d/',
}
