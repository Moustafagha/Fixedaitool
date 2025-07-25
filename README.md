# MaintAI Platform - Full Stack Application

A comprehensive maintenance management and monitoring system built with Flask (backend) and React (frontend).

## 🚀 Features

- **User Authentication & Authorization** - Secure login with JWT tokens
- **Machine Monitoring** - Real-time tracking of machine performance
- **Predictive Analytics** - AI-powered maintenance scheduling
- **Activity Management** - Track maintenance activities and repairs
- **Dashboard Analytics** - Comprehensive reporting and insights
- **Responsive Design** - Works on desktop and mobile devices

## 🛠️ Tech Stack

### Backend
- **Flask** - Python web framework
- **SQLAlchemy** - Database ORM
- **Flask-JWT-Extended** - JWT authentication
- **Flask-CORS** - Cross-origin resource sharing
- **PostgreSQL/SQLite** - Database (PostgreSQL for production, SQLite for development)

### Frontend
- **React** - Frontend framework
- **Tailwind CSS** - Styling framework
- **Shadcn/UI** - UI component library
- **Lucide React** - Icon library
- **Vite** - Build tool

## 📁 Project Structure

```
maintai-fullstack/
├── api/
│   └── index.py              # Vercel entry point
├── src/
│   ├── main.py              # Flask application
│   ├── models/              # Database models
│   │   ├── user.py
│   │   ├── machine.py
│   │   ├── activity.py
│   │   └── predictive_data.py
│   ├── routes/              # API routes
│   │   ├── auth.py
│   │   ├── user.py
│   │   ├── machines.py
│   │   ├── activities.py
│   │   └── analytics.py
│   └── static/              # Built frontend files
├── requirements.txt         # Python dependencies
├── vercel.json             # Vercel configuration
├── .env.example            # Environment variables template
└── README.md               # This file
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Node.js 16+
- Git

### Local Development

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd maintai-fullstack
   ```

2. **Set up Python environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

4. **Run the application**
   ```bash
   python src/main.py
   ```

5. **Access the application**
   - Open http://localhost:5000
   - Default credentials: `admin` / `password`

## 🌐 Deployment on Vercel

### Method 1: Using Vercel CLI

1. **Install Vercel CLI**
   ```bash
   npm install -g vercel
   ```

2. **Login to Vercel**
   ```bash
   vercel login
   ```

3. **Deploy**
   ```bash
   vercel --prod
   ```

### Method 2: Using GitHub Integration

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Connect to Vercel**
   - Go to [vercel.com](https://vercel.com)
   - Import your GitHub repository
   - Vercel will automatically detect the configuration

### Environment Variables for Production

Set these environment variables in your Vercel dashboard:

```
SECRET_KEY=your-super-secret-key-here
JWT_SECRET_KEY=your-jwt-secret-key-here
DATABASE_URL=your-postgresql-connection-string
```

## 🗄️ Database Setup

### For Development (SQLite)
The application automatically creates a SQLite database in `src/database/app.db`.

### For Production (PostgreSQL)
1. Create a PostgreSQL database
2. Set the `DATABASE_URL` environment variable:
   ```
   DATABASE_URL=postgresql://username:password@hostname:port/database_name
   ```

## 🔧 API Endpoints

### Authentication
- `POST /api/auth/login` - User login
- `POST /api/auth/register` - User registration
- `POST /api/auth/logout` - User logout

### Users
- `GET /api/users` - Get all users
- `GET /api/users/<id>` - Get user by ID
- `PUT /api/users/<id>` - Update user
- `DELETE /api/users/<id>` - Delete user

### Machines
- `GET /api/machines` - Get all machines
- `POST /api/machines` - Create new machine
- `GET /api/machines/<id>` - Get machine by ID
- `PUT /api/machines/<id>` - Update machine
- `DELETE /api/machines/<id>` - Delete machine

### Activities
- `GET /api/activities` - Get all activities
- `POST /api/activities` - Create new activity
- `GET /api/activities/<id>` - Get activity by ID
- `PUT /api/activities/<id>` - Update activity

### Analytics
- `GET /api/analytics/dashboard` - Get dashboard data
- `GET /api/analytics/reports` - Get reports

### Health Check
- `GET /api/health` - Application health status

## 🔐 Default Credentials

- **Username:** `admin`
- **Password:** `password`
- **Email:** `admin@maintai.com`
- **Role:** `admin`

**⚠️ Important:** Change the default credentials in production!

## 🛡️ Security Features

- JWT-based authentication
- Password hashing with bcrypt
- CORS protection
- Input validation
- SQL injection prevention via SQLAlchemy ORM

## 📱 Frontend Features

- Responsive design for all screen sizes
- Modern UI with Tailwind CSS and Shadcn/UI
- Real-time dashboard updates
- Interactive charts and analytics
- Mobile-friendly navigation

## 🔧 Configuration

### Vercel Configuration (`vercel.json`)
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

## 🐛 Troubleshooting

### Common Issues

1. **Import Errors**
   - Ensure all dependencies are installed: `pip install -r requirements.txt`
   - Check Python path configuration

2. **Database Connection Issues**
   - Verify DATABASE_URL format
   - Ensure database server is running
   - Check firewall settings

3. **CORS Issues**
   - Verify CORS configuration in `src/main.py`
   - Check allowed origins

4. **Static Files Not Loading**
   - Ensure frontend is built: `npm run build`
   - Check static folder path configuration

## 📝 Development Notes

### Adding New Features

1. **Backend (API)**
   - Add models in `src/models/`
   - Create routes in `src/routes/`
   - Register blueprints in `src/main.py`

2. **Frontend**
   - The frontend is pre-built and included in `src/static/`
   - To modify frontend, you'll need the original React source code

### Database Migrations

For production deployments with schema changes:
1. Use Flask-Migrate for database migrations
2. Add migration scripts to handle schema updates

## 📄 License

This project is licensed under the MIT License.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📞 Support

For support and questions:
- Create an issue in the repository
- Check the troubleshooting section
- Review the API documentation

---

**Built with ❤️ for efficient maintenance management**

