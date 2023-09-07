class nginx_config {
  # Install Nginx
  package { 'nginx':
    ensure => 'installed',
  }

  # Create directories
  file { ['/data/web_static/releases/test/', '/data/web_static/shared/']:
    ensure => 'directory',
    owner  => 'ubuntu',
    group  => 'ubuntu',
    mode   => '0755',
  }

  # Create index.html file
  file { '/data/web_static/releases/test/index.html':
    ensure  => 'file',
    content => 'Holberton School',
    owner   => 'ubuntu',
    group   => 'ubuntu',
    mode    => '0644',
    require => File['/data/web_static/releases/test/'],
  }

  # Create a symbolic link
  file { '/data/web_static/current':
    ensure => 'link',
    target => '/data/web_static/releases/test/',
  }

  # Define an Nginx location block
  file { '/etc/nginx/sites-available/default':
    ensure  => 'file',
    content => template('nginx_config/default.erb'),
    require => Package['nginx'],
    notify  => Service['nginx'],
  }

  # Start and enable Nginx service
  service { 'nginx':
    ensure    => 'running',
    enable    => true,
    require   => Package['nginx'],
    subscribe => File['/etc/nginx/sites-available/default'],
  }
}

server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /data/web_static/current;

    location /hbnb_static/ {
        alias /data/web_static/current/;
    }

    # ... other server configurations ...
}
