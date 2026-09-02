# CS50 Network — Social Media Web App

<p>A full social networking platform built with Django, Python, HTML, CSS, and JavaScript as part of the CS50 Web Programming course.
Users can create posts, edit them, like posts, follow other users, and view a personalized feed of posts from people they follow.</p>

---
<p>

## Features

User Authentication

- Register, log in, and log out using Django’s built‑in authentication system.
</p>

---
<p>

Posts

- Create new text posts.
- View all posts on the main feed.
- Posts are displayed newest → oldest.
- Pagination ensures fast loading and clean navigation.

</p>

---
<p>

Editing Posts

- Users can edit their own posts.
- Editing happens inline using JavaScript (no page reload).
- Edit button disappears while editing.
- Only the original author can edit a post.

</p>

---
<p>

Likes

- Users can like or unlike any post.
- Like count updates instantly using JavaScript.
- Like data stored using a ManyToMany relationship.

</p>

---
<p>

Profiles

Each user has a profile page showing:
- Username
- Number of followers
- Number of users they follow
- All posts created by that user
- Follow/Unfollow button
- Pagination for profile posts
Only logged‑in users can follow or unfollow others.

</p>

---
<p>

Follow / Unfollow

- Users can follow other users.
- Follow/unfollow happens instantly using JavaScript.
- Follower count updates without reloading the page.

</p>

---
<p>

Following Feed

A dedicated page showing:
- Posts only from users you follow
- Ordered newest → oldest
- Paginated
This creates a personalized social feed similar to Twitter or Instagram.

</p>

---
<p>
Pagination

Implemented on:
- Main feed
- Profile pages
- Following feed
Uses Django’s Paginator class to display 10 posts per page.

</p>

---
<p>

Tech Stack

- Python / Django — backend, routing, models, authentication
- SQLite — database
- HTML / CSS / Bootstrap — layout and styling
- JavaScript — dynamic editing, liking, following
- Django Templates — rendering pages_

</p>


## Last Updated

<!-- TIMESTAMP_START -->
_Last updated: 2026-09-02 17:48 UTC_
<!-- TIMESTAMP_END -->
