# 🌐 User Management System – Internship Task

Welcome to the **User Management System** – a secure, sleek, and dynamic Django-based web application built as part of the **CodeB Internship Task**. This project demonstrates essential web development practices including authentication, role-based access, user dashboards, password recovery, and admin functionalities.

> 🔗 **Live Demo:** [chirag18.pythonanywhere.com](https://chirag18.pythonanywhere.com)  
> 💻 **Repository:** [GitHub - internshipTask](https://github.com/Chirag-wamanacharya12/internshipTask.git)

---

## 📌 Features Overview

### 🔐 User Registration (Optional for Multi-role Setup)
A user-friendly registration form where users can sign up with:
- Full Name
- Unique Username
- Email
- Password & Confirm Password
- Role Selection (Admin, Viewer, Guest, etc.)

### 🔑 Login Panel
Secure login interface for both Admins and Users:
- Email and Password input
- Password visibility toggle
- Links: Register | Forgot Password
- Social login options (Google/Facebook)

### ❌ Invalid Credentials
Handles incorrect login attempts with:
- Real-time authentication checks
- "Invalid credentials" error feedback
- Secure login validation

### ✅ Dashboard Access
After successful login, users are redirected to personalized dashboards:
- Displays welcome message and user email
- Logout option to terminate session

### 🛠️ Admin Panel
Admins can:
- View and manage all registered users
- Edit or delete user records
- Navigate through Dashboard, Search, Insights, Logout

### 🗑️ Real-Time User Deletion
- Admins can delete users instantly
- Dynamic UI reflects changes immediately
- Consistent design post-update

### 🔄 Forgot & Reset Password
- Send reset link via email
- Secure, time-bound reset tokens
- Confirmation messages enhance user experience

### ⏳ Session Management
- Sessions expire after inactivity (configurable)
- Optional auto-logout on browser close
- Uses Django's secure session backend

---

## 🛠️ Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: SQLite3 (default Django setup)
- **Hosting**: [PythonAnywhere](https://www.pythonanywhere.com/)
- **Version Control**: Git + GitHub

---

## 🚀 Getting Started (Local Setup)

### 1. Clone the Repository
```bash
git clone https://github.com/Chirag-wamanacharya12/internshipTask.git
cd internshipTask
