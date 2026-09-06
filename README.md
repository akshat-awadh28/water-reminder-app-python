# 💧 Water Reminder App

A simple **Python desktop application** that reminds you to drink water at regular intervals. The application can run silently in the background using `pythonw`.

## ✨ Features

* 🔔 Desktop notification reminders
* ⏰ Customizable reminder interval
* 🖥️ Runs in the background
* 💧 Lightweight and easy to use
* 🎨 Custom notification icon

## 🛠️ Tech Stack

* **Python**
* **Plyer** – Desktop notifications

## 📂 Project Structure

```text
water-reminder-app-python/
│
├── scripts/
│   └── water_reminder_app.py
│
├── app_icons/
│   └── water_glass_icon.ico
│
└── README.md
```

## 🚀 Setup

Install the required Python package:

```bash
pip install plyer
```

## ▶️ Run the Application

Run normally:

```bash
python scripts/water_reminder_app.py
```

Run silently in the background on Windows:

```bash
pythonw scripts/water_reminder_app.py
```

## ⏰ Change Reminder Interval

The default reminder interval is **1 hour**.

Modify the following line in the Python script:

```python
time.sleep(60 * 60)
```

For example, for a 30-minute reminder:

```python
time.sleep(30 * 60)
```

## 🎯 Purpose

A simple productivity and wellness utility designed to help users **stay hydrated during long working or study sessions**.

---

**Author:** Akshat
