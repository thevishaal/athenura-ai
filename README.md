# 🚀 Athenura AI

A modern **Django based web application** with multiple content and AI tools.

This project is built using **Django + Tailwind CSS** and structured for **team collaboration** so developers can easily clone the repository and run the project locally.

---

# 📌 Features

### 👤 Authentication
- User registration
- Login / Logout system
- User management

### 🤖 AI Tools
- Article generator
- Blog generator
- Caption generator
- Social media tools

### 🎨 Modern UI
- Built using **Tailwind CSS**
- Responsive design
- Clean and minimal interface

### 🔐 Security
- Environment variables using `.env`
- Sensitive data not stored in repository

---

# 🧰 Tech Stack

| Technology | Usage |
|------------|------|
| Backend | Django |
| Frontend | HTML + Tailwind CSS |
| Database | SQLite |
| Styling | Tailwind |
| Package Manager | pip + npm |

---

# 📁 Project Structure

```
project-root/

accounts/          # authentication app
article/           # article generator
athenura_ai/       # main django project
blog/              # blog generator
caption/           # caption generator
core/              # core utilities
social_media/      # social tools

theme/             # tailwind css app

media/

manage.py
requirements.txt
.env.example
README.md
```

---

# ⚙️ Installation Guide

Follow the steps below to run the project locally.

---

# 1️⃣ Clone Repository

```
git clone https://github.com/thevishaal/athenura-ai
```

```
cd project-folder
```

---

# 2️⃣ Create Virtual Environment

```
python -m venv .venv
```

### Activate Environment

**Windows**

```
.venv\Scripts\activate
```

**Linux / Mac**

```
source .venv/bin/activate
```

---

# 3️⃣ Install Python Dependencies

```
pip install -r requirements.txt
```

---

# 4️⃣ Install Tailwind Dependencies

Go inside the theme app.

```
cd theme/static_src/
```

Install node modules.

```
npm install
```

---

# 5️⃣ Configure Environment Variables

Create a `.env` file in the project root directory.

Example:

```
.env.example
```

⚠️ Never commit `.env` to GitHub.

---

# 6️⃣ Database Setup

Run migrations.

```
python manage.py makemigrations
python manage.py migrate
```

---

# 7️⃣ Create Admin User

```
python manage.py createsuperuser
```

---

# 8️⃣ Start Tailwind CSS

Run Tailwind watcher to compile CSS.

```
python manage.py tailwind start
```

---

# 9️⃣ Run Django Server

```
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000/
```

Admin panel:

```
http://127.0.0.1:8000/admin/
```

---

# 🔐 Environment Security

Sensitive credentials are stored in `.env`.

`.env` is ignored using `.gitignore`.

Developers should use `.env.example` as reference.

---

# 📦 Required Software

Make sure the following tools are installed:

- Python 3.10+
- Node.js
- npm
- Git

---

# 👨‍💻 Development Workflow

Pull latest code

```
git pull
```

Install dependencies

```
pip install -r requirements.txt
npm install
```

Run Tailwind

```
python manage.py tailwind start
```

Start Django server

```
python manage.py runserver
```

---

# 🤝 Contributing

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push the branch
5. Create a Pull Request

---