# Web application - CS162

A Kanban board is a simple form of task management. Every task that you add can be in one of three states: Incomplete, Complete, or Currently Being Completed.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them:
You will need to install a few dependencies. Assuming your working directory is the project folder 'todo', run:

```
pip3 install -r requirements.txt
```
Next you'll need to create the sql tables. This will create empty tables for Usernames and for Tasks. Run the following:

```
bash instructions.sh
```

Finally, you can run the program.
```
python app.py
```
Once the app is running you will likely need to enter http://127.0.0.1:5000/ into your browser to view the app.
## Notes

'authenticate.py' is unused in this app, but for further development would use a version of in order to encrypt user's passwords with sugar and ensure that each user gets to create their own database of tasks, unique to their needs.

## Authors

* **Yoel Ferdman**

## Acknowledgments

* Professor Philip Sterne
