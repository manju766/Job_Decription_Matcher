# Job Description Matcher

A modern AI-powered job description matcher that helps job seekers find their perfect match by analyzing resumes against job descriptions using advanced NLP techniques.

## 🚀 Features

- **AI-Powered Analysis**: Advanced skill extraction and matching algorithms
- **Multiple Format Support**: Works with DOCX, PDF, and plain text files
- **Instant Results**: Real-time analysis with detailed insights
- **Modern UI**: Beautiful, responsive interface with smooth animations
- **RESTful API**: FastAPI backend with comprehensive endpoints

## 🛠️ Tech Stack

- **Backend**: FastAPI, Python 3.11+
- **Frontend**: HTML5, CSS3, Bootstrap 5.3.2, JavaScript
- **Styling**: Custom CSS with gradient animations and modern design
- **Server**: Uvicorn ASGI server

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/job-matcher.git
   cd job-matcher
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Running the Application

1. **Start the FastAPI backend**
   ```bash
   uvicorn app.main:app --reload
   ```
   The API will be available at `http://localhost:8000`

2. **Start the frontend server**
   ```bash
   cd frontend
   python -m http.server 3000
   ```
   The web application will be available at `http://localhost:3000`

## 📁 Project Structure

```
job-matcher/
├── app/
│   ├── main.py          # FastAPI application entry point
│   ├── matcher.py       # Job matching logic
│   └── schemas.py       # Pydantic models
├── frontend/
│   └── index.html       # Main web application
├── requirements.txt     # Python dependencies
├── .gitignore          # Git ignore rules
└── README.md           # Project documentation
```

## 🔧 API Endpoints

- `GET /` - Health check endpoint
- `POST /match` - Analyze resume against job description
- `GET /docs` - Interactive API documentation (Swagger UI)

## 🎨 Features Overview

- **Enhanced Navbar**: Gradient animations with smooth hover effects
- **Contact Section**: Modern design with glass morphism and smooth transitions
- **Responsive Design**: Optimized for all device sizes
- **Accessibility**: Focus states and keyboard navigation support

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

Your Name - [your.email@example.com](mailto:your.email@example.com)

## 🙏 Acknowledgments

- Bootstrap for the responsive framework
- FastAPI for the excellent Python web framework
- Inter font family for beautiful typography