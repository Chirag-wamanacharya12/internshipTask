my-fullstack-app/
│
├── backend/                      # Django backend (GraphQL API)
│   ├── manage.py
│   ├── db.sqlite3
│   ├── requirements.txt
│   ├── .env
│   ├── backend/                 # Django project settings folder
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── asgi.py
│   │
│   ├── user/                    # Django app for authentication
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── schema.py           # Graphene schema for user
│   │   ├── urls.py
│   │   └── admin.py
│   │
│   └── schema.py               # Root schema that combines all app schemas
│
├── frontend/                    # Next.js frontend
│   ├── public/
│   ├── styles/
│   ├── pages/
│   │   ├── _app.js             # ApolloProvider setup
│   │   ├── index.js
│   │   └── login.js            # Sample login page
│   │
│   ├── components/             # Reusable React components
│   │   └── Navbar.js
│   │
│   ├── lib/
│   │   └── apolloClient.js     # Apollo Client setup
│   │
│   ├── .env.local
│   ├── next.config.js
│   ├── package.json
│   └── README.md

