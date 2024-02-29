import streamlit as st
import functions

todos = functions.get_todo()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todo(todos)
    st.session_state["new_todo"] = ""


st.title("My To-do App")
st.subheader("This is my to-do app.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todo(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add new to-do .....",
              on_change=add_todo, key="new_todo")