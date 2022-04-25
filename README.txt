- In this project, I will perform calculation on a website. I will create a program to 
	manage employees, teams, projects in a company
- I will use JavaScript, Python and C++
- I will use JavaScript for front end, Java Script will work along with HTML
- I will use Django framework, so I will use Python
- I will use C++ to perform fast calculation
- Django will provide ways to communicate between front end JavaScript and Python, SWIG 
	will provide ways to communicate between C++ and Python
- I will use Docker containers


Project description
	An organization can have many staffs, many squads and work on multiple projects
	One squad can have many staff, 1 or more squad will work on a project
	A staff can work for many squad. For example, he can spend 0.5 of his time on one squad and 0.5 of his time helping another squad
	When a staff is deleted, that staff no longer appears in squads that he works for
	When a squad is deleted, all the staffs in that squad will not work for that squad anymore, but these staffs are not deleted
	When a squad is deleted, it no longer appears in the group of squad that work for a project

	My app summarize the budget spent for each squad, each project, budget for each positon (frontend developer, backend developer, 
		fullstack developer). Hence, the company can balance the budget better
	My app also summarize the squads that does not yet have a project to work on, staffs that have not used 100% of their time. Hence,
		the company can utilize human resource better
	My app also sumarize project timeline, start date and end date of projects

- Dcoker commands:
	docker build --tag python-django .
	docker run --publish 8000:8000 python-django
- go to localhost:8000/human_resource to see the main page
- go to localhost:8000/admin to manage human resource (add and remove staff, squad, project, link them together)