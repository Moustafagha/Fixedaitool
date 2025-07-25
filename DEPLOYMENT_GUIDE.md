# 🚀 MaintAI Platform - Vercel Deployment Guide

This guide provides step-by-step instructions for deploying the MaintAI Platform to Vercel.

## 📋 Prerequisites

- [Vercel Account](https://vercel.com) (free tier available)
- [GitHub Account](https://github.com) (for repository hosting)
- [PostgreSQL Database](https://www.postgresql.org/) (for production)

## 🗄️ Database Setup (Required)

### Option 1: Vercel Postgres (Recommended)
1. Go to your Vercel dashboard
2. Navigate to Storage → Create Database
3. Select "Postgres"
4. Choose your plan and create the database
5. Copy the connection string

### Option 2: External PostgreSQL Provider
Popular options:
- [Supabase](https://supabase.com) (Free tier available)
- [Railway](https://railway.app) (Free tier available)
- [ElephantSQL](https://www.elephantsql.com) (Free tier available)
- [Amazon RDS](https://aws.amazon.com/rds/)

## 🚀 Deployment Methods

### Method 1: GitHub Integration (Recommended)

#### Step 1: Prepare Your Repository
1. **Create a new GitHub repository**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: MaintAI Platform"
   git branch -M main
   git remote add origin https://github.com/yourusername/maintai-platform.git
   git push -u origin main
   ```

#### Step 2: Deploy to Vercel
1. Go to [vercel.com](https://vercel.com) and sign in
2. Click "New Project"
3. Import your GitHub repository
4. Vercel will automatically detect the Python project
5. Configure environment variables (see below)
6. Click "Deploy"

### Method 2: Vercel CLI

#### Step 1: Install Vercel CLI
```bash
npm install -g vercel
```

#### Step 2: Login and Deploy
```bash
vercel login
vercel --prod
```

## ⚙️ Environment Variables Configuration

In your Vercel project dashboard, go to Settings → Environment Variables and add:

### Required Variables
```
SECRET_KEY=your-super-secret-key-change-this-in-production
JWT_SECRET_KEY=your-jwt-secret-key-change-this-in-production
DATABASE_URL=postgresql://username:password@hostname:port/database_name
```

### Optional Variables
```
FLASK_ENV=production
FLASK_DEBUG=false
CORS_ORIGINS=https://yourdomain.vercel.app
```

### Example with Supabase
```
SECRET_KEY=maintai-super-secret-key-2024-production
JWT_SECRET_KEY=maintai-jwt-secret-key-2024-production
DATABASE_URL=postgresql://postgres:yourpassword@db.supabase.co:5432/postgres
```

## 🔧 Vercel Configuration Explained

The `vercel.json` file is already optimized:

```json
{
  "version": 2,
  "builds": [
    {
      "src": "api/index.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/api/(.*)",
      "dest": "api/index.py"
    },
    {
      "src": "/(.*)",
      "dest": "api/index.py"
    }
  ],
  "env": {
    "PYTHONPATH": "$PYTHONPATH:/var/task/src"
  }
}
```

### Key Features:
- **Serverless Functions**: Uses `@vercel/python` runtime
- **API Routes**: All `/api/*` routes go to the Flask backend
- **SPA Support**: All other routes serve the React frontend
- **Python Path**: Properly configured for imports

## 🧪 Testing Your Deployment

### 1. Health Check
Visit: `https://your-app.vercel.app/api/health`

Expected response:
```json
{
  "status": "healthy",
  "message": "MaintAI Backend is running",
  "version": "1.0.0"
}
```

### 2. Frontend Access
Visit: `https://your-app.vercel.app`

You should see the MaintAI login page.

### 3. Login Test
Use default credentials:
- Username: `admin`
- Password: `password`

## 🔒 Security Checklist

### Before Going Live:

1. **Change Default Credentials**
   - Create a new admin user
   - Delete or disable the default admin account

2. **Update Secret Keys**
   - Generate strong, unique secret keys
   - Use a password manager or key generator

3. **Database Security**
   - Use strong database passwords
   - Enable SSL connections
   - Restrict database access by IP if possible

4. **Environment Variables**
   - Never commit `.env` files to version control
   - Use Vercel's environment variable management

## 🐛 Troubleshooting

### Common Issues and Solutions

#### 1. Build Failures
**Error**: `ModuleNotFoundError`
**Solution**: Check `requirements.txt` and ensure all dependencies are listed

#### 2. Database Connection Issues
**Error**: `could not connect to server`
**Solution**: 
- Verify `DATABASE_URL` format
- Check database server status
- Ensure database allows external connections

#### 3. Static Files Not Loading
**Error**: 404 errors for CSS/JS files
**Solution**: 
- Ensure frontend is built and in `src/static/`
- Check static file routing in `src/main.py`

#### 4. CORS Errors
**Error**: `Access-Control-Allow-Origin`
**Solution**: 
- Update CORS configuration in `src/main.py`
- Add your domain to allowed origins

#### 5. Function Timeout
**Error**: Function execution timeout
**Solution**: 
- Optimize database queries
- Consider upgrading Vercel plan for longer timeouts
- Use database connection pooling

### Debug Mode

For debugging, temporarily set:
```
FLASK_DEBUG=true
```

**⚠️ Remember to disable debug mode in production!**

## 📊 Monitoring and Maintenance

### Vercel Analytics
1. Enable Vercel Analytics in your project settings
2. Monitor function execution times
3. Track error rates and performance

### Database Monitoring
1. Monitor database connection counts
2. Set up alerts for high CPU/memory usage
3. Regular database backups

### Log Monitoring
1. Check Vercel function logs regularly
2. Set up error alerting
3. Monitor API response times

## 🔄 Updates and Maintenance

### Updating the Application
1. Make changes to your code
2. Commit and push to GitHub
3. Vercel automatically redeploys

### Database Migrations
For schema changes:
1. Create migration scripts
2. Run migrations before deploying new code
3. Test thoroughly in staging environment

## 💰 Cost Optimization

### Vercel Free Tier Limits
- 100GB bandwidth per month
- 100 serverless function executions per day
- 10 second function timeout

### Optimization Tips
1. **Database Connection Pooling**: Reduce connection overhead
2. **Caching**: Implement Redis or in-memory caching
3. **Static Assets**: Use CDN for large files
4. **Function Optimization**: Minimize cold start times

## 🆘 Support Resources

### Documentation
- [Vercel Python Documentation](https://vercel.com/docs/functions/serverless-functions/runtimes/python)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)

### Community
- [Vercel Discord](https://discord.gg/vercel)
- [Flask Community](https://discord.gg/flask)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/vercel)

---

## 🎉 Congratulations!

Your MaintAI Platform should now be successfully deployed on Vercel! 

**Next Steps:**
1. Set up custom domain (optional)
2. Configure monitoring and alerts
3. Create additional user accounts
4. Customize the application for your needs

**Need Help?** Create an issue in the repository or check the troubleshooting section above.

