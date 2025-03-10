import streamlit as st
import google.generativeai as genai  # type: ignore
from datetime import datetime

# SVG icon string
Travel_ICON = """<svg width="193" height="52" viewBox="0 0 193 52" fill="none" xmlns="http://www.w3.org/2000/svg">
<g clip-path="url(#clip0_14_9)">
<path d="M64.008 20.624H57.128V15.6H77.192V20.624H70.344V38H64.008V20.624ZM90.536 38.448C88.168 38.448 86.0347 37.9467 84.136 36.944C82.2587 35.9413 80.776 34.5547 79.688 32.784C78.6213 31.0133 78.088 29.0187 78.088 26.8C78.088 24.5813 78.6213 22.5867 79.688 20.816C80.776 19.0453 82.2587 17.6587 84.136 16.656C86.0347 15.6533 88.168 15.152 90.536 15.152C92.904 15.152 95.0267 15.6533 96.904 16.656C98.8027 17.6587 100.285 19.0453 101.352 20.816C102.44 22.5867 102.984 24.5813 102.984 26.8C102.984 29.0187 102.44 31.0133 101.352 32.784C100.285 34.5547 98.8027 35.9413 96.904 36.944C95.0267 37.9467 92.904 38.448 90.536 38.448ZM90.536 33.2C91.6667 33.2 92.6907 32.9333 93.608 32.4C94.5253 31.8667 95.2507 31.12 95.784 30.16C96.3173 29.1787 96.584 28.0587 96.584 26.8C96.584 25.5413 96.3173 24.432 95.784 23.472C95.2507 22.4907 94.5253 21.7333 93.608 21.2C92.6907 20.6667 91.6667 20.4 90.536 20.4C89.4053 20.4 88.3813 20.6667 87.464 21.2C86.5467 21.7333 85.8213 22.4907 85.288 23.472C84.7547 24.432 84.488 25.5413 84.488 26.8C84.488 28.0587 84.7547 29.1787 85.288 30.16C85.8213 31.12 86.5467 31.8667 87.464 32.4C88.3813 32.9333 89.4053 33.2 90.536 33.2ZM116.639 38.448C113.311 38.448 110.719 37.5413 108.863 35.728C107.028 33.9147 106.111 31.344 106.111 28.016V15.6H112.447V27.824C112.447 31.408 113.865 33.2 116.703 33.2C119.519 33.2 120.927 31.408 120.927 27.824V15.6H127.167V28.016C127.167 31.344 126.239 33.9147 124.383 35.728C122.548 37.5413 119.967 38.448 116.639 38.448ZM141.251 32.048H137.795V38H131.459V15.6H141.699C143.725 15.6 145.485 15.9413 146.979 16.624C148.472 17.2853 149.624 18.2453 150.435 19.504C151.245 20.7413 151.651 22.2027 151.651 23.888C151.651 25.5093 151.267 26.928 150.499 28.144C149.752 29.3387 148.675 30.2773 147.267 30.96L152.099 38H145.315L141.251 32.048ZM145.251 23.888C145.251 22.8427 144.92 22.032 144.259 21.456C143.597 20.88 142.616 20.592 141.315 20.592H137.795V27.152H141.315C142.616 27.152 143.597 26.8747 144.259 26.32C144.92 25.744 145.251 24.9333 145.251 23.888ZM155.146 15.6H161.482V32.976H172.17V38H155.146V15.6ZM184.396 29.968V38H178.06V29.872L169.516 15.6H176.204L181.516 24.496L186.828 15.6H192.972L184.396 29.968Z" fill="#3A78C9"/>
<g clip-path="url(#clip1_14_9)">
<path d="M37.9551 43.9202L36.0433 45.8319C35.8512 46.024 35.614 46.1647 35.3534 46.2414C35.0927 46.3181 34.8171 46.3282 34.5515 46.2709C34.286 46.2135 34.0391 46.0905 33.8334 45.9131C33.6277 45.7356 33.4697 45.5095 33.374 45.2552L27.7874 30.4103L20.682 37.2069L21.2185 42.8135C21.3427 43.9044 21.2278 44.5608 20.2439 45.5447L18.957 46.8316C18.7598 47.0419 18.5148 47.2016 18.2428 47.2971C17.9707 47.3926 17.6797 47.4211 17.3943 47.3803C16.9928 47.3207 16.4341 47.098 16.0406 46.377L12.365 39.8547C12.3378 39.8059 12.3126 39.7549 12.2896 39.7032C12.2868 39.6989 12.2831 39.6953 12.2789 39.6924C12.2267 39.6699 12.1759 39.6445 12.1266 39.6163L5.57058 35.9099C4.86966 35.5178 4.65637 34.967 4.60107 34.5727C4.56386 34.3079 4.58932 34.038 4.67538 33.7848C4.76144 33.5316 4.90571 33.3021 5.0966 33.1148L6.45534 31.7561C7.19002 31.0214 8.23278 30.6379 9.18433 30.7507L14.6868 31.2878L21.5725 24.1953L6.74691 18.6253C6.49266 18.5298 6.26642 18.372 6.08887 18.1665C5.91132 17.9609 5.78812 17.7141 5.73055 17.4487C5.67297 17.1832 5.68285 16.9076 5.75929 16.6469C5.83572 16.3863 5.97627 16.149 6.16808 15.9567L8.10064 14.0241C8.37567 13.7599 8.70668 13.5611 9.06909 13.4423C9.43151 13.3236 9.81601 13.288 10.1941 13.3383L30.0905 15.2737L34.1302 11.0158C34.4174 10.6955 35.2534 9.84804 35.448 9.65342C39.4187 5.68705 43.0769 4.60551 45.2357 6.76428C45.9151 7.44366 46.9033 8.97477 45.8885 11.5924C45.2903 13.1386 44.0996 14.8091 42.3502 16.5585C42.1577 16.751 41.3124 17.5847 40.9878 17.8763L36.7292 21.9138L38.6423 41.8325C38.6915 42.2098 38.6553 42.5932 38.5363 42.9546C38.4173 43.3159 38.2187 43.6459 37.9551 43.9202V43.9202Z" fill="#3A78C9"/>
</g>
</g>
<defs>
<clipPath id="clip0_14_9">
<rect width="193" height="52" fill="white"/>
</clipPath>
<clipPath id="clip1_14_9">
<rect width="52" height="52" fill="white" transform="translate(-8.76955 24) rotate(-45)"/>
</clipPath>
</defs>
</svg>
"""

