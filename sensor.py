import random
import time
from datetime import datetime
import os

from dotenv import load_dotenv
from supabase import create_client

# Load environment variables
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Connect to Supabase
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

print("Temperature Sensor Started...\n")

while True:
    # Generate random temperature
    temperature = round(random.uniform(20, 40), 1)

    # Current date and time
    current_time = datetime.now()

    # Insert into Supabase
    data = {
        "temperature": temperature,
        "timestamp": current_time.isoformat()
    }

    supabase.table("temperature").insert(data).execute()

    print(f"Temperature: {temperature}°C | Time: {current_time.strftime('%Y-%m-%d %H:%M:%S')} | Uploaded Successfully")

    # Wait 5 seconds
    time.sleep(5)