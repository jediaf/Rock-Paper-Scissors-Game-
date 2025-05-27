# 🧠 Rock-Paper-Scissors AI Game (CENG 3511 Final Project)

This is a web-based Rock-Paper-Scissors game developed for the **CENG 3511: Artificial Intelligence** course final project. The game allows users to play against two types of AI agents:
- **Rule-Based AI:** Chooses moves randomly.
- **Machine Learning AI:** Learns from user patterns using a Decision Tree classifier.

Built with **Python** and **Streamlit**, the app runs entirely in the browser and demonstrates how AI can make decisions in a simple, turn-based environment.

---

## 🚀 Features

- 🎮 Interactive gameplay with graphical buttons and emojis  
- 🧠 Selectable AI types: Rule-Based and Machine Learning  
- 📈 Real-time score tracking and move history  
- 🔁 AI switching resets game state for fair comparison  
- 🌐 Streamlit-powered web interface  

---

## 📦 Requirements

Make sure you have Python 3.7+ installed.
Install required libraries:

```bash
pip install streamlit scikit-learn numpy

---

## ▶️ Run the App

streamlit run rock_paper_ml.py

Then open the provided local URL in your browser.

---

## 🛠️ AI Agents Explained

Rule-Based AI
-Picks moves randomly
-Does not learn or adapt

Machine Learning AI
-Uses a Decision Tree (sklearn.tree.DecisionTreeClassifier)
-Learns from your previous moves after round 5
-Attempts to predict your next move and beat it

---

## 📝 Project Structure

rock_paper_ml.py         # Main game and AI logic
README.md                # Project documentation

---

## Course Outcomes Demonstrated
Applying AI in an interactive system
Decision-making using rules and ML
Evaluating AI behavior in a game environment
Experience with Streamlit and Scikit-learn

---
📌 Author
Ceyda Arık
---
📄 License
This project is for educational purposes only.