# Page configuration
st.set_page_config(
    page_title="Travel Recomendation",
    page_icon=" ✈️",
    layout="wide"
)

# Initialize session state for user preferences and chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'user_preferences' not in st.session_state:
    st.session_state.user_preferences = {
        'age': '',
        'gender': '',
        'interests': '',
        'number_of_people': ''
    }

# Custom CSS with colors from the stylesheet
st.markdown("""
    <style>
    :root {
        --bright-navy-blue: hsl(214, 57%, 51%);
        --united-nations-blue: hsl(214, 56%, 58%);
        --spanish-gray: hsl(0, 0%, 60%);
        --black-coral: hsl(225, 8%, 42%);
        --oxford-blue: hsl(208, 97%, 12%);
        --yale-blue: hsl(214, 72%, 33%);
        --gainsboro: hsl(0, 0%, 88%);
        --cultured: hsl(0, 0%, 98%);
        --white: hsl(0, 0%, 100%);
    }
    
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    
    .main-header {
        text-align: center;
        padding: 2rem 0;
        color: hsl(214, 57%, 51%); /* bright-navy-blue */
    }
    
    .sub-header {
        color: hsl(225, 8%, 42%); /* black-coral */
        font-size: 1.2rem;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .user-preferences {
        background-color: hsl(0, 0%, 98%); /* cultured */
        padding: 1rem;
        border-radius: 5px;
        margin-bottom: 1rem;
        border: 1px solid hsl(214, 56%, 58%); /* united-nations-blue */
    }
    
    /* Style for buttons */
    .stButton button {
        background-color: hsl(214, 57%, 51%) !important; /* bright-navy-blue */
        color: hsl(0, 0%, 100%) !important; /* white */
        border: none !important;
        border-radius: 100px !important;
        transition: 0.25s ease-in-out !important;
    }
    
    .stButton button:hover {
        background-color: hsl(214, 72%, 33%) !important; /* yale-blue */
    }
    
    /* Style for expanders */
    .streamlit-expanderHeader {
        background-color: hsl(0, 0%, 98%) !important; /* cultured */
        color: hsl(214, 57%, 51%) !important; /* bright-navy-blue */
    }
    
    /* Style for text input and select boxes */
    .stTextInput input, .stSelectbox select {
        border-color: hsl(214, 56%, 58%) !important; /* united-nations-blue */
        border-radius: 5px !important;
    }
    
    /* Chat message styling */
    .chat-message {
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 5px;
    }
    
    .user-message {
        background-color: hsl(214, 56%, 58%, 0.1); /* united-nations-blue with opacity */
        border-left: 4px solid hsl(214, 57%, 51%); /* bright-navy-blue */
    }
    
    .assistant-message {
        background-color: hsl(0, 0%, 98%); /* cultured */
        border-left: 4px solid hsl(214, 72%, 33%); /* yale-blue */
    }
    </style>
""", unsafe_allow_html=True)

