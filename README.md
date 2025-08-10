# 💸 FinSage AI – Smart Personal Finance & Wealth Assistant

> A voice-enabled finance management app that tracks income, expenses, goals, and generates smart insights — powered by AI.

---

## 📌 Project Summary

FinSage AI is a personal finance desktop app that integrates:

1. **Smart Ledger with Voice Input**

   * 🎙️ Add transactions using voice commands
   * 📋 Tracks income, expenses, categories, and dates with real-time UI updates

2. **Automated Reports + Filters**

   * 🧾 Generate PDF reports with filters (date, city, province, party)
   * 📊 View summaries of balances and transactions by category or location

3. **AI-Driven Insights (Upcoming)**

   * 📈 Forecast savings, expenses, and budgets using LSTM models
   * 🤖 Integrated chatbot for financial planning tips

---

## 🧠 How it Works

### 🎙️ Voice Ledger Entry

* Voice commands (via `SpeechRecognition`) converted into text
* Parses entries like: `"Add expense 1200 groceries"`
* Stores data in structured format in SQLite or Supabase

### 🧾 Report Generation

* Select filters (city, date range, party name, province)
* Auto-generates styled PDF using FPDF / ReportLab
* Reports include transaction breakdowns and balance charts

### 📊 Financial Overview & Goals

* Track goals like “Save 10k/month” or “Limit food to 5k”
* Visual dashboards for category-wise spending
* Daily, weekly, monthly summaries using matplotlib

---

## 🧰 Tech Stack

| Category            | Tools / Frameworks        |
| ------------------- | ------------------------- |
| Language            | Python 3.10+              |
| UI Framework        | Flutter             |
| Voice Input         | SpeechRecognition         |
| Data Storage        | SQLite / Supabase         |
| Report Generation   | FPDF, ReportLab           |
| Visualization       | Matplotlib                |
| ML Forecasting (\*) | LSTM (Keras / TensorFlow) |
| NLP Chatbot (\*)    | Gemini AI / OpenAI API    |

\* in future versions (v4–v5)

---

## ⚙️ How to Run the Project

### 🔧 1. Clone the Repository

```bash
git clone https://github.com/your-username/FinSageAI.git
cd FinSageAI
```

### 🔧 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 🔧 3. Set Credentials

* Set Supabase config in `database.py`
* Add Gemini/OpenAI keys for future ML/NLP features

### 🚀 4. Launch App

```bash
python main.py
```

---

## ✨ Features

* ✅ Voice-powered income/expense tracking
* ✅ Custom filters for PDF report generation
* ✅ User goal setting and budget visualization
* ✅ Secure login and data persistence
* 🔜 AI-based forecasting and finance chatbot

---

## 🔮 Future Plans

* 📈 Integrate LSTM-based savings/expense prediction
* 🗣️ Launch AI chatbot for smart money guidance
* ☁️ Sync data with cloud for mobile version
* 📱 Release Android/iOS version
* 🧠 Add anomaly detection (fraud/overspending alerts)

---

## 📩 Contact

👤 **Afnan Shoukat**
📧 Email: [shaikhusama541@gmail.com](mailto:afnanshoukat35@gmail.com)

Feel free to reach out for:

* 🤝 Collaborations or use cases
* 💬 Suggestions or improvements
* 🧪 Customization or integration support

---


---
