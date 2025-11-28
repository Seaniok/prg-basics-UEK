# facebook = True
# twitter = False
# instagram = True
# You are a good influencer!

def f(socialmedia1, socialmedia2, socialmedia3):
    if socialmedia1 == True and socialmedia2 == True or socialmedia3 == True:
        print('You are a good influencer')
    else:
        print('Try harder')

print(f(False, True, True))