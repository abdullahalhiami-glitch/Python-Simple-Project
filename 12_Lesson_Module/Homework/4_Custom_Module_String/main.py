import String_tool as st

text = input("Enter a text: ")
reversed_text = st.reverse_string(text)

default_paragraph = st.generate_default_paragraph(100)

print("Reversed text:", reversed_text)
print("Word count:", st.count_words(text))
print("Uppercase text:", st.to_uppercase(text))
print("------------------------------------------")
print("Default paragraph:", default_paragraph)