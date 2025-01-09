# ResumeProcessor

## **Project Setup and API Testing Instructions**

This project is a Django-based application that processes resumes (in PDF or DOCX format) and extracts key information such as first name, email, and mobile number. Below are the steps to set up the project locally and test the API endpoint.

---

### **Prerequisites**

Ensure you have the following installed:

- **Python** 3.6+ (for running the backend)
- **PostgreSQL** (for the database)
- **Postman** (for testing the API)

### **Steps to Set Up the Project Locally**

1. **Clone the repository** Clone the repository to your local machine:
   ```bash
   git clone https://github.com/apuravmahajan/ResumeProcessor.git
   
2. **Navigate to the Project Directory** Once the repository is cloned, navigate to the project directory:
   ```bash
   cd ResumeProcessor
   
3. **Create a Virtual Environment** Create a virtual environment to isolate the dependencies:
   ```bash
   python3 -m venv venv
   
4. **Activate the Virtual Environment** Activate the virtual environment:
   ```bash
   venv/Scripts/activate
   
5. **Install Project Dependencies** Install all required packages by running:
   ```bash
   pip install -r requirements.txt
   
6. **Set Up the Database** Follow the steps in the **Database Setup** section below to set up the PostgreSQL database and link it to your project.
    
7. **Apply Migrations** After setting up the database, apply the migrations:
   ```bash
   python manage.py migrate

8. **Run the Development Server** Start the Django development server:
   ```bash
   python manage.py runserver

### **Test the API Endpoint**

1. **Install Postman** Download and install Postman.
    
2. **Enter the API Endpoint URL** Type in the URL to the API endpoint:
    ```http
    http://127.0.0.1:8000/api/extract_resume
   
3. **Select the HTTP method** Select POST from the dropdown list to the left of the URL input.
    
4. **Set Up the Request Body in Postman**
- Go to the **Body** tab in Postman
- Select **form-data**
- Enter resume as the key
- Select File from the dropdown to the right of the key field
- Upload a compatible resume file (PDF or DOCX)

5. **Send the Request** Click Send, and wait for the response. If no error occurs, a JSON response similar to the one below will be returned:
    ```json
    {
     "first_name": "John",
     "email": "john.doe@example.com",
     "mobile_number": "123-456-7890"
     }

### **Steps to set up the database**

1. **Install PostreSQL** on your computer

2. **Log in to PostgreSQL as a Superuser** Once PostgreSQL is installed, log into the PostgreSQL shell as a superuser:
   ```bash
   psql -U postgres

3. **Create the Database and User** Run the following SQL commands inside the psql shell to create the database and user:
   ```sql
   CREATE DATABASE resumeprocessor;
   CREATE USER myuser WITH PASSWORD 'password';
   GRANT ALL PRIVILEGES ON DATABASE resumeprocessor TO myuser;
   \c resumeprocessor;
   GRANT ALL PRIVILEGES ON SCHEMA public TO myuser;
   GRANT ALL ON ALL TABLES IN SCHEMA public TO myuser;
   GRANT ALL ON ALL SEQUENCES IN SCHEMA public TO myuser;
   ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO myuser;
   ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON SEQUENCES TO myuser;
   \q

### **Linking Project with Database**

1. Open the settings.py file in the ResumeProcessor project folder.
   
2. Update the DATABASES dictionary with your database credentials:
   
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'resumeprocessor',          
           'USER': 'myuser',      
           'PASSWORD': 'password',     
           'HOST': 'localhost',          
           'PORT': '5432',              
       }
   }

You can update it according to the details of your database.

**Note** This setup is for Windows. Please make changes accordingly.
