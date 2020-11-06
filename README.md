Code Institute Module 11 Data-Centric Development Milestone Project

Reunion Planner

Reunion Planner is an app for users to plan a family reunion, including a list of family members and their 
pertinent information, a schedule of events and meals for the week, and a list of group expenses to be shared.

Project Aims

Reunion Planner is the third milestone project for Code Institute's data-centric development module. It is a tool 
designed specifically for my family and the annual reunion we have with my mom, stepdad, brothers and their wives, 
and our kids. Because we are spread out over three continents in different time zones, planning can be difficult. 
We have been doing the planning mostly over email (we are on Facebook but Facebook has security concerns and one 
of my brothers is starting to avoid it). It gets cumbersome to have to scroll through numerous emails if we are 
looking for a specific piece of information, such as a hotel address. The goal of the project is to incorporate data 
with the functionality to create, read, update, and delete (CRUD) the data in a user-friendly format.

Specifically, users should be able to do the following:
- view a map of the reunion location
- see where the accommodations are on the map
- access links to the destination and accommodation
- view list of family members 
- update personal information (the delete functionality was not added for people because it seems harsh but 
the administrator can delete people)
- add new family members
- view the schedule for the week
- add new schedule items or plans for dinner (the schedule is set up as a week so days of the week and times 
of day cannot be added or deleted, e.g. we only eat one dinner per day and cannot realistically fit in more than 
two activities during the day and one in the evening
- edit schedule items
- view expenses for the week such as groceries 
- see the total amount of expenses- add new expenses- delete expenses- make changes to expense entries

UX Design

The design was based on planning apps, specifically My Daily Planner, and the Task Manager Mini-Project which we 
did as part of Module 11. The color scheme is based around nature with blues and greens, as we usually visit destinations 
with natural features, such as Niagara Falls, which is the tentative destination if we (hopefully) have a reunion in 2021. 
The design is also supposed to be clean and functional to make it easy for the user to find, add, delete, or edit the 
relevant piece of information. For consistency and to make it more intuitive for users, blue is the color of buttons 
for adding things, jade green is the color for the edit buttons, and green is the color for the delete buttons. The 
page was designed primarily with Materialize, along with FontAwesome, Bootstrap, and Google Fonts. The focus on the site 
was to make it functional rather than commercial because it is for my family members so I avoided things like pop-ups and 
lots of icons. I created a wireframe in Figma but the design changed as I was working on the project. 

Future features would include a password to access the site, a page to share photographs of the trip (contingent on 
having a password for the site), and a way to link information between the pages. I specifically avoided adding email 
functionality because we already have each others' emails and the idea of the app was to cut down on the number of 
emails and to keep the information in one place.

Technologies Used:
-Gitpod and the Code Institute template
-HTML5
-CSS
-jQuery
-Javascript
-Python 3.8.3     
-Flask     
-Jinja
-Bootstrap 
-Materialize
-FontAwesome
-Google Fonts

Validators Used:
- W3C 
- HTMLW3C 
- CSS
- JSHint
- Python Extends Class

Testing:

I tested viewing all the pages as well as adding people, editing people, adding new schedule items, editing schedule 
items, adding expenses, editing expenses, and deleting expenses, and making sure the total for the expenses was correct. 
I also tested the site on a mobile phone and laptop.

Deployment: 

The project is deployed on Heroku and I used Github for version control.

Finally, a huge thank you to the tutors (I specifically got a lot of help from Tim, Kevin, and Igor and many others as 
well) and my mentor Aaron for all their help and patience with this project and the modules in spite of my glacial pace.
