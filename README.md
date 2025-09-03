# 🛍️ MahmoudWafiStore

A modern **Django E-Commerce Website** with custom user authentication, product management, cart functionality, and an elegant frontend built with Bootstrap.  
This project is designed to be simple, scalable, and developer-friendly.

---

## 🚀 Features

- ✅ User Registration & Login (Custom User Model with email authentication)
- ✅ Category & Product Management
- ✅ Product Search (by name & slug)
- ✅ Product Pagination
- ✅ Cart Functionality (Add, Remove, Update Quantities)
- ✅ Dynamic Navbar with Categories (via context processors)
- ✅ Jazzmin Customized Admin Dashboard
- ✅ Responsive UI (Bootstrap 4)
- ✅ Slug-based SEO-friendly URLs

---

## 🛠️ Technologies Used

- **Backend:** Django 5+, SQLite (default, easy to switch to PostgreSQL/MySQL)
- **Frontend:** HTML, CSS, Bootstrap 4, JavaScript (jQuery)
- **Admin Dashboard:** Jazzmin
- **Other Tools:** Git, Virtualenv

---

## ⚙️ Installation & Setup

Clone the repository:

```bash
git clone https://github.com/yourusername/mahmoudwafistore.git
cd mahmoudwafistore
python3 -m venv env
source env/bin/activate   # Linux/Mac
env\Scripts\activate      # Windows
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

git clone https://github.com/yourusername/mahmoudwafistore.git
cd mahmoudwafistore
