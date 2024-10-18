# CS-340 Dashboard Project

## Animal Shelter Dashboard

About the Project

Title: Animal Shelter Dashboard
Description:
This Python module streamlines CRUD operations for an Animal Shelter database in MongoDB. It serves as the backend for a web application, offering essential functionalities to manage and visualize animal data within a dashboard.

Motivation

The goal of this project is to create a user-friendly Python module that simplifies interaction between a user interface and a MongoDB database. It focuses on efficient management and visualization of animal data through a dashboard interface.

Getting Started

Prerequisites

	•	Python 3 (Download)
	•	MongoDB Community Edition (Download)
	•	Pymongo library (install via: pip install pymongo)
	•	Jupyter Notebook (included in Anaconda)

Database Configuration

Update the provided lines in the code with your MongoDB credentials (USER, PASS, HOST, PORT, DB, and COL).

Tools & Rationale

	•	Programming Language: Python, chosen for its versatility and extensive libraries for web development and data manipulation.
	•	Database: MongoDB, selected for its flexible schema and ease of integration with Python using Pymongo.
	•	Development Environment: Jupyter Notebook, offering a convenient space for testing and iterating on the code.
	•	Web Framework: Dash, used to create interactive, web-based data visualizations and control the web application’s structure.

Features

	•	Interactive Filters: Users can filter animal data by predefined categories like Water Rescue, Mountain Rescue, Disaster Rescue, or Individual Tracking, with a Reset option.
	•	Data Table: Displays animal data from the MongoDB database, allowing users to sort, filter, and select rows.
	•	Pie Chart: Visualizes the distribution of animals based on selected filter criteria.
	•	Geolocation Map: Displays the location of selected animals using their coordinates.

Usage

Code Example

	•	The AnimalShelter class interacts with the animal data in the specified MongoDB collection.
	•	Create: Inserts new animal entries.
	•	Read: Retrieves data based on provided queries.
	•	Update: Updates one or multiple entries.
	•	Delete: Removes one or multiple entries.

Tests

	•	The main function demonstrates the use of create, read, update, and delete methods.
	•	It runs only when the script is executed directly.

Additional Information

Reproducing the Project

	1.	Install MongoDB and required libraries (pymongo).
	2.	Import a CSV data file (e.g., “aac_shelter_outcomes.csv”).
	3.	Set up user authentication for secure database access.
	4.	Implement CRUD operations using the Python module.
	5.	Develop a web application using the module to visualize data with Jupyter Notebook.

Challenges Encountered

The primary challenge was setting up the project and environment on my local machine, as the school-provided environment was pre-configured. Additionally, I struggled with filtering age_upon_outcome because it includes both integers and strings, and I couldn’t convert it into the needed variable age_upon_outcome_in_weeks.
