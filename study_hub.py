from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for study resources
RESOURCES = [
    {"id": 1, "title": "Introduction to Flask Routing", "category": "Programming", "content": "Flask uses decorators like @app.route('/') to bind URLs to functions."},
    {"id": 2, "title": "English Literature: Poetry Analysis", "category": "Literature", "content": "Focus on theme, tone, imagery, and structural devices when analyzing poems."}
]

@app.route('/')
def study_hub_home():
    resource_html = ""
    for r in RESOURCES:
        resource_html += f'''
        <div style="background: #1b2230; border-radius: 8px; padding: 14px; margin-bottom: 12px; border: 1px solid #2a3447;">
            <div style="font-size: 11px; background: #0284c7; color: #fff; padding: 2px 6px; border-radius: 4px; display: inline-block; margin-bottom: 6px; font-weight: bold;">{r['category']}</div>
            <div style="font-size: 15px; font-weight: bold; color: #fff; margin-bottom: 6px;">{r['title']}</div>
            <div style="font-size: 13px; color: #94a3b8; line-height: 1.4;">{r['content']}</div>
        </div>
        '''
    
    if not resource_html:
        resource_html = "<p style='color:#64748b; text-align:center;'>No study resources added yet.</p>"

    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Study Hub</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {{ font-family: sans-serif; background: #121824; color: #fff; margin: 0; padding: 12px; }}
            h2 {{ color: #38bdf8; border-bottom: 2px solid #38bdf8; padding-bottom: 6px; }}
            .card {{ background: #1b2230; padding: 15px; border-radius: 8px; margin-bottom: 15px; border: 1px solid #2a3447; }}
            input, select, textarea {{ width: 100%; padding: 10px; margin: 6px 0 12px 0; background: #121824; border: 1px solid #334155; color: #fff; border-radius: 6px; box-sizing: border-box; font-family: sans-serif; }}
            button {{ width: 100%; padding: 12px; background: #0284c7; color: white; border: none; border-radius: 6px; font-weight: bold; cursor: pointer; }}
        </style>
    </head>
    <body>
        <h2>Digital Study Hub</h2>
        
        <div class="card">
            <h3 style="margin-top:0; color:#38bdf8; font-size:15px;">Add New Study Note</h3>
            <form action="/add" method="POST">
                <label style="font-size:12px; color:#94a3b8;">Resource Title</label>
                <input type="text" name="title" placeholder="e.g., Python Basics" required>
                
                <label style="font-size:12px; color:#94a3b8;">Category</label>
                <select name="category">
                    <option value="Programming">Programming</option>
                    <option value="Literature">Literature</option>
                    <option value="General">General</option>
                </select>
                
                <label style="font-size:12px; color:#94a3b8;">Notes / Summary Content</label>
                <textarea name="content" rows="3" placeholder="Type core summary points here..." required></textarea>
                
                <button type="submit">+ Upload Resource</button>
            </form>
        </div>

        <h3 style="color: #38bdf8; margin-top: 20px;">Available Study Notes</h3>
        {resource_html}
    </body>
    </html>
    '''

@app.route('/add', methods=['POST'])
def add_resource():
    title = request.form.get('title')
    category = request.form.get('category')
    content = request.form.get('content')
    
    if title and content:
        new_id = len(RESOURCES) + 1
        RESOURCES.append({
            "id": new_id,
            "title": title,
            "category": category,
            "content": content
        })
    return redirect(url_for('study_hub_home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True)
