# PMR3304 - Investment Info Website

A Django-based blog platform focused on investment topics, developed as part of the PMR3304 – Information Systems course at the University of São Paulo (2023). The system allows users to publish, categorize, and comment on blog posts related to finance and investments.

---

## 📚 About the Project

This web system simulates a blog-style information portal for investment content. It was created to apply backend and frontend development techniques using Django and follows best practices of software modularization and information systems. The user can explore posts, navigate by category, and leave comments when authenticated.

---

## 🚀 Features

- 🔐 User authentication (login/logout)
- 📝 Post creation, editing, and deletion via admin panel
- 💬 Commenting system for posts
- 🗂️ Post filtering by investment categories
- 🌐 Dynamic rendering with Django templating
- 🧱 Modular structure using Django apps

---

## 🖥️ Website Screens Overview

### 1. **Homepage (`/`)**
- Displays all blog posts in reverse chronological order.
- Each post shows title, date, and category.
- Navigation menu and login button included.

### 2. **Post Detail Page (`/post/<id>`)**
- Shows the full content of a selected post.
- Includes the category, date, and comment section.
- Allows logged-in users to add comments.

### 3. **Category Page (`/category/<id>`)**
- Filters posts by investment topic (e.g., Stocks, Funds).

### 4. **Login Page (`/login/`)**
- Simple login form for registered users.
- On success, user is redirected to the homepage.

### 5. **Admin Panel (`/admin/`)**
- Admin-only dashboard.
- Enables management of posts, categories, and comments.

---

## 🧰 Technologies

- **Django** (Python 3.8+)
- **SQLite3** (default Django database)
- **HTML5 + CSS3** (via templates and static folder)
- **Django Template Engine**

---

## 🖼️ Screenshots

Homepage example:  
![image](https://github.com/user-attachments/assets/0bb9bf26-9ab3-4642-8fff-ca0f0d92d919)


Post view and comments:  
![image](https://github.com/user-attachments/assets/0b86f4ab-4081-4f71-a76d-d47528edf484)

---

## ⚙️ How to Run the Project Locally

```bash
# 1. Clone the repository:
git clone https://github.com/asforaarthur/PMR3304_Investment_Info_Website.git
cd PMR3304_Investment_Info_Website

# 2. Create a virtual environment:
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# 3. Install the dependencies:
pip install -r requirements.txt

# 4. Apply migrations and run the server:
python manage.py migrate
python manage.py runserver
```
📄 License
© 2023 - All rights reserved - Arthur Asfora
