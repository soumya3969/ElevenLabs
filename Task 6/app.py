"""
Portfolio Website with Flask
A modern, responsive personal portfolio website with advanced UI
"""

from flask import Flask, render_template, request, flash, redirect, url_for
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'gfhjk-asdfv-sdf')

# Portfolio data
PROJECTS = [
    {
        'id': 1,
        'title': 'Calculator CLI App',
        'description': 'A command-line calculator supporting basic arithmetic operations with error handling.',
        'technologies': ['Python', 'CLI'],
        'github': 'https://github.com',
        'category': 'Python'
    },
    {
        'id': 2,
        'title': 'To-Do List Manager',
        'description': 'Console-based task management system with persistent storage and full CRUD operations.',
        'technologies': ['Python', 'File I/O'],
        'github': 'https://github.com',
        'category': 'Python'
    },
    {
        'id': 3,
        'title': 'News Headlines Scraper',
        'description': 'Web scraper collecting top headlines from multiple news sources using BeautifulSoup.',
        'technologies': ['Python', 'BeautifulSoup', 'Requests'],
        'github': 'https://github.com',
        'category': 'Data'
    },
    {
        'id': 4,
        'title': 'User Management REST API',
        'description': 'RESTful API with complete CRUD operations, validation, and comprehensive error handling.',
        'technologies': ['Python', 'Flask', 'REST API'],
        'github': 'https://github.com',
        'category': 'Web'
    },
    {
        'id': 5,
        'title': 'Sales Data Analysis',
        'description': 'Comprehensive data analysis with Pandas featuring interactive visualizations and insights.',
        'technologies': ['Python', 'Pandas', 'Matplotlib', 'Seaborn'],
        'github': 'https://github.com',
        'category': 'Data'
    },
    {
        'id': 6,
        'title': 'Portfolio Website',
        'description': 'Modern, responsive portfolio website with advanced UI/UX and smooth animations.',
        'technologies': ['Python', 'Flask', 'HTML', 'CSS', 'JavaScript'],
        'github': 'https://github.com',
        'category': 'Web'
    }
]

SKILLS = {
    'Languages': ['Python', 'JavaScript', 'HTML5', 'CSS3', 'SQL'],
    'Frameworks': ['Flask', 'Pandas', 'NumPy', 'Matplotlib', 'Seaborn', 'Django', 'React', 'Node.js', 'Express.js'],
    'Tools': ['Git', 'VS Code', 'Jupyter', 'Postman', 'Docker'],
    'Concepts': ['REST API', 'Data Analysis', 'Web Scraping', 'OOP', 'Responsive Design']
}

EXPERIENCE = [
    {
        'role': 'Python Developer Intern',
        'period': '2024 - Present',
        'description': 'Building web applications, REST APIs, and data analysis solutions.'
    },
    {
        'role': 'Full Stack Developer Training',
        'period': '2023 - 2024',
        'description': 'Developed responsive web applications with Flask, Django and modern frontend technologies.'
    }
]

@app.route('/')
def index():
    """Homepage with hero section"""
    return render_template('index.html', 
                         current_year=datetime.now().year,
                         page='home')

@app.route('/about')
def about():
    """About page with skills and experience"""
    return render_template('about.html', 
                         skills=SKILLS,
                         experience=EXPERIENCE,
                         current_year=datetime.now().year,
                         page='about')

@app.route('/projects')
def projects():
    """Projects showcase page"""
    # Get filter parameter
    category_filter = request.args.get('category', 'all')
    
    # Filter projects if needed
    if category_filter == 'all':
        filtered_projects = PROJECTS
    else:
        filtered_projects = [p for p in PROJECTS if p['category'] == category_filter]
    
    # Get unique categories
    categories = list(set(p['category'] for p in PROJECTS))
    
    return render_template('projects.html', 
                         projects=filtered_projects,
                         categories=categories,
                         current_filter=category_filter,
                         current_year=datetime.now().year,
                         page='projects')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact page with form"""
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        subject = request.form.get('subject', '').strip()
        message = request.form.get('message', '').strip()
        
        # Validate form data
        errors = []
        if not name:
            errors.append('Name is required')
        if not email or '@' not in email:
            errors.append('Valid email is required')
        if not subject:
            errors.append('Subject is required')
        if not message:
            errors.append('Message is required')
        
        if errors:
            for error in errors:
                flash(error, 'error')
        else:
            # In production, you would send email or save to database here
            flash(f'Thank you, {name}! Your message has been received. I will get back to you soon.', 'success')
            return redirect(url_for('contact'))
    
    return render_template('contact.html', 
                         current_year=datetime.now().year,
                         page='contact')

@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors"""
    return render_template('404.html', 
                         current_year=datetime.now().year), 404

@app.errorhandler(500)
def internal_server_error(e):
    """Handle 500 errors"""
    return render_template('500.html', 
                         current_year=datetime.now().year), 500

# Template filters
@app.template_filter('year')
def current_year_filter(s):
    """Get current year"""
    return datetime.now().year

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🚀 Portfolio Website Server")
    print("="*60)
    print("📍 Running on: http://127.0.0.1:5000")
    print("🌐 Open in browser to view your portfolio")
    print("="*60 + "\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
