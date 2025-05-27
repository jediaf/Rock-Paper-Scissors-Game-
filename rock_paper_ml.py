import streamlit as st
import random
import numpy as np
from sklearn.tree import DecisionTreeClassifier

# Page config
st.set_page_config(page_title="Rock Paper Scissors AI", page_icon="✊📄✂")
st.title("✊ 📄 ✂ Rock Paper Scissors with AI")

# Sidebar AI type selection
st.sidebar.title("⚙️ Game Settings")
ai_type = st.sidebar.radio("Select AI Type:", ["Rule-Based", "Machine Learning"])

# Detect AI type change and reset if needed
if "last_ai_type" not in st.session_state:
    st.session_state.last_ai_type = ai_type

if st.session_state.last_ai_type != ai_type:
    for key in ["X", "y", "model", "player_score", "ai_score", "ai_move", "result", "pending_ai_move"]:
        if key in st.session_state:
            del st.session_state[key]
    st.session_state.model = DecisionTreeClassifier()
    st.session_state.last_ai_type = ai_type
    st.success(f"🔄 Switched to {ai_type} mode. Starting fresh game.")

# Initialize session state
if "X" not in st.session_state:
    st.session_state.X = []
    st.session_state.y = []
    st.session_state.model = DecisionTreeClassifier()
    st.session_state.ai_move = ""
    st.session_state.result = ""
    st.session_state.player_score = 0
    st.session_state.ai_score = 0
    st.session_state.pending_ai_move = ""

moves = ["rock", "paper", "scissors"]
emoji_map = {"rock": "🪨", "paper": "📄", "scissors": "✂"}

# Update ML model
def update_model():
    if len(st.session_state.X) >= 5:
        X_np = np.array(st.session_state.X)
        y_np = np.array(st.session_state.y)
        st.session_state.model.fit(X_np, y_np)

# Rule-based AI
def rule_based_ai():
    return random.choice(moves)  # fair: choose before knowing player move

# ML-based AI
def ml_based_ai():
    if len(st.session_state.X) < 5:
        return random.choice(moves)
    last = np.array([st.session_state.X[-1]])
    predicted = st.session_state.model.predict(last)[0]
    counter = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
    return counter[predicted]

# Update scores and result
def update_scores(player, ai):
    if player == ai:
        st.session_state.result = "🤝 It's a draw!"
    elif (player == "rock" and ai == "scissors") or \
         (player == "paper" and ai == "rock") or \
         (player == "scissors" and ai == "paper"):
        st.session_state.result = "🎉 You win this round!"
        st.session_state.player_score += 1
    else:
        st.session_state.result = "🤖 AI wins this round!"
        st.session_state.ai_score += 1

# Prepare next AI move before user input
if not st.session_state.pending_ai_move:
    if ai_type == "Rule-Based":
        st.session_state.pending_ai_move = rule_based_ai()
    elif ai_type == "Machine Learning":
        st.session_state.pending_ai_move = ml_based_ai()

# Game UI
st.subheader("Choose your move:")

col1, col2, col3 = st.columns(3)
player_move = None

if col1.button("🪨 Rock"):
    player_move = "rock"
elif col2.button("📄 Paper"):
    player_move = "paper"
elif col3.button("✂ Scissors"):
    player_move = "scissors"

# Play round
if player_move:
    if len(st.session_state.X) == 0:
        st.session_state.X.append([0, 0, 0])
    else:
        last = st.session_state.X[-1]
        st.session_state.X.append(last)

    if player_move == "rock":
        st.session_state.X[-1] = [1, 0, 0]
    elif player_move == "paper":
        st.session_state.X[-1] = [0, 1, 0]
    else:
        st.session_state.X[-1] = [0, 0, 1]

    st.session_state.y.append(player_move)
    update_model()

    ai_move = st.session_state.pending_ai_move
    st.session_state.pending_ai_move = ""  # clear for next round

    update_scores(player_move, ai_move)
    st.session_state.ai_move = ai_move
    st.rerun()

# Show result
if st.session_state.ai_move:
    st.markdown(f"### 🤖 **AI played:** {emoji_map[st.session_state.ai_move]} `{st.session_state.ai_move.capitalize()}`")

    if st.session_state.result == "🎉 You win this round!":
        st.success(st.session_state.result)
    elif st.session_state.result == "🤖 AI wins this round!":
        st.error(st.session_state.result)
    else:
        st.info(st.session_state.result)

    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(f"""
        <div style='text-align:center; font-size:28px;'>
            🧝 You: <strong>{st.session_state.player_score}</strong> &nbsp;|&nbsp; 🤖 AI: <strong>{st.session_state.ai_score}</strong>
        </div>
        """, unsafe_allow_html=True)

# Reset button
col1, col2, col3 = st.columns(3)
with col2:
    if st.button("🔄 Reset Game"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()