from supabase import Client,create_client
#SUPABASE_URL tells your app which Supabase project to connect to.
SUPABASE_URL="https://yolurkksvcovaqnuajou.supabase.co"
"""SUPABASE_KEY is like a password (usually anon or service key)
 that authenticates your app so it can read/write data securely."""

SUPABASE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9." \
             "eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InlvbHVya2tzdmNvdmF" \
             "xbnVham91Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTM1NDEzOTIsI" \
             "mV4cCI6MjA2OTExNzM5Mn0.DorD-mEQsQjGnUaoEfUPOclREXl" \
             "-f8zCvX-OPva2Fi0"
# create_client is a function that takes Supabase URL (library address) and API key (secret password)
# It returns a client object (magic key) that lets our Python code connect and interact with the Supabase database securely.
# We need this to read/write data from/to our Supabase backend.
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
class Database:
    def __init__(self):
        self.supabase=supabase

    def user(self):
        self.name=input("Enter your name::")
        self.email=input("Enter the email::")
        print(f'Your name is : {self.name}  and email is:{self.email}')
        try:
            response=self.supabase.table("users").insert({
                "fullname":self.name,
                "email": self.email
            }).execute()
            if response.data:
                print(f"User inserted successfully: {response.data}")
            else:
                print("Failed to insert user: No data returned")

        except Exception as e:
            print("Error inserting user:", str(e))


        except Exception as e:
            print("Error inserting user:", str(e))


    def test_connection(self):
        try:
            response = self.supabase.table("users").select("*").execute()
            if response and response.data:
                print("Connected to Supabase! Users:", response.data)
            else:
                print("Connected to Supabase! Users: None")
        except Exception as e:
            print("Connection Error:", str(e))
db=Database()
db.test_connection()
db.user()


