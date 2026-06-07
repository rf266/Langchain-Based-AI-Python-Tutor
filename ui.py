import gradio as gr
import requests

def submission(text, prev): 
       print(f"gonna send {text} to the box")
       ans = requests.post("http://127.0.0.1:5000/submit", json={"text":text})
       ans = ans.text
       new = prev + "\n" + ans + "\n" 
       print(f"Added {text} to the box")
       return "",new

def startup():
      message = requests.get("http://127.0.0.1:5000/")
      return message.text

with gr.Blocks() as app:
    gr.Markdown("## **Python Tutoring AI Agent**")
    gr.Markdown("Answer questions, get feedback, get stronger!")
    
    out = gr.Textbox(lines=5, placeholder="Output", interactive=False)
    inp = gr.Textbox(lines=1, placeholder="Input")
    submit_b = gr.Button(value="Submit")
    app.load(fn=startup, inputs = None, outputs=out)
    submit_b.click(fn=submission, inputs=[inp, out], outputs=[inp,out])
    
    
app.launch()


    