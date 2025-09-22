# Article Summarizer

A web app for summarizing articles by pasting text or providing a URL, powered by Hugging Face Transformers.

## Tech Stack
- **Frontend**: Next.js, Tailwind CSS
- **Backend**: Django, GraphQL, SQLite
- **AI**: Hugging Face Transformers

![Overview](https://github.com/JDRanpariya/Article_Summarizer/blob/master/media/overview.png)

## TO DO
- [ ] Figure out how to deploy affordably for long term
- [ ] Need to add features like queue, better loading and faster processing on backend
- [ ] Extend Project
    - [ ] I want to extend this by making it place to get discussion of an article/opinions critically by imitating experts of the field and polymaths, to get different perspectives on it via LLMs
    - [ ] Not just summarize but what would great minds in the field and polymaths would say about it after thinking critically and what are the actionable insights that you can implement as daily/periodic habits to improve your life using LLMs and maybe other methods

## Getting Started
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/Article_Summarizer.git
   cd Article_Summarizer
   ```

2. **Backend Setup** (in `backend/`):
   ```bash
   cd backend
   conda env create -f env.yml
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
