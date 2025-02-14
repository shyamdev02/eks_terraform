import streamlit as st

st.set_page_config(
    page_title="DDIApp-Login",
    page_icon="👋",
)


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
            background-color: #B0E0E6; /* Light Blue Background */
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
            flex-direction: column;
            margin-top: 20px;
        }
        .social-buttons button {
            width: 100%;
            padding: 10px;
            border-radius: 5px;
            border: none;
            font-size: 16px;
            cursor: pointer;
            margin-bottom: 10px;
        }
        .social-buttons .google {
            background-color: #4285f4;
            color: white;
        }
        .social-buttons .email {
            background-color: #d1d1d1;
            color: #000;
        }
        .forgot-password {
            text-align: center;
            margin-top: 10px;
        }
        .forgot-password a {
            color: #4caf50;
            text-decoration: none;
        }
        .forgot-password a:hover {
            text-decoration: underline;
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
        .line-with-text {
            position: relative;
            text-align: center;
            margin: 20px 0;
        }
        .line-with-text hr {
            border: 1px solid #000000;
            margin: 0;
            height: 1px;
        }
        .line-with-text span {
            position: absolute;
            top: -0.7em; /* Adjust this value based on the font size and line height */
            left: 50%;
            transform: translateX(-50%);
            background: #ffffff; /* Match the background color with the page background */
            padding: 0 10px;
        }
    </style>
    <div class="banner" id="banner">
        Save 40%! We just launched brand new annual plans, grab them at a discount this week only! →
        <button class="close-btn" onclick="document.getElementById('banner').style.display='none';">×</button>
    </div>
""", unsafe_allow_html=True)

# Login form
st.markdown("""
    <div class="form-container">
        <h1>Login</h1>
        <div class="social-buttons">
            <button class="google">Login with Google</button>
        </div>
        <div class="line-with-text">
        <hr>
        <span>Or Continue with</span>
        </div>
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
                <button type="submit">Login</button>
            </div>
            <div class="forgot-password">
                <a href="#">Forgot your password?</a>
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
