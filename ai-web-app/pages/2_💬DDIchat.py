import streamlit as st

# Set up the page configuration
st.set_page_config(
    page_title="DDIApp - Chat",
    page_icon="🤖",
)

# Apply overall background color and text styling
st.markdown("""
    <style>
        html, body {
            background-color: #003366; /* Midnight Blue */
            color: #000000; /* White text color */
            margin: 0;
            padding: 0;
            height: 100%;
            width: 100%;
        }

        .main {
            background-color: #B0E0E6; /* Ensure the main content area is also black */
            color: #000000; /* Ensure the text in the main content area is white */
            padding: 20px;
        }
           

        .cta-button {
            background-color: #4CAF50; /* Green */
            color: white;
            padding: 10px 20px;
            border: none;
            cursor: pointer;
            border-radius: 5px;
            font-size: 16px;
        }

        .cta-button:hover {
            background-color: #45a049; /* Darker green */
        }
        
        .card {
            border: 1px solid #ddd;
            border-radius: 5px;
            padding: 20px;
            margin: 10px;
            box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
            background-color: #1a1a1a; /* Dark gray */
        }

        .header {
            margin: 20px 0;
        }

        .header h1 {
            color: #000000;
            font-size: 3.5rem;
        }

        .header p {
            color: #000000;
            font-size: 1.2rem;
        }

        .footer {
            text-align: center;
            margin-top: 40px;
            padding: 20px;
            background-color: #003366; /* Midnight Blue */
            color: #ffffff;
        }

        .enter-symbol {
            font-size: 1.5rem;
            color: #ffffff; /* White text color */
            margin-left: 10px;
        }
    </style>
    """, unsafe_allow_html=True)

# Header Section
st.markdown("""
    <div class='header'>
        <h1>🗨️DDI Chat</h1>
       <p>Empowered by cutting-edge AI technology!</p>
<p>Our mission is to deliver the advanced and effective AI chatbot experience available.</p>
    </div>
    """, unsafe_allow_html=True)


# Define the options
options = [
    "GPT-4o Mini",
    "GPT-3.5",
    "GPT-4o (Paid account required)",
    "Claude 3.5 Sonnet (Paid account required)",
    "Claude 3 Opus (Paid account required)"
]

# Create a dropdown menu
selected_option = st.selectbox(
    "Choose an AI Model:",
    options
)

# Display the selected model with an "Enter" symbol
st.markdown(f"""
    <div style='text-align: center; margin: 20px 0;'>
        <input type="text" value="{selected_option}" style='width: 100%; padding: 10px; border-radius: 5px;' readonly />
    </div>
    """, unsafe_allow_html=True)

# Footer Section
st.markdown("""
    <div class='footer'>
            <p></p>
    </div>
    """, unsafe_allow_html=True)
