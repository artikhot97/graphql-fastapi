# graphql-fastapi

A FastAPI project demonstrating GraphQL integration with Strawberry, DataLoader batching, and a modular structure for social media posts, users, tags, and books (including AI/ML books).

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
{
  fetchBooks {
    title
    author
    description
  }
}
```

#### Search books
```graphql
{
  searchBooks(searchText: "AI") {
    title
    author
    description
  }
}
```

### Screenshot: Fetch All Books

![Fetch All Books](screenshots/fetch-all-books.png)

### Screenshot: Search Books

![Search Books](screenshots/search-books.png)

## Screenshots

Below are some screenshots of the GraphQL Playground in action:

### Search Books by AI
![Search Books by AI](screenshots/search-books-ai.png)

### Fetch All Books
![Fetch All Books](screenshots/fetch-all-books.png)

## 📝 Post API

The Post API allows you to fetch all posts, including their users and tags, using efficient DataLoader batching.

### Example Query

#### Fetch all posts with user and tags
```graphql
{
  getPosts {
    id
    title
    content
    user {
      name
      description
    }
    tagObjects {
      name
    }
    userId
  }
}
```

#### Fetch post detail by ID
```graphql
{
  getPostDetail(postId: 1) {
    content
    tagObjects {
      name
      postIds
    }
    title
  }
}
```

### Screenshot: Get Posts

![Get Posts](screenshots/get-posts.png)

### Screenshot: Get Post Detail

![Get Post Detail](screenshots/get-post-detail.png)

## User API

The User API allows you to fetch user information using GraphQL queries. You can retrieve all users or fetch a specific user by their ID. The API uses DataLoader for efficient batching and caching of user data.

### Fetch All Users

**Sample Query:**
```graphql
query {
  fetchUsers {
    id
    name
    description
  }
}
```

**Sample Response:**
```json
{
  "data": {
    "fetchUsers": [
      { "id": 1, "name": "Alice", "description": "User Alice" },
      { "id": 2, "name": "Bob", "description": "User Bob" },
      // ...more users
    ]
  }
}
```

**Screenshot:**

![fetchUsers Screenshot](./screenshots/fetchUsers.png)

---

Feel free to contribute or open issues!
