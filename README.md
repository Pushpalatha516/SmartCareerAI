# SmartCareer AI 🚀

**SmartCareer AI** is an AI-inspired career assistance web application that helps job seekers understand how well their resume matches a target job role.

The application analyzes resume content, identifies matched and missing skills, calculates a weighted job-readiness score, provides personalized recommendations, generates interview questions, creates learning roadmaps, and allows users to download a detailed PDF analysis report.

## ✨ Features

* 📄 **Resume Analysis**

  * Upload a PDF resume or paste resume text.
  * Extract and analyze resume content.

* 🎯 **Skill Gap Detection**

  * Identify skills already present in the resume.
  * Detect important skills missing for the selected job role.
  * Support skill aliases such as `OOP`, `Object-Oriented Programming`, and related terms.

* 📊 **Weighted Job Readiness Score**

  * Calculate a percentage-based readiness score.
  * Assign different weights to important skills depending on the selected role.
  * Display a readiness level such as:

    * Job Ready
    * Good Progress
    * Beginner
    * Needs Improvement

* 🚀 **Career Recommendations**

  * Provide recommendations for missing skills.
  * Suggest what the user should learn next.

* 📚 **Personalized Learning Roadmap**

  * Generate step-by-step learning roadmaps for missing skills.

* 🎤 **Interview Preparation**

  * Generate interview questions based on skills that need improvement.

* 📥 **Downloadable PDF Report**

  * Generate a complete resume analysis report containing:

    * Job role
    * Readiness score
    * Matched skills
    * Missing skills
    * Recommendations
    * Interview questions
    * Learning roadmap

## 🛠️ Technologies Used

* **Python**
* **Flask**
* **HTML5**
* **CSS3**
* **Jinja2**
* **ReportLab**
* **PyPDF2**
* **Git**
* **GitHub**

## 📁 Project Structure

```text
SmartCareerAI/
│
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── static/
│   └── css/
│       └── style.css
│
├── templates/
│   ├── index.html
│   ├── analyzer.html
│   └── result.html
│
└── utils/
    ├── analyzer.py
    ├── resume_parser.py
    └── report_generator.py
```

## ⚙️ How It Works

```text
User uploads resume
        ↓
Resume text is extracted
        ↓
User selects target job role
        ↓
Resume skills are analyzed
        ↓
Required skills are compared
        ↓
Matched & missing skills are identified
        ↓
Weighted readiness score is calculated
        ↓
Recommendations are generated
        ↓
Interview questions are generated
        ↓
Learning roadmap is generated
        ↓
PDF report can be downloaded
```

## 🚀 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/Pushpalatha516/SmartCareerAI.git
```

### 2. Navigate to the project

```bash
cd SmartCareerAI
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows PowerShell:**

```bash
venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
python app.py
```

The Flask development server will start locally.

Open the local URL displayed in your terminal in a web browser.

## 🎯 Supported Job Roles

The current application supports analysis for:

* Software Engineer
* Python Developer
* Data Analyst

Each role has its own required skills and weighted scoring configuration.

## 📄 Resume Analysis Example

For a selected role, SmartCareer AI provides a result containing:

```text
Job Readiness Score
        ↓
Readiness Level
        ↓
Matched Skills
        ↓
Missing Skills
        ↓
Recommended Next Steps
        ↓
Interview Preparation
        ↓
Learning Roadmap
        ↓
Downloadable PDF Report
```

## 🔐 Privacy & Git

Resume files and generated PDF files should not be committed to the repository.

The project includes a `.gitignore` file to prevent files such as:

```text
venv/
__pycache__/
*.pyc
.env
uploads/
*.pdf
```

from being uploaded to GitHub.

## 🔮 Future Improvements

Possible future enhancements include:

* 🤖 Integration with a real AI/LLM API for deeper resume analysis
* 📌 Job-description-based skill matching
* 📝 Resume improvement suggestions
* 📈 Resume ATS score analysis
* 💼 Job recommendation system
* 👤 User accounts and profiles
* 📊 Career progress dashboard
* ☁️ Cloud deployment
* 📱 Improved mobile responsiveness

## 👩‍💻 Author

**Pushpalatha Oggu**

Computer Science & Engineering Graduate

---

⭐ If you find this project useful, consider giving the repository a star!
