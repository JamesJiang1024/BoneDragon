BoneDragon
==========

One Key For Start A Openstack Project

Getting Started
========

If you'd like to begin a project use openstack framework, you can use this project.

  * Choose your project name, such as ``helloworld``
  * Get the BoneDragon ``git clone https://github.com/JimJiangX/BoneDragon.git``
  * Get your project framework `./generate.sh helloworld`
  * Waitting the magic

Unfortunately, if you are use BoneDragon in China, it may broken because of the pip download timeout.

Do it manually
   
  * cd helloworld
  * source .tox/venv/bin/active
  * pip install -r requirement.txt
  * pip install -r test-requirement.txt
  * python setup.py develop
  * testr init
  * testr run


Now you get your basic framework, do something interesting.

Sync your db : ``python helloworld/cmd/manager.py``.

Run your api: ``bin/helloworld-api``
