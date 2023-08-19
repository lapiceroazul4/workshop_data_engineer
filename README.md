# workshop_data_engineer
# Repository ReadMe

## Dataset Exploration

Upon reviewing the CSV file, we can extract valuable information. Firstly, it becomes apparent that the file follows a well-defined format, which we can categorize as a fact table. Furthermore, it contains no null values, and the column names provide sufficient indications of their respective meanings.

## Brief Explanation of Files

### Python Files

#### [Database.py]

This file handles the database connection using the ORM, SQLAlchemy.
- We begin with the necessary imports, noting that only specific SQLAlchemy functionalities required for the project have been imported.
- The "db_config" JSON file is read, containing database access information. If you intend to use this code, ensure to provide your own credentials.
- The Workshop class is created, establishing a connection to the MySQL database. The connection is indicated by the (Base) attribute. Subsequently, we define the database columns and their characteristics.
- The constructor ("__init__") requires a session argument. This session is needed to execute subsequent class functions.
- Following are functions to perform CRUD operations (Create, Read, Update, Delete). Given project requirements, the focus is on querying the database. The following functions cater to these needs:
  - `hires_by_technology`
  - `hires_by_year`
  - `hires_by_seniority`
  - `hires_by_year_country`
- Lastly, three additional functions related to the database are defined outside the class:
  - `create_engine` → creates the database engine
  - `creating_session` → establishes a session with the database
  - `closing_session` → closes the created session

> Note: None of the functions in this file (neither within the Workshop class nor outside it) are invoked. Additionally, the data to populate the database originates from a CSV file, which is yet to be read.

---

#### [Transformation.py]

In this file, all necessary adjustments are made to the CSV for database uploading. The file consists of three functions:
- The constructor → requests the CSV's name and reads it as a pandas DataFrame.
- `normalizing` → performs two tasks: renaming the CSV's columns and creating a new column crucial for analysis.
  - The new column is "is_hired," a boolean column indicating whether candidates were hired or not.
- `Importing_db` → Defines the function responsible for sending the CSV data to the database. Note that DataFrame indices are specified to populate the "candidate_id" column in the database.

---

### [Main.py]

This file orchestrates the calls to the previously created functions, adhering to a necessary order. It also contains loops to display information returned by queries. Furthermore, query results are transformed into DataFrames and then saved into separate CSV files.

## Usage

To utilize the provided code, follow these steps:
1. Review and adjust the import statements in [Database.py], ensuring all required libraries are available.
2. Provide your own database credentials within the "db_config" JSON file.
3. Customize the functions in [Database.py] and [Transformation.py] as needed for your specific project requirements.
4. Run [Main.py] to execute the functions and generate the desired query results and CSV files.

Keep in mind that the code is designed to work with a specific dataset and may require modifications to suit your data and objectives.

For any inquiries or assistance, feel free to contact Lapiceroazul at lapiceroazul@proton.me.
