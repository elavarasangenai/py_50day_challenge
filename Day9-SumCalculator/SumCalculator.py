import streamlit as st

def main():
    st.title("Sum Calculator")
    if 'n' not in st.session_state:
        st.session_state.n = ''
    if 'inputs' not in st.session_state:
        st.session_state.inputs = []
    if 'show_inputs' not in st.session_state:
        st.session_state.show_inputs = False
    if 'sum_result' not in st.session_state:
        st.session_state.sum_result = None

    with st.form(key='n_form'):
        n = st.text_input("Enter how many numbers you want to sum (n):", value=st.session_state.n)
        submit_n = st.form_submit_button("Submit")
        if submit_n:
            if n.isdigit() and int(n) > 0:
                st.session_state.n = n
                st.session_state.inputs = ['' for _ in range(int(n))]
                st.session_state.show_inputs = True
                st.session_state.sum_result = None
            else:
                st.warning("Please enter a valid positive integer for n.")

    if st.session_state.show_inputs:
        with st.form(key='inputs_form'):
            input_values = []
            for i in range(int(st.session_state.n)):
                value = st.text_input(f"Enter number {i+1}", value=st.session_state.inputs[i], key=f'input_{i}')
                input_values.append(value)
            sum_btn = st.form_submit_button("Sum")
            if sum_btn:
                try:
                    numbers = [float(val) for val in input_values]
                    st.session_state.sum_result = sum(numbers)
                    st.session_state.inputs = input_values
                except ValueError:
                    st.error("Please enter valid numbers in all input boxes.")
        if st.session_state.sum_result is not None:
            st.success(f"Sum is: {st.session_state.sum_result}")

if __name__ == "__main__":
    main()
