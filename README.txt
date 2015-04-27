Swiss Tournament Generator
==================================
Version: 1.1
----------------------------------

This program will run and match players in a swiss tournament setting

---------------

What's Included:
 - tournament.sql --> Holds the tables and views of the tournament database
 - tournament.py --> Holds all the functions to help the program run correctly
 - tournament_test.py --> The testing document to make sure all functions in tournament.py are working correctly.

How to Run:
 1) Assuming you have Vagrant, Git, and Oracle VM VirtualBox running on your PC
 2) Open up your Git shell to the folder you unzipped this pacakge in. 
 3) Type 'vagrant up' in the shell
 4) Type 'vagrant ssh' in the shell
 5) Next, you'll have to set up a tournament database to make the program work. You can do this by:
	   - typing 'psql' in the shell and then creating a database in the shell - 'CREATE DATABASE tournament'
	   - or, if you're having trouble with that, in the tournament.sql document, line 10 is commented out to create a database
	     (you may uncomment and run the sql file to create the database)
 6) To connect to the database, you'll want to type '\c tournament' in the shell. You'll recieve a:
 	'You are now connected to database "tournament" as user "vagrant"'
 7) Once you add the database, then you can add the tournament.sql file by typing '\i tournament.sql' in your shell
 8) To make sure it's complete, you can run 'python tournament_test.py' in your shell to see if it's working.
 9) You're finished.
