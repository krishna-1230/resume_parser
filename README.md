# Resume Parser

A web application that analyzes resumes (CVs) and ranks candidates based on required skills.

## Features

- Upload multiple resume PDFs
- Specify required skills in a comma-separated list
- Automatically score and rank candidates based on skill matches
- Clean and responsive user interface

## Project Structure

- **Frontend**: Next.js application with React
- **Backend**: Flask REST API with PDF parsing capabilities

## Setup and Installation

### Backend

1. Navigate to the backend directory:
   ```
   cd backend
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install required dependencies:
   ```
   pip install flask flask-cors PyPDF2
   ```

4. Start the Flask server:
   ```
   python main.py
   ```
   The server will run on http://127.0.0.1:5000

### Frontend

1. Navigate to the frontend application directory:
   ```
   cd frontend/my-app
   ```

2. Install dependencies:
   ```
   npm install
   ```

3. Run the development server:
   ```
   npm run dev
   ```
   The application will be available at http://localhost:3000

## Usage

1. Open the application in your web browser
2. Upload one or more PDF resumes
3. Enter required skills separated by commas (e.g., "Python, JavaScript, SQL")
4. Click "Submit" to process the resumes
5. View the ranked results

## Technologies Used

- **Frontend**: 
  - Next.js
  - React
  - TailwindCSS

- **Backend**:
  - Flask
  - PyPDF2
  - flask-cors

## License

MIT 