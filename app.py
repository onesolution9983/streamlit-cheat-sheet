import streamlit as st


# Page configuration
st.set_page_config(
    page_title="Streamlit Cheat Sheet",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for premium look
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    h1 {
        background: -webkit-linear-gradient(45deg, #FF4B4B, #FF914D);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: 3.5rem !important;
        padding-bottom: 1rem;
    }
    
    h2 {
        color: #31333F;
        border-bottom: 2px solid #F0F2F6;
        padding-bottom: 0.5rem;
        margin-top: 2rem;
    }
    
    .stCodeBlock {
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
    }
    
    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background-color: #f8f9fa;
    }
</style>
""", unsafe_allow_html=True)

# Intro Animation
if "intro_shown" not in st.session_state:
    st.toast("Welcome to the Ultimate Streamlit Cheat Sheet!", icon="🚀")
    st.balloons()
    st.session_state.intro_shown = True

st.title("Streamlit Cheat Sheet 🚀")

# Sidebar
st.sidebar.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", width=250)
st.sidebar.info("💡 **Tip:** You can use  either **Sidebar Navigation** or **Tabs** mode to check the cheat sheet.")
layout_mode = st.sidebar.radio("Layout Mode", ["Sidebar Navigation", "Tabs"], index=0)

st.sidebar.markdown("---")
st.sidebar.caption("Made with ❤️ using Streamlit")

# Function to render content based on section name
def render_install_text():
    st.header("Install & Import")
    st.code("pip install streamlit")
    st.code("streamlit run first_app.py")
    st.code("import streamlit as st")

    st.header("Command line")
    st.code("""
streamlit --help
streamlit run your_script.py
streamlit hello
streamlit config show
streamlit cache clear
streamlit docs
streamlit version
    """)

    st.header("Magic commands")
    st.markdown("Magic commands implicitly call `st.write()`.")
    st.code("""
'_This_ is some **Markdown**'
my_variable
'dataframe:', my_data_frame
    """)

    st.header("Display text")
    st.code("st.write('Most objects') # df, err, func, keras!")
    st.code("st.write(['st', 'is <', 3])")
    st.code("st.text('Fixed width text')")
    st.code("st.markdown('_Markdown_')")
    st.code(r"st.latex(r''' e^{i\pi} + 1 = 0 ''')")
    st.code("st.title('My title')")
    st.code("st.header('My header')")
    st.code("st.subheader('My sub')")
    st.code("st.code('for i in range(8): foo()')")
    st.code("st.html('<p>Hi!</p>')")
    
    st.header("Layouts & Containers")
    st.code("""
st.sidebar
st.columns
st.tabs
st.expander
st.popover
st.container
st.empty
    """)

def render_data_media():
    st.header("Display data")
    st.code("""
st.dataframe(my_dataframe)
st.table(data.iloc[0:10])
st.json({'foo':'bar','fu':'ba'})
st.metric('My metric', 42, 2)
    """)

    st.header("Display media")
    st.code("""
st.image('./header.png')
st.audio(data)
st.video(data)
    """)
    
    st.header("Display charts")
    st.code("""
st.area_chart(df)
st.bar_chart(df)
st.line_chart(df)
st.map(df)
st.scatter_chart(df)
    """)
    st.code("""
st.altair_chart(chart)
st.graphviz_chart(fig)
st.plotly_chart(fig)
st.pydeck_chart(chart)
st.pyplot(fig)
st.vega_lite_chart(df, spec)
    """)

    st.header("Utilities")
    st.code("""
st.help(df)
st.get_option(key)
st.set_option(key, value)
st.set_page_config()
st.query_params
    """)

def render_widgets_control():
    st.header("Interactive widgets")
    st.code("""
st.button('Click me')
st.download_button('Download file', data)
st.link_button('Go to gallery', url)
st.page_link('app.py', label='Home')
st.data_editor('Edit data', data)
st.checkbox('I agree')
st.feedback('thumbs')
st.pills('Tags', ['Sports', 'Politics'])
st.radio('Pick one', ['cats', 'dogs'])
st.segmented_control('Filter', ['Open', 'Closed'])
st.toggle('Enable')
st.selectbox('Pick one', ['cats', 'dogs'])
st.multiselect('Buy', ['milk', 'apples', 'potatoes'])
st.slider('Pick a number', 0, 100)
st.select_slider('Pick a size', ['S', 'M', 'L'])
st.text_input('First name')
st.number_input('Pick a number', 0, 10)
st.text_area('Text to translate')
st.date_input('Your birthday')
st.datetime_input('Event date and time')
st.time_input('Meeting time')
st.file_uploader('Upload a CSV')
st.audio_input('Record a voice message')
st.camera_input('Take a picture')
st.color_picker('Pick a color')
    """)

    st.header("Control flow")
    st.code("""
st.stop()
st.rerun()
st.form()
st.dialog
st.fragment
    """)

    st.header("Status elements")
    st.code("""
st.progress(50)
st.spinner()
st.balloons()
st.snow()
st.toast()
st.error()
st.warning()
st.success()
st.info()
st.exception()
    """)

    st.header("Personalize apps for users")
    st.code("""
st.user.name
st.user.email
    """)

# Logic for Layout
if layout_mode == "Sidebar Navigation":
    st.sidebar.markdown("---")
    selected_section = st.sidebar.radio(
        "Go to",
        ["Install & Text", "Data & Media", "Widgets & Control"],
        label_visibility="collapsed"
    )
    
    if selected_section == "Install & Text":
        render_install_text()
    elif selected_section == "Data & Media":
        render_data_media()
    elif selected_section == "Widgets & Control":
        render_widgets_control()

elif layout_mode == "Tabs":
    tab1, tab2, tab3 = st.tabs(["Install & Text", "Data & Media", "Widgets & Control"])
    
    with tab1:
        render_install_text()
    with tab2:
        render_data_media()
    with tab3:
        render_widgets_control()
