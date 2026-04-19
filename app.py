import streamlit as st
from api_calling import generate_audio, generate_note, generate_quiz
from PIL import Image



st.title("Note summary and quiz Generator")
st.markdown("Upload upto 3 images to generate a summary and quiz.")

st.divider()

# image upload section
with st.sidebar:
    st.header("Upload your images here:")
    images = st.file_uploader("Upload the photos of your notes.", 
                             type=["jpg", "jpeg", "png"], accept_multiple_files=True)
    
    pil_images = []

    for img in images:
         pil_img = Image.open(img)
         pil_images.append(pil_img)

    if images:
        # st.image(images)
        if len(images) > 3:
            st.error("Please upload a maximum of 3 images.")
        else:
            st.header("Uploaded Images:")
            col = st.columns(len(images))
            for i, img in enumerate(images):
                with col[i]:
                    st.image(img)
    
    # category selection
    st.header("Enter the difficulty of quiz")

    selected_option = st.selectbox("Choose your options", 
                 ("Easy", "Medium", "Hard"), 
                 key="difficulty",
                 index= None)
    if selected_option:
        st.markdown(f"You have selected **{selected_option}** difficulty level for the quiz.")
   

    pressed = st.button("Click the button to initiate AI", type="primary")

if pressed:
    if not images:
        st.error("Please upload at least one image to generate the summary and quiz.")
    if not selected_option:
        st.error("Please select a difficulty level for the quiz.")

    if images and selected_option:
        # note
        with st.container(border = True):
            st.subheader("Summary of your notes:")

            with st.spinner("AI is generating the summary of your notes..."):
                generate_text = generate_note(pil_images)
                st.markdown(generate_text)


        # audio
        with st.container(border = True):
            st.subheader("Audio Transcription :")
            with st.spinner("AI is generating the audio transcription of your notes..."):
                # clear markdown
                generate_text = generate_text.replace("$", " ")
                generate_text = generate_text.replace("*", " ")
                generate_text = generate_text.replace('"', " ")
                generate_text = generate_text.replace('.', " ")
                audio_buffer = generate_audio(generate_text)
                st.audio(audio_buffer, format='audio/mp3')




        # quiz
        with st.container(border = True):
            st.subheader(f"Quiz {selected_option} Difficulty: ")
            
            with st.spinner("AI is generating the quiz based on your notes..."):
                quizzes = generate_quiz(pil_images, selected_option)
                st.markdown(quizzes)