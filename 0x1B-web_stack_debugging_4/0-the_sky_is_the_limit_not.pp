# Puppet manifest to optimize Nginx configuration for handling ApacheBench load

# Define class for Nginx configuration
class nginx_config {

    # Ensure Nginx package is installed
    package { 'nginx':
        ensure => installed,
    }

    # Configure Nginx settings
    file { '/etc/nginx/nginx.conf':
        ensure  => file,
        owner   => 'root',
        group   => 'root',
        mode    => '0644',
        content => template('nginx/nginx.conf.erb'), # Use ERB template for configuration
        require => Package['nginx'],
        notify  => Service['nginx'],
    }

    # Ensure Nginx service is running
    service { 'nginx':
        ensure  => running,
        enable  => true,
        require => Package['nginx'],
    }
}

# Include Nginx configuration class
include nginx_config
