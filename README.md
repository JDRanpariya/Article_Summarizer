# Article Summarizer

A web app for summarizing articles by pasting text or providing a URL, powered by Hugging Face Transformers.

## Tech Stack
- **Frontend**: Next.js, Tailwind CSS
- **Backend**: Django, GraphQL, SQLite
- **AI**: Hugging Face Transformers

![Overview](https://github.com/JDRanpariya/Article_Summarizer/blob/master/media/overview.png)

## Getting Started
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/Article_Summarizer.git
   cd Article_Summarizer
   ```

2. **Backend Setup** (in `backend/`):
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   python manage.py runserver
   ```
   See `backend/README.md` for details.

3. **Frontend Setup** (in `frontend/`):
   ```bash
   cd frontend
   npm install
   npm run dev
   ```
   Open [http://localhost:3000](http://localhost:3000). See `frontend/README.md` for details.

## Deployment
- **Frontend**: Deploy on Vercel (see `frontend/README.md`).
- **Backend**: Deploy on a Python-compatible host (e.g., Heroku, Railway).
