import os
from flask import Flask, render_template
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

app = Flask(__name__)

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route('/')
def index():
    # Fetch latest 20 temperature records
    response = supabase.table("temperature").select("*").order("timestamp", desc=True).limit(20).execute()
    records = response.data
    # Reverse to display them chronologically on the chart
    records.reverse()
    return render_template('index.html', records=records)

if __name__ == '__main__':
    app.run(debug=True)
