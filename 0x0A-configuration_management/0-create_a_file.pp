file {'school':
ensure  =>  file,
path    =>  '/tmp/school',
owner   =>  'www-data',
group   =>  'wwww-data',
mode    =>  '0744',
content =>   'I love Puppet'
}
