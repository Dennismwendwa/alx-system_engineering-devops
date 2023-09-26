# This class installs and configure Nginx and webserver


package { 'nginx':
  ensure => 'installed',
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World',
}

file { 'etc/nginx/sites-available/default':
  ensure => 'file',
  source => 'puppet:///modules/web_server/nginx_default_config',
}

service { 'ngixx':
  ensure    => 'running';
  enable    => true,
  require   => [Package['nginx'], File['/etc/nginx/sites-available/default']],
  subscribe => File['/etc/nginx/sites-available/default'],
}

nginx::resource::location { 'redirect_me':
  ensure   => 'present',
  location => '~ ^/redirect_me$',
  rewrite  => '^/redirect_me / permanent',
}
