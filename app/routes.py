from flask import render_template
from app import app


@app.route('/components.html')
def index():
    return render_template('components.html',
                           title='Components Page - Material Kit PRO by Creative Tim')

@app.route('/sections.html')
def sections():
    return render_template('sections.html',
                           title='Sections Page - Material Kit PRO by Creative Tim')

@app.route('/')
@app.route('/index')
@app.route('/index.html')
@app.route('/presentation.html')
def presentation():
    return render_template('presentation.html',
                           title='Presentation Page - Material Kit PRO by Creative Tim')

@app.route('/template.html')
def template():
    return render_template('template.html',
                           title='Template Page - Material Kit PRO by Creative Tim')

@app.route('/tutorial-components.html')
def tutorial_components():
    return render_template('tutorial-components.html',
                           title='Tutorial Components - Material Kit PRO by Creative Tim')

"""
    Example pages
"""
@app.route('/examples/landing-page.html')
def landing_page():
    return render_template('/examples/landing-page.html',
                           title='Landing Page - Material Kit PRO by Creative Tim')

@app.route('/examples/about-us.html')
def about_us():
    return render_template('/examples/about-us.html',
                           title='About Us - Material Kit PRO by Creative Tim')

@app.route('/examples/blog-post.html')
def blog_post():
    return render_template('/examples/blog-post.html',
                           title='Blog Post Page - Material Kit PRO by Creative Tim')

@app.route('/examples/blog-posts.html')
def blog_posts():
    return render_template('/examples/blog-posts.html',
                           title='Blog Posts Page - Material Kit PRO by Creative Tim')

@app.route('/examples/contact-us.html')
def contact_us():
    return render_template('/examples/contact-us.html',
                           title='Contact Us Page - Material Kit PRO by Creative Tim')

@app.route('/examples/ecommerce.html')
def ecommerce():
    return render_template('/examples/ecommerce.html',
                           title='Ecommerce Page - Material Kit PRO by Creative Tim')

@app.route('/examples/login-page.html')
def login_page():
    return render_template('/examples/login-page.html',
                           title='Login Page - Material Kit PRO by Creative Tim')

@app.route('/examples/pricing.html')
def pricing():
    return render_template('/examples/pricing.html',
                           title='Pricing Page - Material Kit PRO by Creative Tim')

@app.route('/examples/product-page.html')
def product_page():
    return render_template('/examples/product-page.html',
                           title='Product Page - Material Kit PRO by Creative Tim')

@app.route('/examples/profile-page.html')
def profile_page():
    return render_template('/examples/profile-page.html',
                           title='Profile Page - Material Kit PRO by Creative Tim')

@app.route('/examples/signup-page.html')
def signup_page():
    return render_template('/examples/signup-page.html',
                           title='Signup Page - Material Kit PRO by Creative Tim')