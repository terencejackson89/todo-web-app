import streamlit as st
import todo_functions as td


todos = td.read_tasks()


def add_todo():
    todo = st.session_state['new_todo']
    todos.append(todo.capitalize() + '\n')
    td.write_tasks(todos)


st.title("My Todo App")
st.subheader("Here you can view, edit, and complete todo tasks!")

for idx, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(idx)
        td.write_tasks(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Default label", label_visibility="hidden",
              placeholder="Add new task", on_change=add_todo,
              key='new_todo')