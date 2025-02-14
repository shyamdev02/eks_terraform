import streamlit as st

# Add CSS and HTML for the banner
st.markdown("""
    <style>
        /* Banner Styles */
        .banner {
            background-color: #001f3f;
            color: white;
            padding: 10px;
            text-align: center;
            position: relative;
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 20px;
        }
        .banner .close-btn {
            position: absolute;
            top: 10px;
            right: 20px;
            cursor: pointer;
            font-size: 20px;
            background: none;
            border: none;
            color: white;
        }
        .banner .close-btn:hover {
            color: #ddd;
        }
        /* Main Styles */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background: url('https://via.placeholder.com/1500') no-repeat center center fixed;
            background-size: cover;
        }
        .main {
            background-color: #B0E0E6; /* Ensure the main content area is also black */
            /* color: #ffffff; Ensure the text in the main content area is white */
            padding: 20px;
        }
        .form-container {
            background: rgba(255, 255, 255, 0.9);
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            max-width: 400px;
            margin: 100px auto;
        }
        h1 {
            text-align: center;
            margin-bottom: 20px;
        }
        .form-group {
            margin-bottom: 15px;
        }
        .form-group label {
            display: block;
            margin-bottom: 5px;
        }
        .form-group input {
            width: 100%;
            padding: 10px;
            border-radius: 5px;
            border: 1px solid #ddd;
        }
        .form-group button {
            width: 100%;
            padding: 10px;
            background-color: #4caf50;
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
        }
        .form-group button:hover {
            background-color: #45a049;
        }
        .social-buttons {
            display: flex;
            justify-content: space-between;
            margin-top: 20px;
        }
        .social-buttons button {
            width: 48%;
            padding: 10px;
            border-radius: 5px;
            border: none;
            font-size: 16px;
            cursor: pointer;
        }
        .social-buttons .google {
            background-color: #4285f4;
            color: white;
        }
        .social-buttons .email {
            background-color: #d1d1d1;
            color: #000;
        }
        .footer {
            position: absolute;
            bottom: 0;
            width: 100%;
            background-color: #333;
            color: #fff;
            text-align: center;
            padding: 10px;
        }
        .footer a {
            color: #fff;
            text-decoration: none;
            margin: 0 10px;
        }
    </style>
    <div class="banner" id="banner">
        Save 40%! Our new annual plans are now available at a special discount—act fast, this offer is only for this week! →
        <button class="close-btn" onclick="document.getElementById('banner').style.display='none';">×</button>
    </div>
""", unsafe_allow_html=True)

# Registration form
st.markdown("""
    <div class="form-container">
        <h1>Register</h1>
        <form>
            <div class="form-group">
                <label for="email">Email address</label>
                <input type="email" id="email" name="email" placeholder="Enter your email" required>
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" name="password" placeholder="Enter your password" required>
            </div>
            <div class="form-group">
                <button type="submit">Register</button>
            </div>
            <div class="social-buttons">
                <button class="google">Register with Google</button>
                <button class="email">Continue with Email</button>
            </div>
        </form>
    </div>
""", unsafe_allow_html=True)

st.write("\n")
# Footer
st.markdown("""
    <div class="footer">
        <div>
            <a href="#">Contact</a> |
            <a href="#">Support</a> |
            <a href="#">Updates</a> |
            <a href="#">Reviews</a> |
            <a href="#">Blog</a> |
            <a href="#">API</a> |
            <a href="#">Terms</a> |
            <a href="#">Privacy</a>
        </div>
        <div>
            © 2024 DDI AI. All rights reserved.
        </div>
    </div>
""", unsafe_allow_html=True)
