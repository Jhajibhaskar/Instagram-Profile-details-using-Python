# First run 'pip install instagramy' in terminal of pycharm then execute the below program
from instagramy import InstagramUser

Id=input("Enter Instagram ID= ")
user = InstagramUser(Id)
print('UserName = ',user.username)
print('Followers = ',user.number_of_followers)
print('Following = ',user.number_of_followings)
print('No. of Posts = ',user.number_of_posts)
print('is Instagram Id Private = ',user.is_private)
print('Bio = ',user.biography)
print('Insta Post Link = ',user.posts)
