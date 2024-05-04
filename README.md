# Django API Server for Bank Branches


This Django API server provides endpoints to retrieve bank and branch information, with support for adding new branches. It uses PostgreSQL as the database backend.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Abhi19990628/assignment.git
   cd assignment

2. **Install dependencies**:
   ```bash
   pip install django
   pip install djangorestframework
   pip install psycopg2

3. **Database Configuration**:
    * Make sure you have PostgreSQL installed and running.
    * Create a new PostgreSQL database for the project.
4. **Set Database Credentials**:
    * Open settings.py in the my_project directory.
    * Update the DATABASES dictionary with your PostgreSQL database credentials.
  
5. **Apply Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate

6. **Run the Server**:
   ```bash
   python manage.py runserver

## Endpoints

 * /api/banks/: GET endpoint to retrieve a list of all banks.
 * /api/branches/: GET endpoint to retrieve a list of all branches.
 * /api/branches/<ifsc>/: GET endpoint to retrieve details of a specific branch identified by its IFSC code.
 * path('branches/<str:ifsc>/', BranchDetail.as_view(), name='branch-detail'),

## API Usage

 * To retrieve a list of all banks, send a GET request to /api/banks/.
 * To retrieve a list of all branches, send a GET request to /api/branches/.
 * To retrieve details of a specific branch, send a GET request to /api/branches/<ifsc>/ where <ifsc> is the IFSC code of the branch.



 


   
   
