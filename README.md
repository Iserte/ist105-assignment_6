# 🧠 IST105 Assignment 6 — Bitwise Analyzer with MongoDB  
**Author:** Gustavo Iserte Bonfim  
**Course:** IST105 – Introduction to Programming  
**Assignment:** #6 — Django Web App with MongoDB Integration on AWS EC2  

---

## 📦 Project Structure  
**Project Name:** `assignment6`  
**App Name:** `bitwise`  
**Form:** `EntryForm` with five integer fields:  
- `a`, `b`, `c`, `d`, `e`: Integer inputs  

---

## 🧠 App Logic  
After submitting the form, the app performs:

### 🔢 Statistical Analysis  
- Calculates the average of the five numbers  
- Counts how many are positive  
- Sorts values above threshold (e.g. >10)  

### 🧮 Bitwise Classification  
- Uses bitwise logic to classify each number as even or odd  

### ⚠️ Warnings  
- Displays a warning if any negative values are detected  

### 🗃️ Data Persistence  
- Saves all results to MongoDB using Django ORM (`djongo`)  
- Collection: `entries`  

---

## 🗂️ GitHub Branches  
- `main`: Final version  
- `development`: Integration testing  
- `feature1`: Initial development  

---

## 🛠️ Technologies Used  
- Python 3  
- Django
- Djongo + MongoDB  
- AWS EC2 (Ubuntu)  
- Git & GitHub  

---

## 📄 License  
This project is for educational purposes under IST105.  
© 2025 Gustavo Iserte Bonfim