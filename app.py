from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
import os

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

# Portfolio Data
portfolio_data = {
    "name": "Tran Bao Ngoc",
    "title": "AI Engineer",
    "tagline": "Passionate about AI, Machine Learning, and Building Scalable Solutions",
    "location": "Hanoi, Vietnam",
    "email": "trbaongoc17@gmail.com",
    "github": "https://github.com/TrBn17",
    "huggingface": "https://huggingface.co/NGOC1712",
    
    "about": """I have almost 2 years of learning, research, and development in AI industry. 
    I've joined many AI projects with different domains: Healthcare, Banking, Technical Operations. 
    I'm finding an environment where I can work, learn to improve my tech skills and soft skills. 
    Besides that, I want to long term commitment and contribute to the company in this AI technical era.""",
    
    "skills": {
        "professional": [
            {"name": "Business Analysis", "level": 85},
            {"name": "Problem Solving", "level": 90},
            {"name": "Technical Writing", "level": 80},
            {"name": "Communication", "level": 85},
            {"name": "Team Collaboration", "level": 90},
            {"name": "Quick MVP Development", "level": 85}
        ],
        "technical": [
            {"name": "Python", "level": 95},
            {"name": "AI/DL & ML", "level": 90},
            {"name": "Data Processing", "level": 85},
            {"name": "FastAPI", "level": 90},
            {"name": "Deployment & DevOps", "level": 80},
            {"name": "Hugging Face", "level": 85}
        ]
    },
    
    "experience": [
        {
            "title": "AI Engineer",
            "company": "FOXAi Joint Stock Company",
            "period": "May 2024 - Present",
            "description": [
                "Developed scalable backend services using Python, FastAPI framework",
                "Collaborated closely with business analysts and product managers to translate complex requirements",
                "Developed demo services using Hugging Face, website for client and internal showcases",
                "Authored, develop technical documentation, system architecture diagrams for chatbot",
                "Worked across multiple domains, including low-resource languages (e.g., Lao) with limited training data"
            ]
        },
        {
            "title": "AI Intern",
            "company": "Wisdom Brain",
            "period": "Sep 2023 - Feb 2024",
            "description": [
                "Researched layered architectures in reinforcement learning algorithms",
                "Gained initial experience with deep learning models"
            ]
        }
    ],
    
    "projects": [
        {
            "name": "AI-Powered Chatbot System",
            "description": "Developed comprehensive chatbot using OpenAI, Deepseek, and Gemini APIs",
            "language": ["Python"],
            "technologies": ["FastAPI", "OpenAI API", "Deepseek", "Gemini", "OpenAI", "Langchain"],
            "role": "Core Developer",
            "highlights": ["Multi-model integration", "Scalable architecture", "Real-time responses", "Streaming support"]
        },
        {
            "name": "eKYC Identity Verification",
            "language": ["Python", "JavaScript", "HTML", "CSS"],
            "description": "Built electronic Know Your Customer system for ID cards and passports verification",
            "technologies": ["Computer Vision", "OCR", "Deep Learning", "Python"],
            "role": "Core Developer",
            "highlights": ["High accuracy OCR", "Real-time processing", "Security compliance"]
        },
        {
            "name": "Document processing System",
            "description": "Developed RAG system for various document types",
            "language": ["Python"],
            "technologies": ["Qdrant", "Docling", "FastAPI"],
            "role": "Core Developer",
            "highlights": ["Multi-language support", "High accuracy", "Fast processing"]
        },
        {
            "name": "Banking ML Solution",
            "description": "Applied machine learning algorithms for banking domain challenges",
            "language": ["Python"],
            "technologies": ["Scikit-learn", "Pandas", "NumPy"],
            "role": "Technical Support",
            "highlights": ["Risk assessment", "Fraud detection", "Customer segmentation"]
        }
    ],
    
    "education": {
        "degree": "Bachelor of Business Data Analytics",
        "school": "International School - VNU",
        "coursework": ["Business Analysis", "Data Analysis", "Machine Learning", "Deep Learning"]
    },
    
    "certifications": [
        "AI Ethics Certificate",
        "Google Data Analytics Professional Certificate",
        "B2 VSTEP Certificate"
    ]
}

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "data": portfolio_data})

@app.get('/api/data')
async def get_data():
    return portfolio_data

if __name__ == '__main__':
    print("🚀 Portfolio website is starting...")
    print("🌐 Visit http://localhost:8000 to view your portfolio")
    print("📖 API documentation available at http://localhost:8000/docs")
    
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)