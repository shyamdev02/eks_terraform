import streamlit as st

# Set up the page configuration
st.set_page_config(
    page_title="DDIApp - Home",
    page_icon="👋",
)

# Custom CSS for blue-black theme with white text
st.markdown("""
    <style>
        body {
            background-color: #000033; /* Blue-black background color */
            color: #ffffff; /* White text color */
            font-family: 'Arial', sans-serif;
        }
        
        .main {
            background-color: #B0E0E6; /* Ensure the main content area is also black */
            color: #ffffff; /* Ensure the text in the main content area is white */
            padding: 20px;
        }
            
        .header, .features, .testimonials, .footer {
            background-color: #001f3f; /* Slightly lighter blue-black for sections */
            padding: 30px;
            border-radius: 8px;
            margin: 20px auto;
            max-width: 1200px;
        }
        .header h1, .header p, .features h2, .features p, .testimonials h2, .footer h3 {
            color: #ffffff;
        }
        .cta-button {
            background-color: #001f3f;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            text-decoration: none;
            margin-top: 10px;
        }
        .cta-button:hover {
            background-color: #ffffff;
            color: #001f3f;
        }
        .testimonial-box, .feature-box {
            border: 1px solid #003366; /* Darker border to match theme */
            border-radius: 5px;
            padding: 15px;
            margin: 10px;
            box-shadow: 0px 0px 10px rgba(0,0,0,0.3);
            background-color: #00264d; /* Even darker blue-black for boxes */
        }
        .testimonial-box h4, .feature-box h4 {
            color: #00bfff; /* Light blue for headings */
        }
        .testimonial-box p, .feature-box p {
            color: #ffffff; /* White text color */
        }
        .footer a {
            color: #ffffff; /* Light blue for links */
            text-decoration: none;
            margin: 0 10px;
            align: center;
        }
        .footer a:hover {
            text-decoration: underline;
        }
    </style>
    """, unsafe_allow_html=True)

# Header Section
st.markdown("""
    <div style='text-align: center;'>
    <div class='header'>
        <h1>Transform Your Content Creation with DDI AI</h1>
        <p>Produce top-notch, SEO-friendly articles in just minutes. DDI Writer harnesses the power of GPT-4 and real-time SERP insights to craft content that excels in search rankings.</p>
    </div>
    </div>
    """, unsafe_allow_html=True)

# Call to Action
st.markdown("""
    <div style='text-align: center;'>
        <h2>Try DDI Writer for Free</h2>
        <a href='#' class='cta-button'>Try DDI Writer for Free</a>
    </div>
    """, unsafe_allow_html=True)

# Testimonials Section
st.markdown("""
    <div style='text-align: center;'>
    <div class='testimonials'>
        <h2>What Our Users Are Saying</h2>
    </div>
    </div>
    """, unsafe_allow_html=True)

# Define testimonials with new names and reviews
testimonials = [
    {
        "name": "Afna Aziz",
        "review": "DDI has revolutionized our content production. The AI's ability to generate detailed and SEO-optimized articles is unmatched.",
        "rating": "★★★★★"
    },
    {
        "name": "Dinesh Ekam",
        "review": "Exceptional tool for anyone serious about content creation. DDI not only generates content but ensures it's SEO-friendly and engaging.",
        "rating": "★★★★★"
    },
    {
        "name": "Janardhan M",
        "review": "The most powerful AI writing tool I've used. It's perfect for producing high-quality, structured content that requires minimal editing.",
        "rating": "★★★★★"
    }
]

# Create 3-column layout for testimonials
num_cols = 3
cols = st.columns(num_cols)

# Distribute testimonials among columns
for i, testimonial in enumerate(testimonials):
    col_idx = i % num_cols
    with cols[col_idx]:
        st.markdown(f"""
            <div class='testimonial-box'>
                <h4>{testimonial['name']}{' (' + testimonial.get('company', '') + ')' if testimonial.get('company') else ''}</h4>
                <p>{testimonial['review']}</p>
                <p>Rating: {testimonial['rating']}</p>
            </div>
            """, unsafe_allow_html=True)

# Features Section
st.markdown("""
    <div style='text-align: center;'>
    <div class='features'>
        <h2>Crafted for Peak Performance</h2>
        <p>Our features are designed to streamline your content creation process and deliver outstanding results quickly and efficiently. Explore some of our standout features below.</p>
    </div>
    </div>
    """, unsafe_allow_html=True)

# Define features with updated descriptions
features = [
    {
        "title": "Advanced SEO Insights",
        "description": "Leverage deep SERP analysis to craft content with optimal keyword placement and structural elements that enhance search engine visibility."
    },
    {
        "title": "Effortless Affiliate Content",
        "description": "Quickly generate engaging Amazon affiliate content with real-time data and review integration for maximum impact and relevance."
    },
    {
        "title": "Broad Platform Compatibility",
        "description": "Seamlessly publish your content across major platforms including WordPress and Shopify, and use webhooks for advanced custom workflows."
    },
    {
        "title": "All-in-One Content Hub",
        "description": "Access DDI Writer, Chat, Images, and Magnets with a single subscription, providing a comprehensive solution for all your content needs."
    },
    {
        "title": "SEO-Focused Chat Features",
        "description": "Interact with DDI Chat for tailored SEO advice and commands that support effective content creation and optimization."
    },
    {
        "title": "Precision Content Creation",
        "description": "Utilize DDI AI’s sophisticated algorithms to produce well-structured, ready-to-publish articles with top-tier SEO and content integration."
    },
    {
        "title": "Adaptable Writing Tones",
        "description": "Customize writing styles and tones to align with your brand’s identity, ensuring a consistent and personalized voice in your content."
    },
    {
        "title": "Real-Time Data Enhancement",
        "description": "Incorporate the latest data from the web into your articles, boosting accuracy and relevance with current information."
    },
    {
        "title": "Dynamic Outline Control",
        "description": "Take full control of your content’s organization by managing headings and subheadings before finalizing the article."
    },
    {
        "title": "Google Sheets Integration",
        "description": "Streamline your workflow with Google Sheets integration, enabling seamless connections with other applications via custom integrations."
    },
    {
        "title": "Comprehensive API Access",
        "description": "Harness the power of DDI AI’s API for advanced content creation needs, allowing for efficient article generation with a single API call."
    },
    {
        "title": "Risk-Free Satisfaction Guarantee",
        "description": "Try our service risk-free with our 15-day satisfaction guarantee. If you’re not completely satisfied, contact us for a full refund within the trial period."
    }
]

# Create 3-column layout for features
num_cols = 3
cols = st.columns(num_cols)

# Distribute features among columns
for i, feature in enumerate(features):
    col_idx = i % num_cols
    with cols[col_idx]:
        st.markdown(f"""
            <div class='feature-box'>
                <h4>{feature['title']}</h4>
            </div>
            """, unsafe_allow_html=True)

# Footer Section
st.markdown("""
    <div style='text-align: center;'>
    <div class='footer'>
        <h3>Get Started Today!</h3>
        <p><strong>Experience DDI Writer for Free</strong></p>
        <a href='#' class='cta-button'>Start Free Trial</a>
        <br><br>
        <a href='#'>Explore Pricing →</a>
        <br><br>
        <div>
            <a href='#'>Contact Us</a> |
            <a href='#'>New Features</a> |
            <a href='#'>User Reviews</a> |
            <a href='#'>Terms of Service</a> |
            <a href='#'>Privacy Policy</a>
        </div>
        <br>
        <p>© 2024 DDI AI. All rights reserved.</p>
    </div>
    </div>
    """, unsafe_allow_html=True)