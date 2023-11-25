#!/usr/bin/pup
# This puppet installs flask version 2.1.0

package {'flask':
  ensure          => 'installed',
  install_options => ['--upgrade', 'flask==2.1.0']
  provider        => 'pip3',
}

