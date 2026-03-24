# 🧮 Command-Line Spreadsheet (Python)

![Python](https://img.shields.io/badge/Python-3.x-blue)
![CLI](https://img.shields.io/badge/Interface-CLI-green)
![Status](https://img.shields.io/badge/Status-Complete-success)

---

## 📌 Overview

This project is a **command-line spreadsheet application** built in Python.
It simulates core spreadsheet functionalities such as cell manipulation, range selection, mathematical operations, and file persistence.

---

## 🚀 Features

### 📊 Spreadsheet Operations

* Create custom-sized sheets
* Navigate using a cursor (`goto`)
* Insert, delete, and read cell values

### 🔲 Selection Handling

* Select a range of cells
* Retrieve selection coordinates

### 🧮 Mathematical Functions

* Sum
* Multiplication
* Average
* Maximum

### 🔁 Undo / Redo

* Implemented using **stack data structure**
* Supports reversing and reapplying actions

### 💾 File Handling

* Save spreadsheet to file (JSON format)
* Load previously saved data

### 💻 Command-Line Interface

* Interactive CLI for executing commands
* User-friendly and structured input system

---

## 🧠 Concepts Used

* Object-Oriented Programming (OOP)
* 2D Arrays (Lists)
* Stack (Undo/Redo)
* File Handling (JSON)
* Input Parsing (CLI design)

---

## 📌 Example Commands

```
create 5 5
goto 1 2
insert 100
select 3 4
sum 0 0
printsheet
undo
redo
save data.json
load data.json
```

---

## 📁 Project Structure

```
Command-Line-Spreadsheet-Python/
│── spreadsheet.py
│── README.md
```

---

## ▶️ How to Run

```bash
python spreadsheet.py
```

---

## 📈 Future Improvements

* Excel-style formulas (`=A1+B1`)
* GUI version (Tkinter / PyQt)
* Data visualization integration
* Performance optimization

---

## 👨‍💻 Author

**Harris Pervez**
Computer Science  Student

---
