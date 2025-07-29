#  NeuroKeys - AI Virtual Keyboard

NeuroKeys is an AI-powered virtual keyboard that allows users to type using only hand gestures, powered by computer vision and deep learning. It uses Mediapipe and OpenCV to detect hand landmarks and translate gestures into keystrokes.

---

##  Features

-  Real-time hand tracking
-  On-screen virtual keyboard
-  Gesture-based key press detection
-  TensorFlow Lite models for efficient inference
-  No need for physical keyboards — just use your fingers!

---

##  Tech Stack

- **Python 3**
- **OpenCV**
- **Mediapipe**
- **TensorFlow Lite**
- **NumPy**

---

## 🚀 How to Run

1. **Clone the repository**

```bash
git clone https://github.com/vedantulhe12/NeuroKeys.git
cd NeuroKeys
```

2. **Create a virtual environment**

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

3. **Install the dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the app**

```bash
python main.py
```

---

## ✋ How to Use

- Raise your hand in front of your webcam.
- A virtual keyboard will appear.
- Use your **index finger and thumb** to "press" a key by bringing them close together.
- The pressed key will be printed in the terminal.

> Tip: Keep your hand steady and use slow, deliberate motions for better accuracy.

---

## 📁 Directory Structure

```
NeuroKeys/
│
├── main.py               # Main application file
├── HandTrackingModule.py # Custom hand detector logic
├── models/               # TensorFlow Lite models
├── assets/               # Key graphics, fonts, etc.
├── requirements.txt      # Python dependencies
└── README.md             # You're here!
```

---

##  License

MIT License — feel free to use, modify, and contribute!

---

