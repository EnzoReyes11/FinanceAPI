# Work Log
See [Design document](Ahttps://docs.google.com/document/d/1xcD04pmzbedeWVP7bYmZX1wn1FIK6YwMjv_LCojADkc/edit?tab=t.0)


### 03/10/25
Moving Users routes from main.py into users/routes.
#### Done:
- Fixed many pylance errors. Improved types and reduced code.
- Trimmed code out of main into Auth, User or dependecies.
- Introduced dotenv, refactored secrets.
- Introducing WORKLOG.md
- Added LICENSE

#### Follow up
- Fill: Create user (POST /user/)
- Pylance is not finding PYJWT library, it throws errors on types.
- Add POSTGRES Database, with SQLAlchemy and Pydantic models
- Fill: GET /user/<id> . It's hardcoded.

