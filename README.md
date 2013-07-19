BoneDragon
==========

Openstack Project Template

Architecture
========

![Alt text](/doc/pic/BoneDragon.png "Architecture")

Getting Started
========

If you'd like to begin a project use openstack framework, you can use this project.

  * Choose your project name, such as ``helloworld``
  * Get the BoneDragon ``git clone https://github.com/JimJiangX/BoneDragon.git``
  * Get your project framework `./generate.sh helloworld`
  * Waiting the magic, then `cd ../helloworld`
  * Step into venv `source .tox/venv/bin/active`
  * pip install -r requirement.txt
  * pip install -r test-requirement.txt
  * python setup.py develop
  * Init tests `testr init`
  * `testr run`

Now you get your basic framework, do something interesting.

copy your etc file `mkdir /etc/helloworld`, `cp etc/helloworld/helloworld.conf /etc/helloworld/helloworld.conf`

Sync your db  ``python helloworld/cmd/manager.py``.

Run your api: ``bin/helloworld-api``

Run `curl http://localhost:8080/v1/exs` will get api demo.
