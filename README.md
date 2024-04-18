<h2>Basic FastAPI template for User Authentication with SQLite.</h2>





<h4>Folder Structure</h4>

```
/fastapi-auth-template
├── app                     # Application module
│   ├── __init__.py         # Initializes the Python package
│   ├── main.py             # Entry point to the FastAPI app; app configuration
│   ├── dependencies.py     # Dependency functions for use with FastAPI's dependency injection system
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
└── alembic.ini             # 
└── run.sh                  # Run the scripts 
```

Currently being prototyped for PC-Manager.
