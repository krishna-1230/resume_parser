# Resume Parser

<div align="center">
  <img src="frontend/my-app/public/file.svg" alt="Resume Parser Logo" width="100" height="100">
  <h3>Automated Resume Analysis and Candidate Ranking System</h3>
</div>

## 📋 Overview

Resume Parser is a modern web application that streamlines the recruitment process by automatically analyzing resume PDFs and ranking candidates based on required skills. This tool helps recruiters and hiring managers quickly identify the most qualified candidates from a large pool of applicants.

## ✨ Features

- **Multiple Resume Upload**: Process multiple PDF resumes simultaneously
- **Skill Matching**: Specify required skills and get instant matching results
- **Automatic Ranking**: Candidates are scored and ranked based on skill matches
- **User-Friendly Interface**: Clean, responsive design built with modern web technologies
- **Real-time Processing**: Get results instantly without page reloads

## 🏗️ Architecture

The application follows a client-server architecture:

- **Frontend**: Single-page application built with Next.js and React
- **Backend**: RESTful API built with Flask that handles PDF parsing and analysis

## 🚀 Getting Started

### Prerequisites

- Python 3.8+ for the backend
- Node.js 18+ for the frontend
- npm or yarn package manager

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv

   # On Windows
   venv\Scripts\activate

   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Start the Flask server:
   ```bash
   python main.py
   ```
   The server will run on http://127.0.0.1:5000

### Frontend Setup

1. Navigate to the frontend application directory:
   ```bash
   cd frontend/my-app
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Run the development server:
   ```bash
   npm run dev
   ```
   The application will be available at http://localhost:3000

## 💻 Usage

1. Open the application in your web browser
2. Click on the file upload area or drag and drop PDF resumes
3. Enter required skills separated by commas (e.g., "Python, JavaScript, SQL")
4. Click "Submit" to process the resumes
5. View the ranked results sorted by matching score

## 🛠️ Technologies Used

### Frontend
- **Next.js**: React framework for server-rendered applications
- **React**: JavaScript library for building user interfaces
- **TailwindCSS**: Utility-first CSS framework

### Backend
- **Flask**: Lightweight WSGI web application framework
- **PyPDF2**: PDF parsing library
- **flask-cors**: Cross-Origin Resource Sharing extension for Flask

## 🔧 Development

### Project Structure
```
resume-parser/
├── backend/
│   ├── main.py             # Flask application
│   └── requirements.txt    # Python dependencies
└── frontend/
    └── my-app/             # Next.js application
        ├── src/
        │   ├── app/        # Next.js app router
        │   └── components/ # React components
        └── public/         # Static assets
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Contact

Project Link: [https://github.com/yourusername/resume-parser](https://github.com/yourusername/resume-parser) 