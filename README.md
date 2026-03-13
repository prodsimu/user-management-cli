<div align="center">
<h1>User Management CLI</h1>
</div>

## 👩‍💻 Tech Stack
[![Python](https://img.shields.io/badge/Vanilla_Python-3776AB?style=for-the-badge&logo=python&logoColor=fff)](#)

## 💡 Overview

A Command-line user management system built with Vanilla Python.

## ✨ Features
- User authentication system
- Role-based access control (admin / user)
- User management (CRUD)
- Password hashing
- Automatic admin seeding
- CLI interface with interactive menus
- Custom exception handling

## 🏗️ Architecture

The project follows a layered architecture:

- **UI** – CLI interface
- **Controllers** – Application flow orchestration
- **Services** – Business logic
- **Repositories** – Data access layer
- **Models** – Users and sessions

## 📂 Project Structure

```
user-management-cli/
├── app/
│   ├── controllers/
│   │   └── app_controller.py
│   ├── database/
│   │   └── database.py
│   ├── exceptions/
│   │   └── exceptions.py
│   ├── models/
│   │   ├── session.py
│   │   └── user.py
│   ├── repositories/
│   │   ├── base_repository.py
│   │   ├── session_repository.py
│   │   └── user_repository.py
│   ├── security/
│   │   └── password_hasher.py
│   ├── seed/
│   │   └── seed.py
│   ├── services/
│   │   ├── session_service.py
│   │   └── user_service.py
│   ├── ui/
│   │   ├── cli.py
│   │   ├── menus.py
│   │   └── prompts.py
│   └── utils/
│       └── terminal.py
└── main.py
```

## 🛠️ Installation

### 1. Clone the repository
```
git clone https://github.com/prodsimu/user-management-cli.git
cd user-management-cli
```

### 2. Run the application
```
python main.py
```
