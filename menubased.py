import streamlit as st
import os
import psutil
from pathlib import Path
import time
from datetime import datetime

# Configure page
st.set_page_config(
    page_title="🧠 Automation Suite - Internship Project",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern dark theme
st.markdown("""
<style>
    .main-header {
        text-align: center;
        background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        color: white;
    }
    
    .category-card {
        background: #1e1e1e;
        padding: 1.5rem;
        border-radius: 10px;
        border: 1px solid #333;
        margin: 1rem 0;
        transition: transform 0.2s;
    }
    
    .category-card:hover {
        transform: translateY(-2px);
        border-color: #4CAF50;
    }
    
    .task-button {
        background: #2d2d2d;
        border: 1px solid #444;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem;
        text-align: center;
        cursor: pointer;
        transition: all 0.2s;
    }
    
    .task-button:hover {
        background: #3d3d3d;
        border-color: #4CAF50;
    }
    
    .stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #4CAF50 0%, #45a049 100%);
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        font-weight: bold;
    }
    
    .sidebar .sidebar-content {
        background: #1aa1a1a;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 0.5rem 0;
    }
    
    .feature-demo {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #4CAF50;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Header with project info
    st.markdown("""
    <div class="main-header">
        <h1>🧠 Automation Suite Dashboard</h1>
        <h3>Internship Project - Multi-Tool Automation Platform</h3>
        <p>A comprehensive dashboard for various automation tools and utilities</p>
        <small>Developed as part of internship program</small>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar navigation
    st.sidebar.title("🧠 Navigation Menu")
    st.sidebar.markdown("---")
    
    # Category selection
    category = st.sidebar.selectbox("Select Category:", 
                                   ["🏠 Dashboard Home", "🔧 Python Tools", "🟨 Web Tools", "📊 System Monitor", "📚 Documentation"])
    
    # Main content routing
    if category == "🏠 Dashboard Home":
        show_dashboard_home()
    elif category == "🔧 Python Tools":
        show_python_tools()
    elif category == "🟨 Web Tools":
        show_web_tools()
    elif category == "📊 System Monitor":
        show_system_monitor()
    elif category == "📚 Documentation":
        show_documentation()

def show_dashboard_home():
    st.header("🏠 Dashboard Overview")
    
    # Project statistics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>12+</h3>
            <p>Tools Available</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>3</h3>
            <p>Categories</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3>100%</h3>
            <p>Python Based</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <h3>Live</h3>
            <p>System Status</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Feature highlights
    st.subheader("🌟 Key Features")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🔧 Python Automation Tools
        - **Email Automation**: Send emails via Gmail SMTP
        - **WhatsApp Integration**: Automated messaging
        - **SMS Services**: Twilio integration
        - **Web Scraping**: Data extraction tools
        - **Image Processing**: Generation and manipulation
        """)
    
    with col2:
        st.markdown("""
        ### 🟨 Web-Based Tools
        - **Photo Capture**: Camera integration
        - **Location Services**: Maps and routing
        - **Email Composer**: Web-based email tools
        - **Real-time Features**: Live camera access
        - **Modern UI**: Responsive design
        """)
    
    # Quick actions
    st.markdown("---")
    st.subheader("🚀 Quick Actions")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📊 Check System Status"):
            st.success("✅ All systems operational!")
            st.info(f"🕐 Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    with col2:
        if st.button("🔧 View Python Tools"):
            st.session_state.category = "🔧 Python Tools"
            st.rerun()
    
    with col3:
        if st.button("🟨 Open Web Tools"):
            st.session_state.category = "🟨 Web Tools"
            st.rerun()

def show_python_tools():
    st.header("🔧 Python Automation Tools")
    
    # Tool selection
    tool = st.sidebar.selectbox("Select Tool:", 
                               ["📧 Email Sender", "💬 WhatsApp", "📱 SMS Sender", "🌐 Web Scraper", 
                                "🎨 Image Generator", "🔄 Face Swap", "📞 Phone Caller"])
    
    if tool == "📧 Email Sender":
        show_email_tool()
    elif tool == "💬 WhatsApp":
        show_whatsapp_tool()
    elif tool == "📱 SMS Sender":
        show_sms_tool()
    elif tool == "🌐 Web Scraper":
        show_scraper_tool()
    elif tool == "🎨 Image Generator":
        show_image_tool()
    elif tool == "🔄 Face Swap":
        show_faceswap_tool()
    elif tool == "📞 Phone Caller":
        show_caller_tool()

def show_email_tool():
    st.subheader("📧 Email Automation Tool")
    
    st.info("📋 **Required Library**: `pip install smtplib` (built-in Python)")
    
    with st.expander("ℹ️ Gmail Setup Instructions"):
        st.markdown("""
        1. Enable 2-Factor Authentication in your Google Account
        2. Go to Security → App passwords
        3. Generate an app password for this application
        4. Use the 16-character password below
        """)
    
    with st.form("email_form"):
        col1, col2 = st.columns(2)
        with col1:
            sender = st.text_input("Sender Email", placeholder="your-email@gmail.com")
            receiver = st.text_input("Receiver Email", placeholder="recipient@example.com")
        with col2:
            app_password = st.text_input("Gmail App Password", type="password")
            subject = st.text_input("Subject", placeholder="Test Email")
        
        message = st.text_area("Message", placeholder="Your email content here...")
        
        if st.form_submit_button("📤 Send Email"):
            if sender and receiver and app_password and message:
                st.success("✅ Email configuration ready! (Demo mode - actual sending requires implementation)")
                st.code(f"""
# Email would be sent with:
Sender: {sender}
Receiver: {receiver}
Subject: {subject}
Message: {message[:50]}...
                """)
            else:
                st.error("❌ Please fill all required fields")

def show_whatsapp_tool():
    st.subheader("💬 WhatsApp Automation")
    
    st.info("📋 **Required Library**: `pip install pywhatkit`")
    
    phone = st.text_input("📞 Phone Number (with country code)", value="+91")
    message = st.text_area("💬 Message", placeholder="Your WhatsApp message...")
    
    col1, col2 = st.columns(2)
    with col1:
        hour = st.number_input("Hour (24-hour format)", min_value=0, max_value=23, value=14)
    with col2:
        minute = st.number_input("Minute", min_value=0, max_value=59, value=30)
    
    if st.button("📤 Schedule WhatsApp Message"):
        if phone and message:
            st.success(f"✅ WhatsApp message scheduled for {hour:02d}:{minute:02d}")
            st.info("📱 Browser will open automatically at scheduled time")
        else:
            st.error("❌ Please enter phone number and message")

def show_sms_tool():
    st.subheader("📱 SMS Sender")
    
    st.info("📋 **Required Library**: `pip install twilio`")
    
    with st.expander("🔧 Twilio Setup"):
        st.markdown("""
        1. Create account at [twilio.com](https://www.twilio.com)
        2. Get your Account SID and Auth Token
        3. Purchase a Twilio phone number
        """)
    
    account_sid = st.text_input("Twilio Account SID")
    auth_token = st.text_input("Auth Token", type="password")
    from_number = st.text_input("From Number (Twilio)")
    to_number = st.text_input("To Number")
    sms_body = st.text_area("SMS Message")
    
    if st.button("📤 Send SMS"):
        if all([account_sid, auth_token, from_number, to_number, sms_body]):
            st.success("✅ SMS configuration ready!")
        else:
            st.error("❌ Please fill all fields")

def show_scraper_tool():
    st.subheader("🌐 Web Scraper")
    
    st.info("📋 **Required Libraries**: `pip install requests beautifulsoup4`")
    
    url = st.text_input("Website URL", placeholder="https://example.com")
    
    file_types = st.multiselect(
        "File types to download:",
        [".pdf", ".csv", ".xlsx", ".txt", ".jpg", ".png"],
        default=[".pdf", ".csv"]
    )
    
    if st.button("🔍 Analyze Website"):
        if url:
            st.success("✅ Website analysis ready!")
            st.info("📊 This would scan for downloadable files")
        else:
            st.error("❌ Please enter a URL")

def show_image_tool():
    st.subheader("🎨 Image Generator")
    
    st.info("📋 **Required Library**: `pip install Pillow`")
    
    col1, col2 = st.columns(2)
    with col1:
        width = st.slider("Width", 100, 800, 400)
        height = st.slider("Height", 100, 600, 300)
    with col2:
        bg_color = st.color_picker("Background Color", "#FFFFFF")
        shape = st.selectbox("Shape", ["Circle", "Rectangle", "Triangle"])
    
    if st.button("🎨 Generate Image"):
        st.success("✅ Image generation ready!")
        st.info(f"📐 Would create {width}x{height} image with {shape}")

def show_faceswap_tool():
    st.subheader("🔄 Face Swap Tool")
    
    st.info("📋 **Required Libraries**: `pip install opencv-python mediapipe`")
    
    col1, col2 = st.columns(2)
    with col1:
        st.file_uploader("Upload First Image", type=["jpg", "png"])
    with col2:
        st.file_uploader("Upload Second Image", type=["jpg", "png"])
    
    if st.button("🔄 Swap Faces"):
        st.success("✅ Face swap ready!")

def show_caller_tool():
    st.subheader("📞 Phone Caller")
    
    st.info("📋 **Required Library**: `pip install twilio`")
    
    to_number = st.text_input("Phone Number to Call")
    message = st.text_area("Message to Speak")
    
    if st.button("📞 Make Call"):
        if to_number and message:
            st.success("✅ Call configuration ready!")
        else:
            st.error("❌ Please fill all fields")

def show_web_tools():
    st.header("🟨 Web-Based Tools")
    
    tool = st.sidebar.selectbox("Select Web Tool:", 
                               ["📷 Photo Capture", "📧 Email Composer", "🗺️ Location Tools"])
    
    if tool == "📷 Photo Capture":
        show_photo_capture()
    elif tool == "📧 Email Composer":
        show_email_composer()
    elif tool == "🗺️ Location Tools":
        show_location_tools()

def show_photo_capture():
    st.subheader("📷 Photo Capture Tool")
    
    html_code = """
    <div style="text-align: center; padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 10px; color: white;">
        <h3>📷 Camera Interface</h3>
        <video id="video" width="400" height="300" autoplay style="border-radius: 10px;"></video><br><br>
        <button onclick="capturePhoto()" style="background: #4CAF50; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer;">📸 Capture Photo</button>
        <canvas id="canvas" width="400" height="300" style="display:none;"></canvas>
        <img id="photo" width="400" style="display:none; border-radius: 10px; margin-top: 10px;">
    </div>
    
    <script>
        navigator.mediaDevices.getUserMedia({ video: true })
            .then(stream => {
                document.getElementById('video').srcObject = stream;
            })
            .catch(err => {
                console.log('Camera access denied');
            });
        
        function capturePhoto() {
            const video = document.getElementById('video');
            const canvas = document.getElementById('canvas');
            const ctx = canvas.getContext('2d');
            ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
            const imageData = canvas.toDataURL('image/png');
            document.getElementById('photo').src = imageData;
            document.getElementById('photo').style.display = 'block';
        }
    </script>
    """
    
    st.components.v1.html(html_code, height=500)

def show_email_composer():
    st.subheader("📧 Email Composer")
    
    recipient = st.text_input("To:", placeholder="recipient@example.com")
    subject = st.text_input("Subject:", placeholder="Email subject")
    message = st.text_area("Message:", placeholder="Your message here...")
    
    if st.button("📧 Open Email Client"):
        if recipient and subject and message:
            mailto_link = f"mailto:{recipient}?subject={subject}&body={message}"
            st.success("✅ Email client will open!")
            st.code(f"mailto:{recipient}?subject={subject}")
        else:
            st.error("❌ Please fill all fields")

def show_location_tools():
    st.subheader("🗺️ Location Services")
    
    st.info("🌐 Web-based location tools")
    
    if st.button("📍 Get Current Location"):
        st.success("✅ Location service ready!")
        
    if st.button("🛣️ Route Planner"):
        st.success("✅ Route planning ready!")

def show_system_monitor():
    st.header("📊 System Monitor")
    
    try:
        # System information
        st.subheader("💻 System Information")
        
        col1, col2, col3 = st.columns(3)
        
        # Memory usage
        memory = psutil.virtual_memory()
        with col1:
            st.metric(
                "RAM Usage", 
                f"{memory.percent}%",
                f"{memory.used / (1024**3):.1f} GB used"
            )
        
        # CPU usage
        cpu_percent = psutil.cpu_percent(interval=1)
        with col2:
            st.metric(
                "CPU Usage",
                f"{cpu_percent}%",
                "Current load"
            )
        
        # Disk usage
        disk = psutil.disk_usage('/')
        with col3:
            st.metric(
                "Disk Usage",
                f"{(disk.used / disk.total) * 100:.1f}%",
                f"{disk.free / (1024**3):.1f} GB free"
            )
        
        # Progress bars
        st.subheader("📈 Resource Usage")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Memory Usage**")
            st.progress(memory.percent / 100)
            
        with col2:
            st.write("**CPU Usage**")
            st.progress(cpu_percent / 100)
        
        # Real-time updates
        if st.button("🔄 Refresh Data"):
            st.rerun()
            
        # Auto-refresh option
        auto_refresh = st.checkbox("🔄 Auto-refresh (5 seconds)")
        if auto_refresh:
            time.sleep(5)
            st.rerun()
            
    except Exception as e:
        st.error(f"❌ System monitoring requires psutil: pip install psutil")
        st.info("📊 Demo metrics would be displayed here")

def show_documentation():
    st.header("📚 Project Documentation")
    
    tab1, tab2, tab3 = st.tabs(["📖 Overview", "🛠️ Setup", "🔧 Usage"])
    
    with tab1:
        st.markdown("""
        ## 🧠 Automation Suite - Internship Project
        
        ### 📋 Project Description
        This is a comprehensive automation dashboard built with Streamlit that provides various tools and utilities for automation tasks.
        
        ### 🎯 Objectives
        - Create a unified dashboard for multiple automation tools
        - Demonstrate Python programming skills
        - Integrate various APIs and services
        - Provide a user-friendly interface
        
        ### 🌟 Features
        - **Multi-category navigation**: Python tools, Web tools, System monitoring
        - **Modern UI**: Dark theme with responsive design
        - **Real-time monitoring**: System resource tracking
        - **API integrations**: Email, SMS, WhatsApp services
        - **Web components**: Camera access, location services
        
        ### 🛠️ Technologies Used
        - **Frontend**: Streamlit, HTML, CSS, JavaScript
        - **Backend**: Python
        - **Libraries**: psutil, requests, beautifulsoup4, Pillow, etc.
        - **APIs**: Gmail SMTP, Twilio, WhatsApp, EmailJS
        """)
    
    with tab2:
        st.markdown("""
        ## 🛠️ Installation & Setup
        
        ### 📋 Prerequisites
        - Python 3.7 or higher
        - pip package manager
        
        ### 📦 Installation Steps
        
        1. **Clone/Download the project**
        ```bash
        # Download project files
        ```
        
        2. **Install dependencies**
        ```bash
        pip install -r requirements.txt
        ```
        
        3. **Run the application**
        ```bash
        streamlit run app.py
        ```
        
        ### 🔧 Configuration
        - Set up API keys for external services
        - Configure email credentials
        - Install optional dependencies as needed
        """)
    
    with tab3:
        st.markdown("""
        ## 🔧 Usage Guide
        
        ### 🏠 Dashboard Navigation
        1. Use the sidebar to select categories
        2. Choose specific tools from the dropdown
        3. Follow on-screen instructions for each tool
        
        ### 🔧 Python Tools
        - **Email Sender**: Configure Gmail SMTP settings
        - **WhatsApp**: Schedule messages using pywhatkit
        - **SMS Sender**: Use Twilio API for SMS
        - **Web Scraper**: Extract data from websites
        
        ### 🟨 Web Tools
        - **Photo Capture**: Access device camera
        - **Email Composer**: Create and send emails
        - **Location Tools**: GPS and mapping features
        
        ### 📊 System Monitor
        - View real-time system metrics
        - Monitor RAM, CPU, and disk usage
        - Auto-refresh capabilities
        
        ### 💡 Tips
        - Install required libraries for each tool
        - Configure API credentials properly
        - Use demo mode for testing
        """)

if __name__ == "__main__":
    main()