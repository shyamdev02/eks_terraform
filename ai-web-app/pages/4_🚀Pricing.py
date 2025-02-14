import streamlit as st

# Page configuration
st.set_page_config(
    page_title="DDIApp-Pricing",
    page_icon="💸",
)
st.markdown("""
    <style>
        html, body {
            /* background-color: #003366;  Midnight Blue */
           /* color: #ffffff;  White text color */
            margin: 0;
            padding: 0;
            height: 100%;
            width: 100%;
        }

        .main {
            background-color: #B0E0E6; /* Ensure the main content area is also black */
            /* color: #ffffff; Ensure the text in the main content area is white */
            padding: 20px;
        }
    
       
    </style>
    """, unsafe_allow_html=True)
# Title of the page
st.title("Pricing")

# Sale banner
st.markdown("""
    <div style="background-color: #f4a261; padding: 10px; border-radius: 5px; text-align: center;">
        <h2 style="color: white;">USE Coupon SUMM2024DDI get 20% Off🎉</h2>
        <p style="color: white;">Offer valid for Limited time only!</p>
    </div>
    """, unsafe_allow_html=True)

# Testimonials in two columns with box pattern
st.markdown("""
    <div style="margin: 20px 0;">
        <h3>What Our Users Are Saying:</h3>
        <div style="display: flex; flex-wrap: wrap; gap: 20px;">
            <div style="flex: 1; min-width: 300px;">
                <div style="border: 1px solid #ddd; border-radius: 10px; padding: 15px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); background-color: #f9f9f9; margin-bottom: 20px;">
                    <blockquote style="margin: 0;">
                        <p style="font-style: italic;">"I was skeptical about AI content until I used ApexWriter. ApexWriter created complete blog posts from just a keyword, ready for publication on my specialty sites. The content is impressively detailed and well-structured, featuring precise headings and subheadings, making it nearly ready to publish out of the box." - Emily Chen, ContentCraft</p>
                    </blockquote>
                </div>
                <div style="border: 1px solid #ddd; border-radius: 10px; padding: 15px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); background-color: #f9f9f9;">
                    <blockquote style="margin: 0;">
                       <p style="font-style: italic;">"ContentMaster is my top choice for crafting articles for our blogs. It effortlessly produces SEO-optimized, well-organized content in just one click, customized to fit my writing style. I highly endorse ContentMaster for anyone aiming to elevate their content creation." - Jake Reynolds, TechSphere</p>
                    </blockquote>
                </div>
            </div>
            <div style="flex: 1; min-width: 300px;">
                <div style="border: 1px solid #ddd; border-radius: 10px; padding: 15px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); background-color: #f9f9f9; margin-bottom: 20px;">
                    <blockquote style="margin: 0;">
                        <p style="font-style: italic;">"With the help of PinnacleWriter's powerful AI and content features, we successfully launched a new site and grew it to over 500,000 monthly visits and $20,000 in monthly revenue within just a year! We've tried various AI tools, but PinnacleWriter is now the cornerstone of our content strategy." - Alex Martin, Digital Insights</p>
                    </blockquote>
                </div>
                <div style="border: 1px solid #ddd; border-radius: 10px; padding: 15px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); background-color: #f9f9f9;">
                    <blockquote style="margin: 0;">
                        <p style="font-style: italic;">"ProWriter has quickly become my preferred AI tool for generating detailed, SEO-optimized content with ease, all tailored to my chosen writing style. While GPT models were revolutionary, ProWriter's output is in a league of its own when you compare the results." - Laura Johnson, Content Innovators</p>
                    </blockquote>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.title("Our Pricing Plans")

# Function to create a pricing card
def pricing_card(name, price, old_price, features, button_text):
    return f"""
    <div style="flex: 1; min-width: 300px; max-width: 300px; margin: 10px; border: 1px solid #ddd; border-radius: 8px; padding: 20px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); background-color: #f9f9f9;">
        <h3 style="margin-top: 0;">{name} - Save 40%</h3>
        <p style="font-size: 1.5em; font-weight: bold;"><strong>${price}</strong> <del>${old_price}</del> /month</p>
        <ul>
            {"".join([f"<li>{feature}</li>" for feature in features])}
        </ul>
        <a href="#" style="background-color: #4caf50; color: black; padding: 10px 20px; border-radius: 5px; text-decoration: none;">{button_text}</a>
    </div>
    """
# Create a container for the pricing cards
st.markdown("""
    <div style="display: flex; flex-wrap: wrap; justify-content: space-around;">
        """ +
        pricing_card(
            name="Starter",
            price="30",
            old_price="15",
            features=[
              "Unlimited content generation",
"Real-time SEO",
"Comprehensive integrations"
            ],
            button_text="Buy Plan"
        ) +
        pricing_card(
            name="Boost",
            price="50",
            old_price="25",
            features=[
               "Advanced AI tools",
"Enhanced features",
"Customizable AI image"
            ],
            button_text="Buy Plan"
        ) +
    "</div>", unsafe_allow_html=True)

