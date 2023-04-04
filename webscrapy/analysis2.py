from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import requests
from bs4.element import Comment
from IPython.display import clear_output

while input("Would you like to scrape a website (y/n)? ") == "y":
    try:
        clear_output( )
        site = input("Enter a website to analyze: ")
        print(site)       # remove after runs properly
    except:
        print("Something went wrong, please try again.")
print("Thanks for analyzing! Come back again!")
