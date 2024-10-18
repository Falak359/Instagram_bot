# Import the InstaBot library for Instagram automation
from instabot import Bot
# Create an instance of the Instagram bot
instagram_bot = Bot()
# Function to log in to Instagram using provided credentials
def login_instagram(user, passwd):
    instagram_bot.login(username=user, password=passwd)
    print("Successfully logged in to Instagram!")
# Function to follow a specified user
def follow_account(account):
    instagram_bot.follow(account)
    print(f"Successfully followed {account}!")
# Function to send a direct message to a user
def send_direct_message(msg, recipient):
    instagram_bot.send_message(msg, recipient)
    print(f"Message sent to {recipient}: '{msg}'")
# Function to upload a photo with a specific caption
def upload_image(image_path, caption_text):
    instagram_bot.upload_photo(image_path, caption=caption_text)
    print("Image uploaded successfully with caption!")
# Function to unfollow a specified user
def unfollow_account(account):
    instagram_bot.unfollow(account)
    print(f"Successfully unfollowed {account}!")
  
# Replace with your actual Instagram credentials
INSTAGRAM_USERNAME = "your_username"
INSTAGRAM_PASSWORD = "your_password"
# Execute the functions in order
login_instagram(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
# Follow a specific account
follow_account("any_acc_of_your_choice")
# Send a direct message
send_direct_message("Hello!Just popping in to share a little happiness from my Instagram automation project”", "any_acc_of_your_choice")
# Upload a photo to the Instagram account
upload_image("photo.jpg", "Sharing smiles one photo at a time!")
# Unfollow a specific account
unfollow_account("any_acc_of_your_choice")
