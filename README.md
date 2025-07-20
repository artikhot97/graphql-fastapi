# graphql-fastapi

This repository demonstrates a production-style FastAPI project integrated with:

✅ Strawberry GraphQL — for clean, type-safe GraphQL APIs

✅ DataLoader — for efficient batching and per-request caching (solve the N+1 problem)

✅ Modular structure — for scalable domains like Posts, Users, Tags, and Books (including AI/ML books)

🔍 What you'll find inside:

Sample GraphQL queries & mutations for real-world use cases

Optimized resolvers using DataLoader to prevent redundant DB calls

Well-organized modules for each domain (users, posts, tags, books)

Async-friendly code with FastAPI’s best practices

🚀 Ideal for:

Backend engineers learning GraphQL in Python

Teams exploring DataLoader batching in real-world GraphQL APIs

FastAPI + Strawberry integration examples

Developers interested in modular API architecture

## Features
- FastAPI + Strawberry GraphQL integration
- DataLoader for efficient batching (users, tags)
- Modular folder structure
- Demo data for users, posts, tags, and books (including AI/ML books)
- Search functionality for books

## Project Structure
```
├── app/
│   ├── dataloaders/
│   │   ├── user_loader.py
│   │   ├── tag_loader.py
│   ├── graphql_types/
│   │   ├── books.py
│   │   ├── post.py
│   │   ├── tag.py
│   │   ├── user.py
├── data.py
├── main.py
├── requirements.txt
├── README.md
```

## Setup
1. Clone the repo and navigate to the project root.
2. Create and activate a virtual environment:
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```
3. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

## Running the App
From the project root, run:
```powershell
uvicorn main:app --reload
```

Visit [http://localhost:8000/graphql](http://localhost:8000/graphql) for the GraphQL Playground.

## Example GraphQL Queries
### Fetch all books
```graphql
{
  fetchBooks {
    title
    author
    description
  }
}
```
### Search books
```graphql
{
  searchBooks(searchText: "machine learning") {
    title
    author
    description
  }
}
```
### Fetch posts with users and tags
```graphql
{
  posts {
    title
    content
    user { name }
    tagObjects { name description }
  }
}
```

## 📚 Books API

The Books API allows you to fetch all books or search for books by title, author, or description.

### Example Queries

#### Fetch all books
```graphql
query MyQuery {
  fetchBooks {
    author
    title
    description
  }
}
```

#### Search books
```graphql
query MyQuery {
  searchBooks(searchText: "AI") {
    author
    description
    title
  }
}
```


## Screenshots

Below are some screenshots of the GraphQL Playground in action:

### Screenshot: Search Books

<img width="1914" height="714" alt="image" src="https://github.com/user-attachments/assets/436a5dd7-d43b-41a1-b546-58328690e830" />


### Fetch All Books
<img width="1914" height="955" alt="image" src="https://github.com/user-attachments/assets/586bd794-3c1d-4c94-a584-3e7888be1360" />


## 📝 Post API

The Post API allows you to fetch all posts, including their users and tags, using efficient DataLoader batching.

### Example Query

#### Fetch all posts with user and tags
```graphql
query MyQuery {
  getPosts {
    content
    id
    tagObjects {
      name
      id
    }
    title
    userId
    user {
      id
      name
    }
  }
}
```

#### Fetch post detail by ID
```graphql
query MyQuery {
  getPostDetail(postId: 4) {
    content
    id
    title
    user {
      description
      id
      name
    }
    userId
    tagObjects {
      name
      postIds
      id
      description
    }
  }
}
```

### Screenshot: Get Posts

<img width="1907" height="952" alt="image" src="https://github.com/user-attachments/assets/24b8d0a7-2e84-4068-af4c-15a206a9cdab" />


### Screenshot: Get Post Detail

<img width="1916" height="938" alt="image" src="https://github.com/user-attachments/assets/dfcf96bf-8645-4cb4-bef3-631fab5e4dc1" />


## User API

The User API allows you to fetch user information using GraphQL queries. You can retrieve all users or fetch a specific user by their ID. The API uses DataLoader for efficient batching and caching of user data.

### Fetch All Users

**Sample Query:**
```graphql
query MyQuery {
  fetchUsers {
    id
    name
  }
}
```

**Sample Response:**
```json
{
  "data": {
    "fetchUsers": [
      {
        "id": 1,
        "name": "Alice"
      },
      {
        "id": 2,
        "name": "Bob"
      },
      {
        "id": 3,
        "name": "Charlie"
      },
      {
        "id": 4,
        "name": "Diana"
      },
      {
        "id": 5,
        "name": "Eve"
      },
      ......
    ]
  }
}
```

**Screenshot:**

<img width="1910" height="934" alt="image" src="https://github.com/user-attachments/assets/252eb21c-c4c8-45b0-80e2-c7dbe7c5b60b" />


### FetchUserById
**Sample Query:**
```
query MyQuery {
  fetchUserById(userId: 10) {
    id
    name
    description
  }
}
```
**Sample Response:**
```
{
  "data": {
    "fetchUserById": {
      "id": 10,
      "name": "Judy",
      "description": "User Judy"
    }
  }
}
```

<img width="1899" height="707" alt="image" src="https://github.com/user-attachments/assets/274a7bc8-e960-416e-b29a-a712516baec5" />


---

Feel free to contribute or open issues!
