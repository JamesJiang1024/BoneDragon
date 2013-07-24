BoneDragon
==========

Openstack Project Template

Architecture
========

![Alt text](/doc/pic/BoneDragon.png "Architecture")

Getting Started
========

If you'd like to begin a project use openstack framework, you can use this project.

  * Make sure you have installed pip ``sudo pip -V``
  * If your are using Mac ``brew install gnu-sed coreutils``
  * Get the BoneDragon ``git clone https://github.com/JimJiangX/BoneDragon.git``
  * ``cd BoneDragon``
  * Get your project framework `./generate.sh helloworld`, your project maybe named `helloworld`.


Your framework has been done, begin to have a test of your project.

  * Waiting the magic, then `cd ../helloworld`
  * Run `tox -evenv -- echo 'done'`
  * Step into venv `source .tox/venv/bin/active`
  * pip install -r requirements.txt
  * pip install -r test-requirements.txt
  * python setup.py develop
  * Init tests `testr init`
  * `testr run`

After the test, do something interesting.

copy your etc file `mkdir /etc/helloworld`, `cp etc/helloworld/helloworld.conf /etc/helloworld/helloworld.conf`

Sync your db  ``python helloworld/cmd/manage.py``.

Run your api: ``bin/helloworld-api``

Run `curl http://localhost:8080/v1/exs` will get api demo.
