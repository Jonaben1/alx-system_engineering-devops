# Puppet manifest to configure OS settings for user "holberton"

# Ensure the holberton user exists
user { 'holberton':
  ensure => present,
}

# Allow the holberton user to log in
file { '/etc/ssh/sshd_config':
  ensure  => file,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => template('ssh/sshd_config.erb'), # You need to create an ERB template for sshd_config
  notify  => Service['ssh'],
}

# Ensure SSH service is running and enabled
service { 'ssh':
  ensure  => running,
  enable  => true,
  require => File['/etc/ssh/sshd_config'],
}
