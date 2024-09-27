import streamlit as st

st.title("Text Generator")

def text_generator(text):
  for char in text:
    yield ord(char)

my_text = st.text_input(
  "Masukkan text dibawah",
  placeholder="Masukkan text disini")
my_generator = text_generator(my_text)

total_char = []

for char in my_generator:
  total_char.append(char)

char_gabung = ''.join(str(x) for x in total_char)
st.buttton("Generate")
st.write(char_gabung)
