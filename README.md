# Tiny AI-Powered Q&A Bot

This is a simple AI-powered app built for the intern assignment.  
It answers questions about India using Hugging Face's Q&A model and uses TextBlob for silent spell correction.  
It features both a command-line and Streamlit web UI.

---

## Features

- **Q&A bot:** Answers questions using Hugging Face's `deepset/roberta-base-squad2` model.
- **Spell correction:** Automatically corrects user spelling with TextBlob.
- **Secure API key:** Uses `.env` and `python-dotenv` for secret management (never hardcodes keys).
- **Web UI:** Simple and interactive interface built with Streamlit.

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/<21112Vivek>/tiny-ai-app.git
cd tiny-ai-app
```

### 2. Create a `.env` file

**Do NOT share or commit this file!**

```
HF_API_KEY=your_huggingface_api_key_here
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
python -m textblob.download_corpora
```

### 4. Run the command-line app

```bash
python app.py
```

### 5. Run the Streamlit web app

```bash
streamlit run streamlit_app.py
```

---

## Security

- `.env` is **listed in `.gitignore`** and never pushed to GitHub.
- Each user must create their own `.env` with their personal Hugging Face API key.

---

## Documentation

See `setup_log.md` for a record of setup steps, troubleshooting, and learning journey.

---

## Stretch Goals

- [x] Added Streamlit web UI
- [ ] Deploy to Hugging Face Spaces or Render
- [ ] Add more context and features

---

## Troubleshooting

- If you get an error about TextBlob corpora, run:
  ```
  python -m textblob.download_corpora
  ```
- If you get an API error, check your `.env` file and Hugging Face account limits.

---

## Contact

For questions or feedback, open an issue or contact me via GitHub.