
# 📊 Amazon Review Sentiment Analyzer

Analyze Amazon product reviews and predict whether they are **Positive 👍, Negative 👎, or Neutral 😐**! Powered by **BiLSTM** and **tokenization**, this app makes sentiment analysis simple and interactive.

Try it live: [Sentiment Analysis App](https://sentiment-analysis-amzxdazcd7fad4zwddbx2x.streamlit.app/)

---

## ✨ Features

* 📝 Input Amazon reviews and get instant sentiment prediction
* 🤖 Uses **Bi-directional LSTM** for accurate sentiment detection
* 🔤 Text is preprocessed & tokenized for best results
* 🌐 Interactive **Streamlit interface** for easy use

---

## 🚀 Installation

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-link>
cd <your-repo-folder>
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

**Common Packages:**
`tensorflow`, `keras`, `numpy`, `pandas`, `nltk` / `spacy`, `streamlit`, `scikit-learn`

---

## 🛠️ Usage

### 1️⃣ Load Your Trained Model

```python
from tensorflow.keras.models import load_model
import pickle

model = load_model("sentiment_model.h5")
with open("tokenizer.pickle", "rb") as f:
    tokenizer = pickle.load(f)
```

### 2️⃣ Run the Streamlit App

```bash
streamlit run app.py
```

* App opens in browser: `http://localhost:8501`
* Type/paste your Amazon review to see sentiment: **👍 / 👎 / 😐**

---

## 📁 Project Structure

```
project-folder/
│
├── app.py                 # Streamlit interface
├── sentiment_model.h5     # BiLSTM trained model
├── tokenizer.pickle       # Tokenizer used for preprocessing
├── requirements.txt       # Dependencies
└── README.md              # Project documentation
```

---

## 💡 How It Works

1. **Text Preprocessing**

   * Clean, lowercase, and tokenize reviews
   * Convert to sequences and pad

2. **BiLSTM Model**

   * Reads text in both directions
   * Captures context for accurate predictions

3. **Prediction**

   * Outputs probability for Positive 👍, Negative 👎, Neutral 😐
   * Returns sentiment with the highest probability

---

## 🌐 Deployment

* Deployed on **Streamlit Cloud**:
  [https://sentiment-analysis-amzxdazcd7fad4zwddbx2x.streamlit.app/](https://sentiment-analysis-amzxdazcd7fad4zwddbx2x.streamlit.app/)

**To deploy your own:**

1. Push your repo to GitHub
2. Go to [Streamlit Community Cloud](https://streamlit.io/cloud)
3. Click **New App → Select Repository → Deploy**

---

## 🔮 Future Enhancements

* 🌎 Multi-language review support
* 📈 Visualize sentiment distribution in graphs
* 🤝 Integrate with e-commerce platforms for real-time analysis
* 💾 Add database to save review history

---


