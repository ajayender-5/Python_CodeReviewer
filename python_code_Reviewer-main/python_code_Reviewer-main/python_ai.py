import google.generativeai as genai
import streamlit as st

# Set page configuration to full width
st.set_page_config(page_title="Python code reviewer", page_icon="💻")

st.image(r'https://innomatics.in/wp-content/uploads/2023/01/Innomatics-Logo1.png')
f = open(r"C:\Users\madas\OneDrive\Desktop\GenAI_apps\gen_AI_app\Key.txt")
key = f.read()
client = genai.configure(api_key=key)
#st.snow()
st.title('💬:rainbow[Python code reviewer]')
#st.subheader("GenAi")

prompt = st.text_area('Enter your python code')
if st.button("Generate"):
    #st.balloons()
    model = genai.GenerativeModel(
        model_name="models/gemini-1.5-pro-latest",
        system_instruction="""You are a helpful AI assistant.
                                        please fix bugs in given python code""")

    response = model.generate_content(prompt)
    st.write(response.text)