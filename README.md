# AI Python Tutor  

This agent is an AI-powered coding tutor. It is designed to help users strengthen their conceptual and code understanding of Python by asking questions targeting specific topics. The workflow is structured, allowing a predictable process to help grasp key topics. 

Deployed link: https://learning-agent-production-5c6e.up.railway.app/

## Tech Stack
- Langchain agent orchestration
- SQLite database storage
- Pydantic Basemodel for schema design
- Gradio UI and server
- Railway deployment

*AI was used throughout the process, supporting ideation, system design, debugging etc. This was an especially important tool, used with thought, to allow me to navigate unfamiliar challenges especially where I have gaps in technical knowledge. Read ahead to find some cases where AI was pivotal in solving these challenges.*

## Functionality
Each topic is tested with five questions. The user has the chance to choose their own topic, or ask the LLM to suggest one, where the TOPICS table is searched to prevent any repetition. When the user answers the first question, feedback is provided to guide them to the correct answer. In the backend, a new record is created for the particular question, containing the response and feedback provided. When the question is reattempted, the new feedback and response is appended to the text already in the respective cells. 

An AI-suggested state dictionary is used to organise the workflow in the required order. This is updated based on the current stage of the workflow, and is also used as a kind of short term memory for the question and topic, ensuring that details are kept easy to access until the next question is asked. Additionally, another specific aspect where AI was used was in coming up with the correct logic for the workflow's progression on the UI - intially, while testing on the CLI, a while loop was used. However, when the submission button was created on the UI, I used AI assistance to help map out the logic for the next steps to be passed based on the current agent state. Additionally, the built in AI agent within Railway was useful in navigating port/URL hosting challenges, as well as the storage needs of a persistent database.

## Significant Decisions in Agent Development

### Agent creation 
The structure and functions of the different components of a Langchain agent were investigated. This was used instead of sending API calls to the LLM due to the presence of tool functions which could be used as required by the situation. The chosen LLM, after experimenting with responses and token size limitations, was Llama 4 Scout, obtained from Groq. However, after looking into advice from AI after resulting in multiple 'tool use failed' errors, the tool functionality was abandoned for normal function definitions, with appropriate prompt templates to manually preserve context. 

### Tool Development
One of the most significant challenges was seen in tool development, where, after research and AI consultation, it was found that the LLM must be explicitly shown the tools it can use to operate as desired. The uncertainty created by missing information causes the model to behave unpredictably, where I even found that it was creating its own functions, as well as generating its own SQL queries. Hence, following online and AI research, **this is currently not being used.**.

Another important consideration was the level of detail to be provided in tool docstrings. It was often the case that the lengthy docstrings would override token limitations, especially in the earlier LLMs tested. I learnt how to ensure that the LLM has complete knowledge of the full interactions it can have with the tool. 

The system prompt was also one of concern, where it was found that a detailed prompt was required to outline all use cases and prevent uncertainties for the model. It deeply outlined a typical agent workflow, database schema and style of interaction. 

### SQLite database
A database was created to store the topics and questions posed to the user, as part of a tracking system to allow the agent to analyse how the questions were answered. 

The database schema is below:
TOPICS(TopicID, Topic, Understood)
QUESTIONS(QID, TopicID, Question, Response, Feedback, Attempts)

A one to many relationship is demonstrated - one topic can have many questions, but one question can have one topic. 

### Gradio UI and Flask Involvement
Gradio was used for the UI due to it being Python-native, allowing fast prototyping. Initially, Flask was set as the backend service for messages being sent to and from the Langchain functions. However, due to the unnecessary complexity added by Flask, I resorted to using the built in Gradio hosting server. The Flask addition came to involve added layers to stream communication between the user and the tutor, where it didn't really serve as a value add, given that Gradio also has its own server capabilities. I realised that even though it is important to experiment with different frameworks, adding complexity to a task which may be executed in a simpler manner was not ideal. 

### Python generator functions 
One important issue I kept facing when combining the backend and the frontend was the role of the 'submit' button on the UI. Events were not being triggered sequentially with one click of the button, due to the return statements in the submission function. I was then introduced to the 'yield' term, which allows a function to continue where it left off earlier. I was then able to use AI to group together the two key functions, getting a topic/question and receiving feedback from the submitted answer, to ensure the flow looks natural.

## Evaluation
Several key additions and future developments could allow the tutor's functionality to expand, serving to become more informative for users. For example, long term analytics was suggested by AI as one interesting addition. Tutees could be given the ability to track their progress over topics, seeing where their strengths and weaknesses lie. Topics suggestions could also be tailored to this data - it could suggest topics which are close to ones the user has already struggled with, which would build greater depth and understanding. Langchain's tool abilities would make more sense over here, where, at periodic moments, it could query the database to provide an insight/summary. 

Additionally, the UI could benefit from a significant improvement in intuitiveness, as well as the functionality of textboxes, which could perhaps be replaced with the Gradio chatbot template for a more natural looking tutor. 

Additional functions to have a conversation agent state could be interesting, where moving beyond the Q and A would allow users to discuss more general aspects of their learning journey with the tutor, which could perhaps be supported by data from the database to provide context. 

Greater support for edge cases, where the input sequence performed differently may cause the tutor to crash, and validation of inputs could provide a smoother user experience, making it feel more natural. Additionally, this could be supported by cautions like rate limiting, to prevent the HTTP Too Many Requests error from arising. 

