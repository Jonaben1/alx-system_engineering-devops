# Puppet manifest for fixing Apache 500 Internal Server Error

# Install Apache2 package
package { 'apache2':
  ensure => installed,
}

# Ensure correct file permissions and ownership (replace '/path/to/your/file' with the actual file path)
file { '~/alx-system_engineering-devops/0x17-web_stack_debugging_3/0-strace_is_your_friend.pp':
  ensure  => file,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
  require => Package['apache2'],
}

# Restart Apache service
service { 'apache2':
  ensure  => running,
  require => File['~/alx-system_engineering-devops/0x17-web_stack_debugging_3/0-strace_is_your_friend.pp'],
}
