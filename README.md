
# To Do Application

The "To Do List" is a web application developed with Django, a Python-based web development framework. This application allows users to create tasks that are listed.

## Features
 
Main features of the application :

- Task creation: Users can create new task.

- Delete task: Users can delete their task create.

- Display tasks deleted : Once a user has deleted a task, this task can be display in "Section Task Deleted".

- Remove definitely each tasks or all tasks.

- Restore each tasks or all tasks.
<!-- View active polls: The application displays only active polls with a publication date prior to the current date. -->

## Screenshots
![Home Page w/ Text](/images/home.png)
![Tasks deleted Page w/ Text](/images/tasks%20deleted.png)

## Requirements
Python [version 3.11.3]
Django [version 4.2]




## Installation

1.Clone the GitHub repository:

```bash
  git clone https://github.com/yandakiY/toDoList-Django.gitv
```

2.Perform database migrations :

```bash
  python manage.py migrate

```

3.Start the development server:

```bash
  python manage.py runserver

```

4.Access the application in your browser at :
```bash
  http://localhost:8000/
```
## License

[MIT](https://choosealicense.com/licenses/mit/)


## Acknowledgements

 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)
 - [Writing your first Django application](https://docs.djangoproject.com/en/4.2/intro/tutorial01/)
