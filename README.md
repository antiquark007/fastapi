backend/
├── app/
│   ├── main.py                # Entry point for the application
│   ├── auth/
│   │   ├── routes.py          # Authentication-related API endpoints
│   │   ├── jwt_handler.py     # Functions for creating and verifying JWT tokens
│   │   └── __init__.py        # Makes the `auth` directory a module
│   ├── models/
│   │   ├── user.py            # Pydantic models for user data
│   │   └── __init__.py        # Makes the `models` directory a module
│   ├── database/
│   │   ├── connection.py      # MongoDB connection logic using Motor or PyMongo
│   │   └── __init__.py        # Makes the `database` directory a module
│   ├── middleware/
│   │   ├── authenticate.py    # Middleware to validate JWT tokens for protected routes
│   │   └── __init__.py        # Makes the `middleware` directory a module
│   └── __init__.py            # Makes the `app` directory a module
├── tests/
│   ├── test_auth.py           # Unit tests for authentication endpoints
│   └── conftest.py            # Test configuration and fixtures
├── .env                       # Environment variables (e.g., MongoDB URI, JWT secret key)
├── requirements.txt           # Python dependencies
└── Dockerfile                 # Docker configuration for containerization
