from fastapi import FastAPI, Query
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_google_genai import ChatGoogleGenerativeAI

app = FastAPI()

@app.get("/text")
def generate_text(prompt: str = Query(..., title="Prompt", description="Input prompt for text generation")):
    apiKey = "AIzaSyB3bz7fGcytKTUVRgSD7LQTgSNpiPxgqr0"

    llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=apiKey)
    # memory = ConversationBufferMemory()
    # conversation = ConversationChain(
    #     llm=llm,
    #     memory=memory,
    #     verbose=False
    # )
    #text_output = conversation.predict(prompt)
    # conversation_buf = ConversationChain(
    #     llm=llm,
    #     memory=ConversationBufferMemory()
    # )
    text_output = llm.invoke(prompt)
    # for chunk in llm.stream(prompt):
    #     text_output = chunk.content
    # response = conversation_buf(prompt)

    return {"text_output": text_output.content}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
