from dotenv import load_dotenv
import os
import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from ChromaVectorDB import df
from chains import Chain
from ChromaVectorDB import Portfolio
from utils import clean_text

# Load the environment variables from the .env file
load_dotenv()

# Check if USER_AGENT is set
user_agent = os.getenv('USER_AGENT')
if user_agent:
    print(f"USER_AGENT is set to: {user_agent}")
else:
    print("USER_AGENT is not set.")

# Set the page config at the top
st.set_page_config(layout="wide", page_title="Outreach email Agent", page_icon="📬")

# Define a function to create the Streamlit app
def create_streamlit_app(llm, portfolio, clean_text):
    # CSS styling for dark theme, larger logo, 3D button, and marquee text
    st.markdown(
        """
        <style>
        body {
            background-color: #181818;
            color: #f1f1f1;
        }
        .logo {
            position: relative;
            top: -60px; /* Move the logo up */
            left: 20px; /* Adjust horizontal position */
        }
        .logo img {
            width: 240px; /* Increased size */
        }
        .main {
            background-color: #282828;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 2px 2px 15px rgba(0,0,0,0.5);
        }
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #FF4B4B;
            color: white;
            text-align: center;
            padding: 10px;
            font-size: 0.9em;
        }
        .marquee {
            position: fixed;
            bottom: 40px; /* Adjust the position above the footer */
            width: 100%; /* Ensure it spans the entire page width */
            left: 0; /* Ensure it starts from the left edge */
            background-color: #ffdd00;
            color: black;
            padding: 5px;
            font-size: 1em;
            font-weight: bold;
            z-index: 9999;
        }
        .marquee-text {
            display: inline-block;
            white-space: nowrap;
            overflow: hidden;
            animation: marquee 10s linear infinite;
        }
        @keyframes marquee {
            0% { transform: translateX(100%); }
            100% { transform: translateX(-100%); }
        }
        .reportview-container {
            font-family: 'Arial', sans-serif;
        }
        pre {
            font-size: 1.1em;
            padding: 15px;
            background-color: #333;
            border-radius: 10px;
            color: #f1f1f1;
            box-shadow: 0 4px 10px rgba(0,0,0,0.5);
        }
        .stButton > button {
            background-color: #FF4B4B;
            color: white;
            border-radius: 10px;
            box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.2);
            transition: all 0.3s ease;
            padding: 10px 20px;
        }
        .stButton > button:hover {
            background-color: #ff7f7f;
            box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.4);
            transform: translateY(-3px);
        }
        h1, h2, h3, h4, h5, h6 {
            color: #f1f1f1;
        }
        a {
            color: #f1f1f1;
        }
        </style>
        """, unsafe_allow_html=True
    )

    # Display the clickable logo using HTML
    logo_url = "https://blogger.googleusercontent.com/img/a/AVvXsEhnHytqetRrBrTA2gpVKmQlvsykyi9PBxYBDg32XOwFsLgebMXbWHXdVXNUAZyntGWG8oBRzUtVGdwBL9WXodkcWHV5v9q3aLFRJeIcZZIZpulojy4_WBezbzZanfp0l0P4YJVtWVZ43xfEtgfTeseu5ZufcfHn_fm1dqZWrdLJXxk0T_QCvSfGA8RK=s450"
    st.markdown(
        f"""
        <div class="logo">
            <a href="https://www.swavimankumar.com" target="_blank">
                <img src="{logo_url}" alt="Logo">
            </a>
        </div>
        """, unsafe_allow_html=True
    )

    # Page Title
    st.title("📬 Outreach Email Agent")

    # Subheader
    st.subheader("Generate personalized outreach emails based on job descriptions")

    # Input URL and button in the sidebar
    with st.sidebar:
        url_input = st.text_input("Enter a URL:", value="https://careers.acer.com/job/New-Taipei-City-%E3%80%90BD%E3%80%91Business-Intelligence-Manager-New-Taipei/943591610/")
        submit_button = st.button("Submit")

    # Display results when the button is clicked
    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            portfolio.load_portfolio()
            jobs = llm.extract_jobs(data)
            for job in jobs:
                skills = job.get('skills', [])
                links = portfolio.query_links(skills)
                email = llm.write_mail(job, links)

                # Display result within a styled block
                st.markdown(f"""
                    <div class="main">
                    <h3>{job['role']}</h3>
                    <pre>{email}</pre>
                    </div>
                """, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"An Error Occurred: {e}")

    # Footer with clickable link
    st.markdown("""
        <div class="footer">
            Built with ❤️ by <a href="https://www.swavimankumar.com" target="_blank" style="color: white; text-decoration: none;">Quantum Leap</a>
        </div>
    """, unsafe_allow_html=True)

    # Scrolling marquee text with copyright symbol and mention
    st.markdown("""
        <div class="marquee">
            <div class="marquee-text">© SwavimanKumar | This is a GenAI tool built for educational purposes. Any unauthorized use without proper consent is a violation of policy.</div>
        </div>
    """, unsafe_allow_html=True)


# Main execution
if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio(df)
    create_streamlit_app(chain, portfolio, clean_text)
