class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")
    
    def display_timeline(self):
        print(f"Username: {self.username}")
        print(f"List of posts: {self.posts}")
        

def main():
    user_one = SocialMediaProfile('johndoe')
    user_one.add_post("Hello, world!")
    user_one.add_post("Had a great day at the park!")
    user_one.add_post("What's up, Natalie? How are you?")

    user_one.display_timeline()


if __name__ == '__main__':
    main()


