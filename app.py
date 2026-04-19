import os
from flask import Flask, render_template_string

app = Flask(__name__)

# --- PROFILE DATA FROM RESUME ---
PROFILE = {
    "name": "Ravella Vaishnavi",
    "role": "Azure Cloud Engineer",
    "summary": "2.5+ years of experience managing 600+ VMs and optimizing cloud infrastructure.",
    "location": "Hyderabad, India"
}

SKILLS = {
    "Cloud": "Microsoft Azure (IaaS & PaaS), ASR, Networking (VNets, NSGs)",
    "Automation": "Terraform (IaC), Azure Logic Apps, PowerShell",
    "Security": "Azure Secure Score (30+ clients improved), RBAC, Defender",
    "Containers": "Native Kubernetes and Containerization"
}

EXPERIENCE = [
    {
        "title": "Azure Engineer @ Cloud4C",
        "highlights": [
            "Managed 600+ Virtual Machines ensuring 99.9% uptime",
            "Automated monitoring using Logic Apps (Cert expiry & incident notifications)",
            "Shift Lead: Managed team operations and critical incident coordination"
        ]
    }
]

EDUCATION = [
    {"degree": "B.Tech", "school": "Vidya Jyothi Institute of Technology", "score": "8.45 CGPA"},
    {"degree": "Intermediate", "school": "Sri Chaitanya Junior College", "score": "96.10%"}
]

# --- ROUTES ---

@app.route("/")
def home():
    return f"""
    <html>
        <body bgcolor="#f4f4f9" style="font-family: sans-serif; padding: 40px;">
            <h1>Hi, I'm {PROFILE['name']} 👋</h1>
            <p><strong>{PROFILE['role']}</strong></p>
            <p>{PROFILE['summary']}</p>
            <hr>
            <nav>
                <a href="/experience">Experience</a> | 
                <a href="/skills">Technical Skills</a> | 
                <a href="/education">Education</a> |
                <a href="/health">Health Check</a>
            </nav>
        </body>
    </html>
    """

@app.route("/experience")
def experience():
    exp = EXPERIENCE[0]
    bullets = "".join([f"<li>{h}</li>" for h in exp['highlights']])
    return f"""
    <html>
        <body bgcolor="#e8f4f8" style="font-family: sans-serif; padding: 40px;">
            <h2>Professional Experience</h2>
            <h3>{exp['title']}</h3>
            <ul>{bullets}</ul>
            <a href="/">← Back</a>
        </body>
    </html>
    """

@app.route("/skills")
def show_skills():
    items = "".join([f"<li><b>{k}:</b> {v}</li>" for k, v in SKILLS.items()])
    return f"""
    <html>
        <body bgcolor="#f0fff0" style="font-family: sans-serif; padding: 40px;">
            <h2>Technical Expertise</h2>
            <ul>{items}</ul>
            <a href="/">← Back</a>
        </body>
    </html>
    """

@app.route("/education")
def show_education():
    edu_items = "".join([f"<li>{e['degree']} - {e['school']} ({e['score']})</li>" for e in EDUCATION])
    return f"""
    <html>
        <body bgcolor="#fff5e6" style="font-family: sans-serif; padding: 40px;">
            <h2>Education</h2>
            <ul>{edu_items}</ul>
            <a href="/">← Back</a>
        </body>
    </html>
    """

@app.route("/health")
def health():
    # Crucial for Kubernetes LivenessProbes
    return {"status": "Healthy", "env": os.getenv("ENV", "Development")}, 200

if __name__ == "__main__":
    # Binds to 0.0.0.0 so Minikube nodes can reach the container
    app.run(host="0.0.0.0", port=5000)
