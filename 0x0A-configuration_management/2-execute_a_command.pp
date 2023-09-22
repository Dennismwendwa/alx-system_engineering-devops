# this manifest uses pkill to kill the killmenow process


exec {'kills process':
  command  => 'pkill killmenow',
  path     => ['/bin', '/usr/bin'],
  provider => 'shell',
}