Moreover, the correction of responses runs solely on the discretion of the LLM. Although efforts have been made to provide a clear system prompt for how the response is to be marked, we cannot avoid the fact that LLMs are probabilistic. They may output a response which does not necessarily appreciate the understanding the user has implied in their response. It may think that the response is lacking, or even incorrect, even though a conceptual understanding has been demonstrated to the human eye. 

Currently, the deployed container involves one database. This means that if the link was distributed to multiple users, they would all fill up the same instance of this database. For better scalability, accommodating more users and providing them with their own setup, through auth and login, would allow them to revisit their own progress, rather than the conflicted version which will arise in the current manner. This expansion would involve choosing plans beyond the free tier with both Railway and Groq as the LLM provider. 

## Sources - non exhaustive 

AI was used throughout the process, supporting ideation, system design, debugging etc. This was an especially important tool, used with thought, to allow me to navigate through unfamiliar challenges. Rather than taking its suggestions blindly, I tried to understand how and why it would fit into my code. It was also significant whilst making decisions regarding rethinking architecture where the workflow did not work as expected. Suggested solutions were implemented with a careful eye. 

One of the main challenges was navigating outdated documentation/fixes, even if published recently. Langchain grows at a rapid rate, and updates are done to the package quite frequently, which are not all reflected. This is another reason why AI was used, to guide me through a process of finding a working solution. 

By looking at forums, I was able to understand how to better structure my code, especially docstrings, which are the fundamental instructions for the LLM's tool orchestration. 

### Documentation 
- Langchain
- Groq-Langchain
- SQLite - Python docs
- HuggingFace - model information 
- Gradio 
- Flask
- Requests

### Help/research 
- https://www.youtube.com/watch?v=jsX99U8UkOo - SQLite DB Creation 

- https://www.w3schools.com/sql/sql_datatypes.asp - SQL Datatypes

- https://www.youtube.com/watch?v=eD2oAsalw7E - SQLite DB table creation 

- https://www.youtube.com/watch?v=YqvCfS6sv7k - SQLite insertion statements

- https://stackoverflow.com/questions/29076312/inserting-sqlite-primary-key-in-python - Primary key 

- https://www.ibm.com/think/topics/llm-temperature#:~:text=Temperature%20controls%20the%20randomness%20of,according%20to%20a%20probability%20distribution. - model temperature

- https://www.reddit.com/r/LangChain/comments/1k0adul/custom_tools_with_multiple_parameters/ - tool parameters and docstring structure

- https://www.reddit.com/r/LangChain/comments/1kfifju/is_it_possible_to_do_tool_calling_sql_with/ - Langchain tool calling 

- https://github.com/langchain-ai/langchain-aws/issues/524 snake case

- https://www.reddit.com/r/LocalLLaMA/comments/13nm96l/models_are_repeating_text_several_times/ - repeated words generated 

- https://www.arsturn.com/blog/langchain-llm-returning-empty-results-common-fixes - empty outputs

- https://www.youtube.com/watch?v=vzJOAnwIokM - Langchain overview

- https://medium.com/data-and-beyond/output-parsers-in-langchain-b2e0db20880f -  output parsers

- https://www.youtube.com/watch?v=v9G-h6Ygokk - LCEL operator

- https://stackoverflow.com/questions/5191503/how-to-select-the-last-record-of-a-table-in-sql - Latest entry in DB

- https://www.youtube.com/watch?v=Hyo9rIuYlFc&t=40s - DB extraction statement

- https://stackoverflow.com/questions/4397757/how-can-i-check-to-see-if-my-sqlite-table-has-data-in-it - check if tables are empty 

- https://www.w3schools.com/Python/python_try_except.asp - Try except statement

- https://stackoverflow.com/questions/10588317/python-function-global-variables - Global variable manipulation

- https://medium.com/@danaasa/building-a-chatbot-with-gradio-a-practical-guide-06986342ef07 - Gradio chatbot

- https://ihitsuperhuman.medium.com/deploy-your-first-ml-app-using-gradio-1684eec7eb5f - Gradio textbox

- https://flask-cors.readthedocs.io/en/latest/ - CORS

- https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world - Flask 

- https://www.geeksforgeeks.org/python/python-flask-request-object/ - Flask request object

- https://stackoverflow.com/questions/393554/python-sqlite3-and-concurrency - Python concurrency

- https://medium.com/@alfininfo/flask-tutorial-implementing-server-sent-events-sse-for-real-time-updates-60103cd89fbf - SSE

- https://www.geeksforgeeks.org/python/python-yield-keyword/ - yield keyword

#### Stack overflow questions I posted

- https://stackoverflow.com/questions/79907528/why-does-groq-langchain-model-return-tool-use-failed-error/79907609#79907609

- https://stackoverflow.com/questions/79910632/langchain-tool-does-not-implement-database-record-addition?r=2

- https://stackoverflow.com/questions/79915713/langchain-agent-state-preservation?r=2

- https://ai.stackexchange.com/questions/50494/langchain-agent-state-preservation

- https://stackoverflow.com/questions/79951889/flask-backend-and-gradio-ui-error-500-function-missing-1-positional-argument

- https://stackoverflow.com/questions/79952563/flask-app-sqlite3-objects-created-in-one-thread-cannot-be-used-in-another/79952632#79952632
