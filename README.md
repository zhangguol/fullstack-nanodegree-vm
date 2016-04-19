Project 2 - Tournament Results
=============

 This is the second project of Udacity Full stack web developer course.
 The project is writing a Python module that uses the PostgreSQL database to keep track of players and matches in a game tournament.

## Run the test case

1. Install [Vagrant](https://www.vagrantup.com) and [VitualBox](https://www.virtualbox.org)

2. Clone this repo

        git clone https://github.com/zhangguol/fullstack-nanodegree-vm

3. Enter the vagrant's directory

        $ cd fullstack-nanodegree-vm/vagrant

4. Launch vagrantVM and connect to the VM by ssh

        $ vagrant up
        $ vagrant ssh

5. Enter the project directory

        $ cd /vagrant/tournament

5. Run the script to create Databbase and tables

        $ psql
        vagrant=> \i tournament.sql

6. Exsit psql by entering `\q` or pressing `Ctrl + d`

5. Run the test case

        $ python tournament_test.py

6. Close ssh and shutdown VM

        $ exit
        $ vagrant halt
