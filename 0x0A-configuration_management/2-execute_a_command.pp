# using Puppet, create manifest that kills a process named a killmenow

exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell'
}
