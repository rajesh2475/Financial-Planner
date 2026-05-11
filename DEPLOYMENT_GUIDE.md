# Wealth Navigator - Deployment Guide

## Free Deployment Options

### Option 1: Render (Recommended) ⭐
**Best for**: Easy deployment, good performance, free tier available

1. **Sign up** at [render.com](https://render.com)
2. **Connect your GitHub repository**
3. **Create a new Web Service**:
   - Select your GitHub repository
   - Environment: `Python 3.10`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn run:app`
4. **Environment Variables** (add in Render dashboard):
   - No special variables needed for basic setup
5. **Deploy!** - Your app will be live in minutes

**Live URL**: `https://wealth-navigator.onrender.com`

---

### Option 2: Heroku (Free tier ended, but still an option)
**Note**: Heroku's free tier ended November 2022, but you can use Hobby tier ($7/month)

1. **Sign up** at [heroku.com](https://heroku.com)
2. **Install Heroku CLI**
3. **Deploy**:
   ```bash
   heroku login
   heroku create wealth-navigator
   git push heroku main
   ```

---

### Option 3: Replit
**Best for**: Quick deployment, learning, free tier

1. **Go to** [replit.com](https://replit.com)
2. **Import from GitHub** - paste your repo URL
3. **Run the app** - Click "Run" button
4. **Share** - Get a free public URL

---

### Option 4: PythonAnywhere
**Best for**: Python-specific hosting

1. **Sign up** at [pythonanywhere.com](https://pythonanywhere.com)
2. **Upload your code** via Git or file upload
3. **Configure WSGI** file
4. **Enable web app** - Free tier available

---

## Step-by-Step: Deploy to Render

### 1. Prepare Your Repository
```bash
cd d:\Financial-Planner
git add .
git commit -m "Deploy to Render - add Procfile and render.yaml"
git push origin main
```

### 2. Create Render Account
- Visit [render.com](https://render.com)
- Sign up with GitHub (recommended)
- Authorize Render to access your repositories

### 3. Create New Web Service
- Click "New +" → "Web Service"
- Connect your `financial-planner` repository
- Configuration:
  - **Name**: `wealth-navigator`
  - **Environment**: `Python 3`
  - **Region**: Choose closest to your users
  - **Branch**: `main`
  - **Build Command**: `pip install -r requirements.txt`
  - **Start Command**: `gunicorn run:app`

### 4. Environment Variables (Optional)
In Render dashboard → Environment:
```
FLASK_ENV=production
```

### 5. Deploy & Monitor
- Render automatically deploys on `git push`
- Monitor logs in Render dashboard
- Your URL: `https://wealth-navigator.onrender.com`

---

## Deployment Checklist

- [ ] Git repository is updated and pushed
- [ ] `requirements.txt` includes all dependencies
- [ ] `Procfile` is created
- [ ] `run.py` uses environment variables for PORT and DEBUG
- [ ] `.gitignore` excludes `venv/`, `__pycache__/`, etc.
- [ ] All static files are in correct directories
- [ ] Excel files are included in `app/excels/`
- [ ] Templates are in `templates/` directory

---

## Troubleshooting

### Issue: "ModuleNotFoundError"
**Solution**: Make sure `requirements.txt` has all dependencies
```bash
pip freeze > requirements.txt
```

### Issue: Port binding error
**Solution**: Already handled - app uses `os.environ.get("PORT", 5000)`

### Issue: Static files not loading
**Solution**: Ensure static files path is correct in templates

### Issue: Slow deployment
**Solution**: This is normal - free tier services can be slower. Upgrades available.

---

## Next Steps After Deployment

1. **Test your live app**: Visit the URL provided by your hosting service
2. **Share with users**: Send them the deployment URL
3. **Monitor performance**: Check logs regularly
4. **Gather feedback**: See how users interact with your calculators
5. **Plan upgrades**: If needed, upgrade to paid tier for better performance

---

## Useful Links

- **Render Docs**: https://render.com/docs
- **Gunicorn Docs**: https://gunicorn.org/
- **Flask Deployment**: https://flask.palletsprojects.com/deployment/
- **GitHub Integration**: https://docs.github.com/en/repositories

---

**Questions?** Check the official docs for your chosen platform!
