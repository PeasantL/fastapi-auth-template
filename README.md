<h2>FastAPI Template for User Auth.</h2>

Basic FastAPI template for User Authentication with SQLite database integration.
Created for PC-Manager.


<h3>Steps to Run</h3>

Clone the repo.

```
git clone https://github.com/PeasantL/fastapi-auth-template
```

Edit config.py, Replace SECRET_KEY with a gen key like the following.

```
openssl rand -hex 32
```

Install the requirements.

```
python3 -m venv .venv
source "./.venv/bin/activate"
pip install -r requirements.txt
```

Create the database and run migration scripts.

```
alembic upgrade head
```

Run the program.

```
./run.sh
```

You can view the endpoints at http://127.0.0.1:8000/docs


<h3>Folder Structure</h3>

```
/fastapi-auth-template
├── app                     
│   ├── __init__.py         
│   ├── main.py             # Entry point to the FastAPI app; app configuration
│   ├── dependencies.py     # Functions for FastAPI's dependency injection system
│   ├── core                # Core application configurations and shared components
│   │   ├── __init__.py
│   │   ├── config.py       # Configuration settings and environment variables
│   │   ├── security.py     # Configuration settings and environment variables
│   │   └── database.py     # Database connection and session management
│   ├── crud                # CRUD operations on the database
│   │   ├── __init__.py
│   │   ├── crud_auth.py    # CRUD operations for authentication
│   │   ├── crud_item.py    
│   │   └── crud_user.py    
│   ├── models              # SQLAlchemy models
│   │   ├── __init__.py
│   │   ├── item.py         
│   │   └── user.py         
│   ├── schemas             # Pydantic schemas for data validation
│   │   ├── __init__.py
│   │   ├── schema_auth.py  
│   │   ├── schema_item.py  
│   │   └── schema_user.py  
│   └── routers             # Router definitions for API endpoints
│       ├── __init__.py
│       ├── router_auth.py  
│       ├── router_item.py  
│       └── router_user.py  
├── alembic                 # Database migrations
│   └── versions            # Migration scripts
└── requirements.txt        # Project dependencies
└── alembic.ini             # Alembic config 
└── run.sh                  # Run the server
```


