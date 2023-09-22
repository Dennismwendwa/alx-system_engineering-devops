# this manifest uses puppet to install Flask

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
