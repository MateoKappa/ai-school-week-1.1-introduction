from langchain_core.messages import AIMessage, HumanMessage,SystemMessage
from langchain_openai import ChatOpenAI

teacher = ChatOpenAI(temperature=0.95)
student = ChatOpenAI(temperature=0.95)


teacherMessages = [
    SystemMessage(
        content=""" 
            System Prompt: You are a teacher with extensive expertese in building CRUD applications and like to share different perspectives and techniques to maintain chat history effectively. Keep your answers short and concise.
        """
    ),
    HumanMessage(
        content="Hello i am Tim, how we can maintain chat history effectively?"
    ),
]

studentMessages = [
    SystemMessage(
        content=""" 
            System Prompt: You are a student called Tim with a basic understanding of building CRUD applications but has a lot of imagination and questions. Your answers are random and creative. Keep your answ
            ers short and concise. Try to act like a student who is curious and eager to learn. Only make questions
        """
    ),
    AIMessage(
        content="Hello i am Tim, how we can maintain chat history effectively?"
    ),
]

print('studentResult:','Hello i am Tim, how we can maintain chat history effectively?')

while True:
    teacherResult = teacher.invoke(teacherMessages).content 
    # add context on teacher 
    teacherMessages.append(AIMessage(content=teacherResult))
    print('teacherResult:',teacherResult)
    # add context on student 
    studentMessages.append(HumanMessage(content=teacherResult))
    
    # answer Student
    studentResult = student.invoke(studentMessages).content 
    # add context on teacher 
    teacherMessages.append(AIMessage(content=studentResult))
    # add context on student 
    studentMessages.append(HumanMessage(content=studentResult))
    print('studentResult:',studentResult)
    
   
