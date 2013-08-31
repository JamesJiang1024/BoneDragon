BoneDragon
==========

Openstack Project Template

wiki: http://wiki.ustack.com/doku.php?id=bonedragon

Architecture
========

![Alt text](/doc/pic/BoneDragon.png "Architecture")

Getting Started
========

If you'd like to begin a project use openstack framework, you can use this project.

  * Make sure you have installed pip ``sudo pip -V``
  * If your are using Mac ``brew install gnu-sed coreutils``
  * Get your project framework `./generate.sh helloworld`, your project maybe named `helloworld`.


Your framework has been done, begin to have a test of your project.

  * Waiting the magic, then `cd ../helloworld`
  * Run `tox -evenv -- echo 'done'`
    Note: it will be very slow,  if you can see "venv installdeps: -r/home/simon/helloworld/requirements.txt, -r/home/simon/helloworld/test-requirements.txt"
        please cut off.
  * Step into venv `source .tox/venv/bin/active`
  * pip install -r requirements.txt
  * pip install http://tarballs.openstack.org/oslo.config/oslo.config-1.2.0a2.tar.gz#egg=oslo.config-1.2.0a2
  * pip install -r test-requirements.txt
  * python setup.py develop
  * Init tests `testr init`
  * `testr run`

After the test, do something interesting.

copy your etc file `mkdir /etc/helloworld`, `cp etc/helloworld/helloworld.conf /etc/helloworld/helloworld.conf`

Sync your db  ``python helloworld/cmd/manage.py``.

Run your api: ``bin/helloworld-api``

Run `curl http://localhost:8080/v1/exs` will get api demo.


Deploy Under Apache2 In Production Env
========

On Ubuntu
--------

* sudo apt-get install apache2 libapache2-mod-wsgi
* modify /etc/apache2/sites-enabled/000-default like:


<VirtualHost *:80>

    ServerName www.example.com
    ServerAlias example.com
    ServerAdmin webmaster@example.com

    DocumentRoot /usr/local/www/documents

    <Directory /home/jiangwt100/WorkingProject/vitrine>
    Order allow,deny
    Allow from all
    </Directory>

    WSGIScriptAlias /app /home/jiangwt100/WorkingProject/vitrine/vitrine/api/app.wsgi

    <Directory /home/jiangwt100/WorkingProject/vitrine>
    Order allow,deny
    Allow from all
    </Directory>

</VirtualHost>

** directory is the install dir in you system

service apache2 restart

if your app did not work, `tail -f /var/log/apache2/error.log`

On CentOS
---------