def initialize_ai():
    """Initialize the AI model with configuration"""
    genai.configure(api_key="AIzaSyAVYQrbN_AfkZ08zIqwrZz18fj6m1D6LGM")
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }
    return genai.GenerativeModel(
        model_name="tunedModels/travel-chat-8vaxzznz0g87",
        generation_config=generation_config,
    )

def get_ai_response(model, message, preferences):
    """Get AI response for the given message with user preferences"""
    try:
        enhanced_message = f"""User Profile:
- Age: {preferences['age']}
- Gender: {preferences['gender']}
- Interests: {preferences['interests']}
- Number of people: {preferences['number_of_people']}

Query: {message}"""
        
        chat_session = model.start_chat(history=[])
        response = chat_session.send_message(enhanced_message)
        return response.text
    except Exception as e:
        st.error(f"Error getting response: {str(e)}")
        return None

# Main UI
st.markdown(f"<h1 class='main-header'>{Travel_ICON} </h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-header'>Your personal AI-powered travel advisor</p>", unsafe_allow_html=True)

# User Preferences Section
with st.expander("✨ Set Your Travel Preferences", expanded=True):
    col1, col2 = st.columns(2)
    
    with col1:
        st.session_state.user_preferences['age'] = st.text_input(
            "Age",
            value=st.session_state.user_preferences['age']
        )
        st.session_state.user_preferences['gender'] = st.selectbox(
            "Gender",
            options=['', 'Male', 'Female', 'Other'],
            index=0 if not st.session_state.user_preferences['gender'] else 
                  ['', 'Male', 'Female', 'Other'].index(st.session_state.user_preferences['gender'])
        )
    
    with col2:
        st.session_state.user_preferences['interests'] = st.text_input(
            "Interests (e.g., adventure, culture, food)",
            value=st.session_state.user_preferences['interests']
        )
        st.session_state.user_preferences['number_of_people'] = st.text_input(
            "Number of People",
            value=st.session_state.user_preferences['number_of_people']
        )

# Main Layout
main_col1, main_col2 = st.columns([2, 1])

with main_col1:
    st.subheader("💭 Let's Plan Your Journey")
    
    st.markdown("### 🚀 Quick Prompts")
    prompt_cols = st.columns(2)
    
    if prompt_cols[0].button("🌅 Suggest weekend getaways"):
        user_message = "Suggest some weekend getaway destinations for a relaxing break"
    elif prompt_cols[1].button("🏖️ Beach vacation ideas"):
        user_message = "Recommend some amazing beach destinations for a vacation"
    else:
        user_message = st.text_area(
            "Enter your travel query:",
            placeholder="Example: Suggest a 5-day itinerary for Puri",
            height=100
        )

    if st.button("Get Recommendations 🎯", type="primary"):
        if user_message:
            if not any(st.session_state.user_preferences.values()):
                st.warning("Please set your travel preferences first!")
            else:
                with st.spinner("Thinking... ✨"):
                    model = initialize_ai()
                    response = get_ai_response(model, user_message, st.session_state.user_preferences)
                    
                    if response:
                        st.session_state.chat_history.append(("user", user_message))
                        st.session_state.chat_history.append(("assistant", response))

with main_col2:
    st.subheader("📌 Travel Tips")
    with st.expander("Best Time to Book", expanded=True):
        st.markdown("""
        - Book flights 3-4 months in advance
        - Tuesday/Wednesday are often cheaper
        - Use incognito mode while searching
        """)
    
    with st.expander("Packing Essentials", expanded=True):
        st.markdown("""
        - Travel documents
        - Universal adapter
        - First-aid kit
        - Portable charger
        """)

# Display chat history with styled messages
st.markdown("### 💬 Previous Recommendations")
for role, message in st.session_state.chat_history:
    if role == "user":
        st.markdown(f"""
            <div class='chat-message user-message'>
                <strong>You:</strong> {message}
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div class='chat-message assistant-message'>
                <strong>AI:</strong> {message}
            </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div style='text-align: center; color: hsl(225, 8%, 42%); padding: 20px;'>
    <p>Built with ❤️ at SAI International</p>
</div>
""", unsafe_allow_html=True)