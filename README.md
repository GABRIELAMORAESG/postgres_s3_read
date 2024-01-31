# User Profile Data Assessment

This assessment involves working with user profile data stored in a PostgreSQL database and a sample CSV dump in an Amazon S3 bucket. Follow the instructions below to complete the assessment.

## Requirements

- Python 3.x
- PostgreSQL
- Necessary Python libraries: `psycopg2`, `boto3`, `pandas`

## Setup Instructions

1. **Clone the Repository**: 
    ```bash
    git clone <repository_url>
    ```

2. **Install Dependencies**: 
    ```bash
    pip install psycopg2 boto3 pandas
    ```

3. **Create Configuration File**: 
    Create a file named `database.ini` inside the `postgres` directory with the following content:

    ```
    [postgresql]
    host = <your-host>
    port = <your-port>
    database = <your-database>
    user = <your-user-name>
    password = <your-password>
    ```

4. **Run PostgreSQL Script**: 
    ```bash
    python postgres/postgres.py
    ```

5. **Run S3 Script**: 
    ```bash
    python s3/s3.py
    ```

## Notes

- The PostgreSQL script (`postgres/postgres.py`) retrieves user profile data from the PostgreSQL database.
- The S3 script (`s3/s3.py`) fetches user account creation data from the provided CSV dump stored in the S3 bucket.
