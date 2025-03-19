# Administration
## Tools
- Markdown, maybe obsidian
- KANBAN on GitHub with projects.
- AI tool for commit message generation and PR. I think that's important because its like getting feedback from another dev.

  
## General Procedure
- Create as simple as possible and deploy immediately. Aka work on all steps in parallel.
- MVP
  - is a homepage with a canvas, which can recognize a letter and store this letter with image and true label (if the user provides it)
  - This is great, because with that the projects is using all parts (backend/db, ml, frontend, ci/cd)
## Timetable 
- ==TODO create with gantt==

---
  
# Backend
==TODO DESIGN ME==
## Overview
## Requirements
## Architecture
## Tech Stack
## API Endpoints
### MVP APIs
### Full project APIs
## Security
## Testing
## Risk & Assumptions
## Conclusion

---

# Machine Learning
## Ideas
-  create a canvas where an user can draw, and then 1. recognize which they wrote and 2. create a image from that (eg given a word, create s cool signature). See [svelte tutorial for canvas]( https://svelte.dev/tutorial/svelte/actions)
-  create a NN visualization, i think thats cool to see.
-  start with a picture of myself which gets recognized from a ml model (eg short video) and which says 90% human or so and say you can trust me im 90% human lol
- Roman mentioned that it would be nice to have something like a doodle, and then AI generates an image from that. Maybe add a prompt as well.
-  show all parts of ML aka 1. predition with nn and letter recognizing, then generation (doodle to art), then innovation eg draw a arrow left/right to come to other pages or 1, 2, 3 to come to home about etc.
-  a llm chatbot which answers questions about me and mainly to get feedback from the user.
- Or for generation create a **cute dog/cat** generater and learn what people like more and show this to them (given gender, age, ..)
  
### Optional
-  something like finding fastest path in random world (and compare that with A*), or user draws obstacles and RL-agent must find way out.
  - Or an algo which doesn't predict optimal but the steps of a human (given a fixed env) 
-  visualization of other algos.

---

# Database
- PostgreSQL, because it's supported by SQLAlchemy, I have experience with it and its state of art / has proof of time.
- Full-text search and indexing might be great down the line as well.
- Not sure how to handle data from ML yet. **Ponder** can we store all data we need (image, text, ..) in postgres?
## Datbase Design
## Dataflow

---

# Frontend
I do think the most important part here is that it looks nice, testing and security since it's such a small site and im the sole contributor. Therefore the design document will not be as deep as for the backend.
## Tech Stack
- Svelte
- CSS / HTML
- TypeScript

## Security

## Testing

## Design
- Elias uses Fimga, Emre mentioned moqups.com and DrawIO are nice. What i have seen Penpot could be great as well.
- Check out [chat](https://www.notion.so/Active-Stuffses-473f9c31d1164d3c830e15c98ba69888?pvs=97#294ef8386774466ea2525b5383f4a5e2) and check other blogs/posts.
- Check out [svelt pages]( https://github.com/w3cj/svelte-5-tasks-app/tree/main) and other svelte based public projects for inspiration
- Check out [web of devs](https://webofdevs.com/ ) i like the design of https://raphaelameaume.com/ and https://antfu.me/ 
- Mby create a generative background, like in [chat](https://you.com/search?q=how+to+generate+background+as+in+https%3A%2F%2Fraphaelameaume.com%2Fde+and+https%3A%2F%2Fantfu.me%2F%0A%0Aso+eg+a+growing+tree%3F&fromSearchBar=true&tbm=youchat&chatMode=custom&cid=c0_009e6455-60e2-4e80-ae45-4066d81613c7) but obviously much more sufficicated.
- [dotbite](https://dotbite.at/de/webentwicklung?gad_source=1&gclid=Cj0KCQjw7dm-BhCoARIsALFk4v8FYDrB6D8BZ9lssPjSIksTTQ_vi5A3ktEbGsFJ_yLYo6QBjeGpmgMaAmViEALw_wcB) has a nice design as well.
- ==TODO add pictures of design==
### MVP Design
### Full Design
## Tabs
- Home
- About Me
- Machine Learning / AI
- This project (what i have learned, what my process was (learning in advance/best practices etc), storytelling here)
- More
  - Certificats / archivements
    - (mby) projects from udemy/lvs (game dev, ros/camera drones, ...),
    - (mby) also thing from leetcode etc, or build my own linked list / tree which is easy but maybe still cool for people to see.
    - Other proejcts which i will build in future like a smart mirror or so
  - Blog
  - Health stuff (area im as passionate about as computer science, things seem complex but actually quite straight forward eg food)
  - Great Sources (youtubers i like, stuff about health, cool books (eg Lean Startup, ..), ...)

---

# CI/CD
- Docker because state of the art.
- AWS because it has proof of consensus and should be great for future jobs since it's in demand.
- GitHub actions because most modern approach and makes sense over GitLab since GitHub is used more often for public repos.
- PR advanced flow as suggested from Bret Fisher (see my [docker repo](https://github.com/Steveineiter/docker-udemy/blob/main/CICD.png) for more).
