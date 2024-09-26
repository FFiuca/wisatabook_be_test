# To-Do Application

## Tech Stack

* **Backend:**
  + **Framework:** Django (Python framework)
  + **API Framework:** Django Rest Framework (DRF)
  + **Database:** PostgreSQL
* **Frontend:**
  + **Framework:** React
  + **UI Library:** Bootstrap
* **Testing:**
  + **Backend:** Django's built-in testing framework, with APITestCase for API testing
* **Factories:** Factory Boy for generating test data
* **Fixtures:** Django's built-in fixtures for loading initial data

## Deployment

The To-Do Application is deployed on Google Cloud Platform (GCP) using the following stack:

* **Web Server:** Gunicorn
* **Reverse Proxy:** Nginx
* **Cloud Platform:** Google Cloud Platform (GCP)

## Use Case System

The To-Do Application is a web-based system that allows users to create, manage, and track their tasks. The system provides a simple and intuitive interface for users to organize their tasks and stay productive.

### Use Cases

#### Task Creation:

* Primary Actor: User
* Goal: Create a new task with a title, description, and optional task repeats.
* Triggers: User clicks the "Create Task" button.
* Description: The system creates a new task and adds it to the user's task list.

#### Task Listing:

* Primary Actor: User
* Goal: View a list of tasks with pagination and filtering options.
* Triggers: User navigates to the task list page.
* Description: The system displays a list of tasks, with options to filter and paginate.

#### Task Detail:

* Primary Actor: User
* Goal: View detailed information about a specific task, including its title, description, and task repeats.
* Triggers: User clicks on a task in the task list.
* Description: The system displays the task detail page, showing the task's information.

#### Task Deletion:

* Primary Actor: User
* Goal: Delete a task and its associated task repeats.
* Triggers: User clicks the "Delete" button on a task.
* Description: The system deletes the task and its associated task repeats.

#### Task Status Update:

* Primary Actor: User
* Goal: Update the status of a task.
* Triggers: User clicks the "Update Status" button on a task.
* Description: The system updates the task's status.

#### Task Starred Status Update:

* Primary Actor: User
* Goal: Update the starred status of a task.
* Triggers: User clicks the "Update Starred Status" button on a task.
* Description: The system updates the task's starred status.

## Scheduler Feature

The To-Do Application features a scheduler that runs every night to create new repeated tasks. This is achieved using a cron job that hits the command `python3 manage.py repeated_task_command` until the due date end. This ensures that repeated tasks are automatically created and added to the user's task list.

## System Architecture

The To-Do Application is built using a layered architecture, with the following components:

1. **Use Cases:** Define the features and functionality required by the system.
2. **Service Layer/Repository Implementation:** Provides the concrete implementation of the repository interface, interacting with the database, and implements the use cases.
3. **Repository Interface:** Defines the interface for accessing and manipulating data.
4. **Database:** Stores task data and provides data persistence.

## Frontend Architecture

The frontend of the To-Do Application is built using React and Bootstrap. The application is designed to be responsive and user-friendly, with a simple and intuitive interface.

## Testing

The To-Do Application uses a combination of unit tests, integration tests, and API tests to ensure the system's functionality and reliability. The testing framework is built using Django's built-in testing tools, with APITestCase for API testing.
