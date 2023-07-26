# README

This repository contains a Python project that utilizes a virtual environment and interacts with a MySQL database using the `mysql-connector-python` library.

## Setup

To set up the project, please follow the steps below:

1. Install `virtualenv` by running the following command:
   ```
   virtualenv venv
   ```

2. Upgrade `pip` by executing the following command:
   ```
   python.exe -m pip install --upgrade pip
   ```

3. Set the execution policy to unrestricted by running the following command (for Windows users):
   ```
   Set-ExecutionPolicy Unrestricted -Force
   ```

4. Activate the virtual environment by executing the following command:
   ```
   .\venv\Scripts\activate
   ```

5. Install the `mysql-connector-python` library by running:
   ```
   pip install mysql-connector-python
   ```

6. View the installed packages by executing the following command:
   ```
   pip list
   ```

7. (Optional) If you want to freeze the current package versions into a `requirements.txt` file, use the following command:
   ```
   pip freeze > requirements.txt
   ```

## Usage

You can now use the project within the activated virtual environment. Make sure to activate the virtual environment by running the command mentioned in step 4 before executing your Python scripts or running the project.

## Additional Notes

- Remember to install and configure MySQL separately if you haven't already.
- Make sure to update the necessary connection details (host, port, username, password, database) in your Python scripts as needed to connect to your MySQL database.

For any additional information or troubleshooting, please refer to the project's documentation or contact the project maintainer.