# increasing user limit

exec { 'increasing hardlimit for users':
  command => 'sed -i "/^holberton hard/s/5/100000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

exec { 'increasing softlimit for users':
  command => 'sed -i "/^holberton soft/s/4/100000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
