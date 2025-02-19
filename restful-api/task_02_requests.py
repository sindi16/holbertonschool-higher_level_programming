#!/usr/bin/python3
import requests
import csv

def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/"
    response = requests.get(url)
    print(f"Status Code: {status_code}")
    if response.status_code == 200:
        posts = response.json

        for post in post:
            print(post.get('title'))

    
def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])
        else:
            print("Failed to fetch posts")

def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()
        post_data = [{"id": post["id"], "title" : post["title"], "body" : post["body"]} for post in posts]
    
        with open("posts.csv", "w", encoding="utf-8") as file:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(post_data)

fetch_and_print_posts()

