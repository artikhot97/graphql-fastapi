# data.py - central location for all mock/demo data

# Users
db_users = {
    1: {"id": 1, "name": "Alice"},
    2: {"id": 2, "name": "Bob"},
    3: {"id": 3, "name": "Charlie"},
    4: {"id": 4, "name": "Diana"},
    5: {"id": 5, "name": "Eve"},
    6: {"id": 6, "name": "Frank"},
    7: {"id": 7, "name": "Grace"},
    8: {"id": 8, "name": "Heidi"},
    9: {"id": 9, "name": "Ivan"},
    10: {"id": 10, "name": "Judy"},
    11: {"id": 11, "name": "Karl"},
    12: {"id": 12, "name": "Laura"},
    13: {"id": 13, "name": "Mallory"},
    14: {"id": 14, "name": "Niaj"},
    15: {"id": 15, "name": "Olivia"},
    16: {"id": 16, "name": "Peggy"},
    17: {"id": 17, "name": "Rupert"},
    18: {"id": 18, "name": "Sybil"},
    19: {"id": 19, "name": "Trent"},
    20: {"id": 20, "name": "Victor"},
}

# Posts
db_posts = [
    {"id": 1, "title": "Hello World", "content": "First post!", "user_id": 1, "tags": ["intro", "welcome"]},
    {"id": 2, "title": "GraphQL is cool", "content": "GraphQL with Strawberry is awesome!", "user_id": 2, "tags": ["graphql", "python"]},
    {"id": 3, "title": "Strawberry Dataloader", "content": "Batching and caching with DataLoader.", "user_id": 1, "tags": ["dataloader", "performance"]},
    {"id": 4, "title": "Nested Demo", "content": "Nested fields example.", "user_id": 2, "tags": ["nested", "demo"]},
]

# Tags
db_tags = [
    {"id": 1, "name": "intro", "post_ids": [1]},
    {"id": 2, "name": "welcome", "post_ids": [1]},
    {"id": 3, "name": "graphql", "post_ids": [2]},
    {"id": 4, "name": "python", "post_ids": [2]},
    {"id": 5, "name": "dataloader", "post_ids": [3]},
    {"id": 6, "name": "performance", "post_ids": [3]},
    {"id": 7, "name": "nested", "post_ids": [4]},
    {"id": 8, "name": "demo", "post_ids": [4]},
]

# Books
db_books = [
    {"title": "1984", "author": "George Orwell", "description": "A dystopian novel about totalitarianism and surveillance."},
    {"title": "Clean Code", "author": "Robert C. Martin", "description": "A handbook of agile software craftsmanship."},
    {"title": "The Pragmatic Programmer", "author": "Andrew Hunt, David Thomas", "description": "Tips for effective and pragmatic software development."},
    {"title": "Design Patterns", "author": "Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides", "description": "A catalog of classic software design patterns."},
    {"title": "Python Crash Course", "author": "Eric Matthes", "description": "A fast-paced introduction to programming with Python."},
    {"title": "Fluent Python", "author": "Luciano Ramalho", "description": "Clear, practical advice for writing idiomatic Python."},
    {"title": "You Don't Know JS", "author": "Kyle Simpson", "description": "A deep dive into the core mechanisms of JavaScript."},
    {"title": "Refactoring", "author": "Martin Fowler", "description": "Improving the design of existing code."},
    {"title": "Test-Driven Development", "author": "Kent Beck", "description": "By example, how to use TDD for robust code."},
    {"title": "Effective Java", "author": "Joshua Bloch", "description": "Best practices for the Java programming language."},
    # AI & Machine Learning books
    {"title": "Artificial Intelligence: A Modern Approach", "author": "Stuart Russell, Peter Norvig", "description": "The leading textbook in AI, covering theory and practice."},
    {"title": "Deep Learning", "author": "Ian Goodfellow, Yoshua Bengio, Aaron Courville", "description": "Comprehensive resource on deep learning methods and theory."},
    {"title": "Pattern Recognition and Machine Learning", "author": "Christopher Bishop", "description": "A foundational text for machine learning and pattern recognition."},
    {"title": "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow", "author": "Aurélien Géron", "description": "Practical guide to building ML systems with Python."},
    {"title": "Machine Learning: A Probabilistic Perspective", "author": "Kevin P. Murphy", "description": "A modern introduction to machine learning from a probabilistic viewpoint."},
    {"title": "Reinforcement Learning: An Introduction", "author": "Richard S. Sutton, Andrew G. Barto", "description": "The classic book on reinforcement learning theory and algorithms."},
    {"title": "The Hundred-Page Machine Learning Book", "author": "Andriy Burkov", "description": "A concise overview of machine learning concepts and techniques."},
    {"title": "Grokking Deep Learning", "author": "Andrew Trask", "description": "A beginner-friendly introduction to deep learning."},
    {"title": "Machine Learning Yearning", "author": "Andrew Ng", "description": "Practical advice for structuring machine learning projects."},
]
