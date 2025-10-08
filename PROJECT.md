# Financial Tracker API

This service is part of a Personal Financial Investments Tracking suite.  
The overall aim of the project is to enable the users to:

1.  Track their current investments in Stocks and Bonds.
1.  Keep a log of transactions.
1.  See how their portfolio changed in time.
1.  Set alerts based on price.

## Backlog
### Tier 1: Must-Have Features (Complete the Core App)
#### Implement Authentication:
- Define User model in users/models.py.
- Implement password hashing logic in auth/security.py.
- Build the user creation logic in users/service.py and the endpoint in users/router.py.
- Build the login logic in auth/service.py to return a JWT, and the endpoint in auth/router.py.
- Create a FastAPI dependency in auth/security.py to protect endpoints.
#### Build the Portfolio & Transaction Endpoints:
- Define Portfolio and Transaction models in portfolios/models.py, linking them to users and assets.
- Implement the business logic for portfolio/transaction CRUD in portfolios/service.py.
- Implement the API endpoints in portfolios/router.py, protecting them with the auth dependency.
#### Integrate the Data Ingestion workflow:
- Update the current workflow to first query the PostgreSQL Assets table (using SQLAlchemy) to get the list of all assets to track.
- Update the asset prices table in BigQuery.

### Tier 2: High-Value Analytics Features 
#### Portfolio Holdings Endpoint:
- In portfolios/service.py, create a function to aggregate transactions from PostgreSQL for a given portfolio to calculate current quantities.
- The service function will then query BigQuery to get the most recent price for each held asset.
- Combine the data to calculate the current market value for each holding.
- Expose this via an endpoint in portfolios/router.py.
#### Portfolio Value Endpoint:
- Create a service function that re-uses the holdings logic and sums the total market value.
- Expose via a simple endpoint.
#### Multi-Currency Support:
- Add a currency field to the Portfolios table (e.g., 'USD', 'ARS').
- Find a reliable API for daily exchange rates.
- Add a new table in BigQuery or Postgres for historical exchange rates.
- Update the data ingestion workflow to fetch and store these rates daily.
- Modify analytics endpoints to convert all values into the portfolio's base currency.

### Tier 3: Professional Polish & Future Ideas
#### Historical Value Endpoint:
- In portfolios/service.py, create a function that takes a portfolio and date range.
- The function will fetch all relevant transactions (Postgres) and all historical prices for the assets (BigQuery) within the date range.
- Implement the complex business logic to loop through each day, calculate the holdings on that day, and multiply by the closing price to determine the historical portfolio value.
#### Dividend Tracking:
- Add 'DIVIDEND' as an allowed type in the Transactions model.
- Update the POST /transactions endpoint to handle this new type.
- Update the analytics endpoints to correctly account for dividends in performance calculations.