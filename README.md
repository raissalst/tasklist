<h1 align="center"><a href="#" alt="cookin">Task List API</a> ✅</h1>

<h2>Contents</h2>

- [1. About 💻](#1-about-)
- [2. Entity-Relationship Diagram ↔️](#2-entity-relationship-diagram-️)
- [3. Application's links 🔗](#3-applications-links-)
- [4. General Functionalities ⚙️](#4-general-functionalities-️)
- [5. Technologies 🧰](#5-technologies-)
  - [5.1 Requisites ☑️](#51-requisites-️)
- [6. Terms of Use 📜](#6-terms-of-use-)

<a name="about"></a>

## 1. About 💻

**_Task List_** is a basic CRUD (create, read, update and delete) application that focuses on creating and managing a task list. Each task can be created with 1 one or more categories corresponding to the task subject.

The user can create tasks and categories as well as update them and also delete. The user can retrieve the categories with their corresponding tasks.

Once the tasks are created they are automatically classificated by importance according to the "Eisenhower Principle", that utilizes the principles of importance and urgency to organize priorities and workload. The classification is based on the importance and urgency values provided when the tasks are created or updated.

This API contains 7 endpoints. For more detailed information about the API and its endpoints, please consult API Documentation in Application links section.

<a name="er-diag"></a>

## 2. Entity-Relationship Diagram ↔️

<p align="center" style="display: flex; align-items: flex-start; justify-content: center;">
  <img alt="ER-Diag" title="ER-Diag" src="./app/assets/diagrama_R0.png" width="400px">
</p>

<a name="links"></a>

## 3. Application's links 🔗

<!-- - <a name="API documentation" href="https://documenter.getpostman.com/view/19787362/UVksLDvG" target="_blank">API Documentation</a>
- <a name="API deploy in Heroku" href="https://cookin-api-capstone.herokuapp.com/" target="_blank">API Deploy in Heroku</a> -->

## 4. General Functionalities ⚙️

<!-- - [x] Once registered in Cookin' app and signed in, users can:
  - [x] update their name, gender or profile photo;
  - [x] create new recipes of their own and keep them private;
  - [x] update recipe's data, like title, ingredients, instructions, category, preparation time, difficulty, portion size and recipe image;
  - [x] consult their own private recipes, shared recipes in Cookin' community and recipes added to favorites;
  - [x] consult users of the Cookin' community info;
  - [x] choose whether to share private recipes with the Cookin' community;
  - [x] add recipes to favorites, their own recipes or shared recipes by other users from Cookin' community;
  - [x] rate shared recipes from Cookin' community;
  - [x] filter recipes by title, category, difficulty, preparation time and portion size; -->

<a name="technologies"></a>

## 5. Technologies 🧰

- <a name="python" href="https://docs.python.org/3/" target="_blank">Python</a>
- <a name="flask" href="https://flask.palletsprojects.com/en/2.0.x/" target="_blank">Flask</a>
- <a name="python.env" href="https://pypi.org/project/python-dotenv/" target="_blank">python-dotenv</a>
- <a name="flask=sql" href="https://flask-sqlalchemy.palletsprojects.com/en/2.x/" target="_blank">Flask SQLAlchemy</a>
- <a name="postgreSQL" href="https://www.postgresql.org/docs/" target="_blank">PostgreSQL</a>
- <a name="flask-m" href="https://flask-migrate.readthedocs.io/en/latest/" target="_blank">Flask Migrate</a>

<a name="requisites"></a>

### 5.1 Requisites ☑️

- Python above version 3.9.6;
- Package manager <a name="pip" href="https://pip.pypa.io/en/stable/" target="_blank">PIP</a>;
- PostgreSQL database;

<a name="terms"></a>

## 6. Terms of Use 📜

This is an Open Source project for educational and non-commercial purposes.

**License type**: <a name="gpl" href="https://www.gnu.org/licenses/gpl-3.0.en.html" target="_blank">GPL</a>
