# stefan-schoerkmeier
My personal web page which showcases my skills as a fullstack developer. 

TODO add steps to run it locally. 

---

## Run it locally (Ubuntu)
### Backend 
1. cd into backend/app 
```bash
cd backend
```
2. create python virutal environment 
```bash
python –m venv <name_of_virtualenv>
```
3. activate envrionment 
```bash
. <name_of_virtualenv>/bin/activate
```
4. run app on uvicorn server 
```bash
 uvicorn app.main:app --reload --port=8000
```

### Machine learning (Ubuntu)
1. cd into machine_learning
```bash
cd machine_learning
```
2. create python virutal environment 
```bash
python –m venv <name_of_virtualenv>
```
3. activate envrionment 
```bash
. <name_of_virtualenv>/bin/activate
```
4. run app on uvicorn server 
```bash
 uvicorn app.main:app --reload --port=4242
```

### Frontend (Ubuntu)
1. cd into frontend
```bash
cd frontend
```
2. Install npm dependencies
```bash
npm install
```
3. start server
```bash
npm run dev -- --open
```

---

## Plan
1. ~~train model / make weights accessible~~
2. ~~create backend / ml model call and ml api~~
3. ~~create prediction via swagger-ui~~
4. implement frontend
5. everything should work on my machine xD
6. Create ci/cd pipeline, let in run locally on docker
7. Purchase schoerkmeier.dev domain and deploy on AWS


# Lessons learned
## AI in workflow
- Automatically creating git messages or pull requests is hard, since locally hosted my GPU is too weak (GTX 1070 (actually it doesnt work on GPU, maybe setup fucked since i dont have enough space on /)) and for other options i would need an API key
  - However for now I will simply use you.com and paste my code after im done for a file / milestone to get feedback.
  - For the commits, I will write them by hand for now, maybe using an api key later after i have set up the feedback-chatbot.
- LLMs are REALLY bad for new technology. GPT as well as sonnet 3.7 give me invalid syntax, often react specific stuff altough I include svelte specific imports etc in query. 

