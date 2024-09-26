# <font color="blue">To-Do Application</font>

## <font color="green">Tech Stack</font>

* **Backend:**
  + **Framework:** <font color="blue">Django (Python framework)</font>
  + **API Framework:** <font color="blue">Django Rest Framework (DRF)</font>
  + **Database:** <font color="blue">PostgreSQL</font>
* **Frontend:**
  + **Framework:** <font color="blue">React</font>
  + **UI Library:** <font color="blue">Bootstrap</font>
* **Testing:**
  + **Backend:** <font color="blue">Django's built-in testing framework, with APITestCase for API testing</font>
* **Factories:** <font color="blue">Factory Boy for generating test data</font>
* **Fixtures:** <font color="blue">Django's built-in fixtures for loading initial data</font>

## <font color="green">Deployment</font>

The To-Do Application is deployed on <font color="blue">Google Cloud Platform (GCP)</font> using the following stack:

* **Web Server:** <font color="blue">Gunicorn</font>
* **Reverse Proxy:** <font color="blue">Nginx</font>
* **Cloud Platform:** <font color="blue">Google Cloud Platform (GCP)</font>

## <font color="green">Use Case System</font>

The To-Do Application is a web-based system that allows users to create, manage, and track their tasks. The system provides a simple and intuitive interface for users to organize their tasks and stay productive.

### <font color="green">Use Cases</font>

#### <font color="blue">Task Creation:</font>

* Primary Actor: User
* Goal: Create a new task with a title, description, and optional task repeats.
* Triggers: User clicks the "Create Task" button.
* Description: The system creates a new task and adds it to the user's task list.

#### <font color="blue">Task Listing:</font>

* Primary Actor: User
* Goal: View a list of tasks with pagination and filtering options.
* Triggers: User navigates to the task list page.
* Description: The system displays a list of tasks, with options to filter and paginate.

#### <font color="blue">Task Detail:</font>

* Primary Actor: User
* Goal: View detailed information about a specific task, including its title, description, and task repeats.
* Triggers: User clicks on a task in the task list.
* Description: The system displays the task detail page, showing the task's information.

#### <font color="blue">Task Deletion:</font>

* Primary Actor: User
* Goal: Delete a task and its associated task repeats.
* Triggers: User clicks the "Delete" button on a task.
* Description: The system deletes the task and its associated task repeats.

#### <font color="blue">Task Status Update:</font>

* Primary Actor: User
* Goal: Update the status of a task.
* Triggers: User clicks the "Update Status" button on a task.
* Description: The system updates the task's status.

#### <font color="blue">Task Starred Status Update:</font>

* Primary Actor: User
* Goal: Update the starred status of a task.
* Triggers: User clicks the "Update Starred Status" button on a task.
* Description: The system updates the task's starred status.

## <font color="green">Scheduler Feature</font>

The To-Do Application features a scheduler that runs <font color="red">every night</font> to create new repeated tasks. This is achieved using a cron job that hits the command `python3 manage.py repeated_task_command` until the due date end. This ensures that repeated tasks are automatically created and added to the user's task list.

## <font color="green">System Architecture</font>

The To-Do Application is built using a layered architecture, with the following components:

1. **Use Cases:** Define the features and functionality required by the system.
2. **Service Layer/Repository Implementation:** Provides the concrete implementation of the repository interface, interacting with the database, and implements the use cases.
3. **Repository Interface:** Defines the interface for accessing and manipulating data.
4. **Database:** Stores task data and provides data persistence.

## <font color="green">Frontend Architecture</font>

The frontend of the To-Do Application is built using <font color="blue">React</font> and <font color="blue">Bootstrap</font>. The application is designed to be responsive and user-friendly, with a simple and intuitive interface.

## <font color="green">Testing</font>

The To-Do Application uses a combination
