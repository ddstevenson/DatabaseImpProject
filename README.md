# DatabaseImpProject
Class Project for CS587 Database Implementations

# Project Summary & Goals:
In this project, you will design and implement and run a database benchmark in the style of the Wisconsin Benchmark and using Wisconsin Benchmark data. You will begin by generating benchmark data and loading it into your selected system to gain an understanding of the data and a platform to work with. You will next research the system or systems you choose to use and design benchmark queries. Finally, you will implement your benchmark and run the performance experiments.

# Part 1

## Brief description of your data generation process including what program you used to generate the data.
In order to generate the data, we first downloaded and analyzied a set of python scripts posted on a public repo on github, (very likely by a previous student in this course.) Once we determined they met our requirements, they were utilized to generate the appropriate datasets in csv files. These csv files were then uploaded to our VM via sSSH and \copied into the correct tables within our VM's database. As of this writing, the tables are fully populated and ready for testing.

## Which system you will be working with and why you chose it
For this project we are using linux on an x86 processor running PostgreSQL. We chose this database because both project partners have experience working with it, because it's cheaply availiable, and because it's very well supported within this classroom enviornment. Although we both have experience with other, commercial, DBMSs that are more popular, it seemed prudent to stick with what's been demonstrated and supported for this class.

## Demonstrate you have loaded data into that system
https://github.com/ddstevenson/DatabaseImpProject/blob/main/onektup.png
https://github.com/ddstevenson/DatabaseImpProject/blob/main/tenktup1.png
https://github.com/ddstevenson/DatabaseImpProject/blob/main/tenktup2.png
https://github.com/ddstevenson/DatabaseImpProject/blob/main/proof%20of%20table%20length.png

## Include lessons learned or issues encountered
The primary issue we've encountered so far is our inability to connect to the database from pgAdmin -- a small issue to be sure, but it would probably benefit us in the course of the project if we could troubleshoot this issue. Otherwise, the project has proceeded smoothly thus far.

## Extra credit for doing the project as a container or VM
- [x] We are running this project on a google cloud VM
