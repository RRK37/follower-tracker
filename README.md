# Follower Tracker

This project provides a simple two-container setup for tracking the follower count of any public Instagram account:
- A worker container periodically scrapes and logs the follower count.
- A web container serves an interactive dashboard to visualize the data. 

The follower count is sampled every hour and stored in "data/followers.csv". A simple plotly dash web server is created to display the follower count for the last 30 days. 

### How to use

Install docker and docker compose. 

Create a file "worker/username.txt" with the username of the account you want to observe.

Run: 
`docker compose up -d --build`

This builds the images and runs them.
