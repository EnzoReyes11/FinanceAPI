# Financial Tracker API

This service is part of a Personal Financial Investments Tracking suite.  
The overall aim of the project is to enable the users to:

1.  Track their current investments in Stocks and Bonds.
1.  Keep a log of transactions.
1.  See how their portfolio changed in time.
1.  Set alerts based on price.

See PROJECT.md for full details.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

*   Python 3.12+
*   uv (for dependency management)
*   A running PostgreSQL instance

### Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/enzo/FinanceAPI.git
    cd FinanceAPI
    ```

2.  **Install dependencies:**
    ```sh
    uv sync
    ```

3.  **Set up environment variables:**
    Create a `.env` file in the root directory by copying the example.
    ```sh
    cp .env.example .env
    ```
    Now, fill in the `.env` file with your configuration, such as your database credentials and a secret key for JWT.

### Running the Application

Once the dependencies are installed and your `.env` file is configured, you can run the API server:

```sh
uv run fastapi dwv src/main.py
```

The API will be available at `http://127.0.0.1:8000`.
