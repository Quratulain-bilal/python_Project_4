import requests

# Your GitHub personal access token
GITHUB_TOKEN = ""

def get_github_profile():
    # Get username input
    username = input("Enter GitHub username: ").strip()
    
    # API endpoint
    url = f"https://api.github.com/users/{username}"
    
    # Headers with authentication
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    try:
        # Make the API request
        response = requests.get(url, headers=headers)
        
        # Check if request was successful
        if response.status_code == 200:
            user_data = response.json()
            
            # Display profile information
            print("\n✅ GitHub Profile Found!")
            print(f"👤 Name: {user_data.get('name', 'Not specified')}")
            print(f"📸 Avatar URL: {user_data['avatar_url']}")
            print(f"📌 Bio: {user_data.get('bio', 'No bio')}")
            print(f"📍 Location: {user_data.get('location', 'Not specified')}")
            print(f"🔗 Profile URL: {user_data['html_url']}")
            print(f"📊 Public Repos: {user_data['public_repos']}")
            print(f"👥 Followers: {user_data['followers']}")
            print(f"👣 Following: {user_data['following']}")
            
        elif response.status_code == 404:
            print("❌ Error: User not found!")
        else:
            print(f"❌ Error: {response.status_code} - {response.json().get('message', 'Unknown error')}")
            
    except Exception as e:
        print(f"🚨 An error occurred: {e}")

if __name__ == "__main__":
    get_github_profile()