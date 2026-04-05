
import streamlit as st
import streamlit.components.v1 as components

val = st.text_input('Test Input', key='test_input')
st.write('Current val:', val)

js = '''
<script>
setTimeout(function() {
    var parentDoc = window.parent.document;
    var input = parentDoc.querySelector('input[aria-label=\\'Test Input\\']');
    if (input && input.value !== 'Success!') {
        let nativeSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
        nativeSetter.call(input, 'Success!');
        input.dispatchEvent(new Event('input', { bubbles: true }));
        // also dispatch enter
        input.dispatchEvent(new KeyboardEvent('keydown', { key: 'Enter', code: 'Enter', bubbles: true }));
    }
}, 2000);
</script>
'''
components.html(js, height=0)
