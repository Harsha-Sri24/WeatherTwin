"""
Reusable city autocomplete search component.
Uses a DOM hack to attach dropdown logic natively to a Streamlit st.text_input, 
preserving layout, theming, and full Streamlit interaction functionality 
(like "Enter" key submits and session_state sync without reloads).
"""

import streamlit as st
import streamlit.components.v1 as components
import uuid

def city_autocomplete(
    label: str,
    default_value: str = "",
    placeholder: str = "Search city...",
    key: str = None,
) -> str:
    """
    Render a native Streamlit text input with a floating autocomplete dropdown 
    attached asynchronously.
    """
    if key is None:
        key = f"city_ac_{uuid.uuid4().hex[:8]}"

    # Native Streamlit input - handles form integration, state, layout perfectly natively
    val = st.text_input(
        label=label,
        value=default_value,
        placeholder=placeholder,
        key=key,
    )

    # Escape label for the JS querySelector
    escaped_label = label.replace("'", "\\'").replace('"', '\\"')

    # Inject a 0-height script that finds the input above and supercharges it
    js = f"""
    <script>
    (function() {{
        var parentDoc = window.parent.document;
        // Search for the specific Streamlit input using its aria-label
        var input = parentDoc.querySelector('input[aria-label="{escaped_label}"]');
        if (!input) return; // Not found yet

        // Prevent double-binding if re-rendered
        if (input.dataset.acBound) return;
        input.dataset.acBound = "true";
        
        // Turn off browser defaults
        input.setAttribute("autocomplete", "off");

        var ddId = "acdd_{key}";
        
        // Cleanup old dropdowns
        var old = parentDoc.getElementById(ddId);
        if (old) old.remove();

        // Global styles for all dropdowns payload (loads once)
        if (!parentDoc.getElementById('ac_styles_v2')) {{
            var style = parentDoc.createElement('style');
            style.id = 'ac_styles_v2';
            style.textContent = [
                '.ac-overlay-dd {{ position:fixed; z-index:999999; display:none;',
                '  background:var(--secondary-background-color, #1e293b); border:1px solid rgba(148,163,184,0.25);',
                '  border-radius:8px; margin-top:4px;',
                '  box-shadow:0 12px 30px rgba(0,0,0,0.5);',
                '  max-height:260px; overflow-y:auto;',
                '  font-family:Inter,-apple-system,sans-serif; }}',
                '.ac-overlay-dd .ac-dd-item {{ padding:10px 14px; color:var(--text-color, #f1f5f9);',
                '  font-size:0.84rem; cursor:pointer;',
                '  border-bottom:1px solid rgba(148,163,184,0.08);',
                '  display:flex; flex-direction:column; gap:1px; }}',
                '.ac-overlay-dd .ac-dd-item:last-child {{ border-bottom:none; }}',
                '.ac-overlay-dd .ac-dd-item:hover {{ background:rgba(59,130,246,0.18); }}',
                '.ac-overlay-dd .ac-hl {{ color:#60a5fa; font-weight:700; }}',
                '.ac-overlay-dd .ac-sub {{ font-size:0.7rem; color:var(--text-secondary-color, #94a3b8); opacity: 0.8; }}'
            ].join('\\n');
            parentDoc.head.appendChild(style);
        }}

        // Create dropdown div
        var dd = parentDoc.createElement('div');
        dd.id = ddId;
        dd.className = 'ac-overlay-dd';
        parentDoc.body.appendChild(dd);

        function positionDd() {{
            var r = input.getBoundingClientRect();
            dd.style.top = r.bottom + 'px';
            dd.style.left = r.left + 'px';
            dd.style.width = r.width + 'px';
        }}

        var timer;
        input.addEventListener('input', function(e) {{
            // Passthrough default Streamlit behaviors - just piggyback for the API fetch
            var val = input.value.trim();
            clearTimeout(timer);
            if (val.length < 2) {{ dd.style.display = 'none'; return; }}

            timer = setTimeout(function() {{
                fetch('https://geocoding-api.open-meteo.com/v1/search?name=' + encodeURIComponent(val) + '&count=5&language=en&format=json')
                .then(function(r) {{ return r.json(); }})
                .then(function(data) {{
                    if (!data.results || data.results.length === 0) {{ dd.style.display = 'none'; return; }}
                    dd.innerHTML = '';
                    positionDd();
                    
                    data.results.forEach(function(res) {{
                        var item = parentDoc.createElement('div');
                        item.className = 'ac-dd-item';
                        
                        var adminStr = res.admin1 ? res.admin1 + ', ' : '';
                        var countryStr = res.country || '';
                        
                        var escaped = val.replace(/[.*+?^${{}}()|[\\]\\\\]/g, '\\\\$&');
                        var regex = new RegExp('(' + escaped + ')', 'gi');
                        var hName = res.name.replace(regex, '<span class="ac-hl">$1</span>');
                        
                        item.innerHTML = '<div>' + hName + '</div><span class="ac-sub">' + adminStr + countryStr + '</span>';
                        
                        // Fire native React updates when item is clicked
                        item.addEventListener('mousedown', function(ev) {{
                            ev.preventDefault(); // Prevent blur
                            var city = res.name + ', ' + countryStr;
                            dd.style.display = 'none';
                            
                            // Emulate standard user React input
                            let nativeSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
                            nativeSetter.call(input, city);
                            input.dispatchEvent(new Event('input', {{ bubbles: true }}));
                            
                            // Simulate Enter to commit the form or sync
                            input.dispatchEvent(new KeyboardEvent('keydown', {{ key: 'Enter', code: 'Enter', keyCode: 13, which: 13, bubbles: true }}));
                        }});
                        dd.appendChild(item);
                    }});
                    dd.style.display = 'block';
                }});
            }}, 200);
        }});

        // Hide dropdown logic
        parentDoc.addEventListener('mousedown', function(e) {{
            if (!e.target.closest('#' + ddId) && e.target !== input) {{
                dd.style.display = 'none';
            }}
        }});
        
        // Reposition cleanly on scroll
        window.parent.addEventListener('scroll', function() {{ if (dd.style.display === 'block') positionDd(); }}, true);
        window.parent.addEventListener('resize', function() {{ if (dd.style.display === 'block') positionDd(); }});

        // Cleanup if component unmounts
        var observer = new MutationObserver(function() {{
           if (!parentDoc.body.contains(input)) {{
               dd.remove();
               observer.disconnect();
           }}
        }});
        observer.observe(parentDoc.body, {{ childList: true, subtree: true }});

    }})();
    </script>
    """
    
    # Render script without altering Streamlit layout space
    components.html(js, height=0)
    
    return val
