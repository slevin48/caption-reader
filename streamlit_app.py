import streamlit as st
import pandas as pd
import webvtt
import time, datetime
# import io

f = st.file_uploader("Upload VTT file")
if f is not None:

    # To read file as bytes:
    # bytes_data = f.getvalue()
    # st.write(bytes_data)

    # To convert to a string based IO:
    # stringio = io.StringIO(f.getvalue().decode("utf-8"))
    # st.write(stringio)

    # To read file as string:
    # string_data = stringio.read()
    # st.write(string_data)

    # To read WebVTT format directly:
    # buffer = io.StringIO(string_data)
    # for caption in webvtt.read_buffer(buffer):
    #     st.write(caption.start)
    #     st.write(caption.end)
    #     st.write(caption.text)
    
    # Store as a dataframe: 
    # df = pd.DataFrame(columns=['start','text'])

    # buffer = io.StringIO(string_data)
    # for caption in webvtt.read_buffer(buffer):
    #     df2 = pd.DataFrame([[caption.start,caption.text]],columns=['start','text'])
    #     df.append(df2,ignore_index=True)
    #     # df
        
    
    with open("web.vtt","wb") as file: 
      file.write(f.getbuffer())

    vtt = webvtt.read('web.vtt')
    start = [v.start for v in vtt]
    end = [v.end for v in vtt]
    text = [v.text for v in vtt]

    df = pd.DataFrame(text,columns=['text'],index=pd.to_datetime(start))
    # st.table(df)


    t0 = time.strptime(vtt[0].start, "%H:%M:%S.%f")
    tf = time.strptime(vtt[-1].end, "%H:%M:%S.%f")
    i = st.slider("timestamp",step=datetime.timedelta(seconds=1),min_value=datetime.time(minute=t0.tm_min,second=t0.tm_sec),max_value=datetime.time(minute=tf.tm_min,second=tf.tm_sec),format = "mm:ss")
    # i = "00:01:20"
    dt = pd.to_datetime(i.strftime("%H:%M:%S.%f"))
    st.write(dt)
    st.write(df.text[df.index.get_loc(dt, method='nearest')])

