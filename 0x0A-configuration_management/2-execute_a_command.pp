# a manifest that kills a process names killmenow

exec {'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
