import streamlit as st

# Page configuration
st.set_page_config(
    page_title="DDIApp-Writer",
    page_icon="👋",
)

# Custom CSS for background and text color
custom_css = """
    <style>
        body {
           background-color: #1e1e1e; /* Bluish-black background */
            color: white; /* White text */
        }
        .main {
            background-color: #B0E0E6; /* Ensure the main content area is also black */
            color: #ffffff; /* Ensure the text in the main content area is white */
            padding: 20px;
        }

        .header h1 {
            color: #000000;
            font-size: 3.5rem;
        }
        .streamlit-expanderHeader {
            color: white; /* White text for expander headers */
        }
        .stButton>button {
            color: black;  /* Button text color */
           background-color: #4b4b4b; /* Button background color */
        }
        .stTextInput>div>input {
            background-color: #2e2e2e; /* Text input background */
            color: white; /* Text input text color */
        }
        .stSelectbox>div>div>div {
            background-color: #2e2e2e;  /* Select box background */
            color: white; /* Select box text color */
        }

        .footer {
            margin-top: 10px;
            padding: 5px;
            background-color: #001f3f; /* Midnight Blue */
            color: white;
        }

        .para {
            color: #000000;
            font-size: 3rem;
        }
        .header h5 {
            color: #ffffff;
            font-size: 3rem;
        }
        .stSlider>div>div>div>div {
            color: white; /* Slider text color */
        }
         .stRadio > div > div > div {
            background-color: #2e2e2e;  /* Select box background */
            color: white; /* Radio button options text color */
        }
    </style>
"""

# Apply custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Title of the app
# Header Section
st.markdown("""
    <div class='header'>
        <h1>DDI Writer</h1>
    </div>
    """, unsafe_allow_html=True)

# Footer Section
st.markdown("""
    <div class='footer'>
       <p>Register for a free account to unlock these premium features:</p>
<p>● Seamless image generation and YouTube video embedding</p>
<p>● Up-to-date data to enhance the accuracy of your articles</p>
<p>● Automatically crafted FAQ sections derived from SERP analysis</p>
<p><strong>Sign Up Now</strong></p>
    </div>
    """, unsafe_allow_html=True)

st.write("\n")
# Main content area
st.markdown("""
    <div class='para'>
            <p>📈 Analyzes search engine data and enhances your content without relying on external tools!</p>

<p>👱🏽‍♀️ Focuses on creating content that is engaging, thorough, and trustworthy for readers</p>

<p>🔗 Automatically adds relevant internal and external links with appropriate anchor text</p>

<p>🤖 Utilizes up-to-date information to ensure your content is accurate and current</p>

<p>👉 Offers a robust Outline Editor for complete control over your article structure</p>

<p>💸 Produces affiliate content using live Amazon data, including authentic user reviews</p>
    </div>
    """, unsafe_allow_html=True)

st.write("\n")


model_choice = st.radio(
    "Choose the model for generating content:",
    ("GPT-4o Mini", "GPT-4o", "Claude 3.5 Sonnet"))





# Input fields
target_keyword = st.text_input("Target Keyword", "are german shepherds good pets?")
article_length = st.slider("Article Length (words)", min_value=500, max_value=5000, value=1000)
seo_optimization_level = st.selectbox("SEO Optimization Level", ["Default", "Manual", "AI-Powered"])
include_faq = st.checkbox("Include FAQ Section", value=True)
include_key_takeaways = st.checkbox("Include Key Takeaways", value=True)
tone_of_voice = st.selectbox("Tone of Voice", ["Confident", "Knowledgeable", "Neutral", "Clear"])
language = st.selectbox("Language", ["English (US)", "Other"])
country = st.selectbox("Country", ["United States", "Other"])
point_of_view = st.selectbox("Point of View", ["Third Person (he, she, it, they)", "First Person (I, we)"])



# Button to generate the article
if st.button("Generate Article"):
    # This is where the content generation logic would go.
    # For demonstration purposes, we will display a placeholder text.
    
    article_content = f"""
    # Article on: {target_keyword}
    
    **Introduction**
    This is a placeholder article on the topic of {target_keyword}. The length of this article is {article_length} words. 

    **Main Content**
    Here we would discuss the details related to {target_keyword}, providing valuable insights and information.

    **Conclusion**
    In conclusion, this article provides a comprehensive overview of {target_keyword}. 

    """
    
    if include_faq:
        article_content += """
        **FAQ**
        - **What is a German Shepherd?** A German Shepherd is a breed of working dog known for its intelligence and versatility.
        - **Are German Shepherds good pets?** Yes, German Shepherds are known to be loyal and protective pets.

        """
    
    if include_key_takeaways:
        article_content += """
        **Key Takeaways**
        - German Shepherds are intelligent and trainable.
        - They make excellent family pets and working dogs.

        """
    
    # Display generated article
    st.write(article_content)


