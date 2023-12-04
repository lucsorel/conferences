import random

# import altair as alt
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
from bokeh.plotting import figure
# from vega_datasets import data
from datetime import datetime, time, date
from time import sleep

st.set_page_config(initial_sidebar_state="collapsed")

########## TEXT ELEMENTS ##########

st.header('✏️:blue[TEXT ELEMENTS]', divider="blue")
st.subheader('st.write')
st.write('Hello *World!* :sunglasses: This is st.write command')

st.divider()
st.subheader('st.markdown')
st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors].''')
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = '''If you end a line with two spaces,
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)

st.divider()
st.subheader('st.title')
st.title('_Streamlit_ is :blue[cool] :sunglasses:')

st.divider()
st.subheader('st.header')
st.header('This is a header with a divider', divider='rainbow')
st.header('_Streamlit_ is :blue[cool] :sunglasses:')

st.divider()
st.subheader('st.subheader')
st.subheader('This is a subheader with a divider', divider='rainbow')
st.subheader('_Streamlit_ is :blue[cool] :sunglasses:')

st.divider()
st.subheader('st.caption')
st.caption('This is a string that explains something above.')
st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')

st.divider()
st.subheader('st.code')
code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')

st.divider()
st.subheader('st.text')
st.text('This is some text.')

st.divider()
st.subheader('st.latex')
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

st.divider()
st.subheader('st.divider')
st.divider()  # 👈 Draws a horizontal rule
st.write("This text is between the horizontal rules.")
st.divider()  # 👈 Another horizontal rule

########### DATA ELEMENTS ##########

st.header('🔢️:blue[DATA ELEMENTS]', divider="blue")
st.subheader('st.dataframe')
df = pd.DataFrame(
    {
        "name": ["Roadmap", "Extras", "Issues"],
        "url": ["https://roadmap.streamlit.app", "https://extras.streamlit.app", "https://issues.streamlit.app"],
        "stars": [random.randint(0, 1000) for _ in range(3)],
        "views_history": [[random.randint(0, 5000) for _ in range(30)] for _ in range(3)],
    }
)
st.dataframe(
    df,
    column_config={
        "name": "App name",
        "stars": st.column_config.NumberColumn(
            "Github Stars",
            help="Number of stars on GitHub",
            format="%d ⭐",
        ),
        "url": st.column_config.LinkColumn("App URL"),
        "views_history": st.column_config.LineChartColumn(
            "Views (past 30 days)", y_min=0, y_max=5000
        ),
    },
    hide_index=True,
)

st.divider()
st.subheader('st.data_editor')
df = pd.DataFrame(
    [
        {"command": "st.selectbox", "rating": 4, "is_widget": True},
        {"command": "st.balloons", "rating": 5, "is_widget": False},
        {"command": "st.time_input", "rating": 3, "is_widget": True},
    ]
)
edited_df = st.data_editor(df)

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")

st.divider()
st.subheader('st.table')
df = pd.DataFrame(np.random.randn(10, 5), columns=("col %d" % i for i in range(5)))
st.table(df)

st.divider()
st.subheader('st.metric')
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

st.divider()
st.subheader('st.json')
st.json({
    'foo': 'bar',
    'baz': 'boz',
    'stuff': [
        'stuff 1',
        'stuff 2',
        'stuff 3',
        'stuff 4',
    ],
})

########## INPUT WIDGETS ##########

st.header('🫵:blue[INPUT WIDGETS]', divider="blue")
st.subheader('st.button')
if st.button('Say hello', type='primary'):
    st.write('Hello 🤟')
else:
    st.write('😞')

st.divider()
st.subheader('st.download_button')
text_contents = '''This is some text'''
st.download_button('Download some text', text_contents)

st.divider()
st.subheader('st.link_button')
st.link_button("Go to gallery", "https://streamlit.io/gallery")

st.divider()
st.subheader('st.checkbox')
agree = st.checkbox('I agree')
if agree:
    st.write('Great!')

st.divider()
st.subheader('st.toggle')
on = st.toggle('Activate feature')
if on:
    st.write('Feature activated!')

st.divider()
st.subheader('st.radio')
genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    index=None,
)
st.write("You selected:", genre)

st.divider()
st.subheader('st.selectbox')
option = st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone"),
    index=None,
    placeholder="Select contact method...",
)
st.write('You selected:', option)

st.divider()
st.subheader('st.multiselect')
options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])
st.write('You selected:', options)

st.divider()
st.subheader('st.slider')
age = st.slider('How old are you?', 0, 130, 28)
st.write("I'm ", age, ' years old')

values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

appointment = st.slider(
    "Schedule your appointment:",
    value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

start_time = st.slider(
    "When do you start?",
    value=datetime(2020, 1, 1, 9, 30),
    format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)

st.divider()
st.subheader('st.select_slider')
color = st.select_slider(
    'Select a color of the rainbow',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
st.write('My favorite color is', color)

st.divider()
st.subheader('st.text_input')
username = st.text_input('Username', )
password = st.text_input('Password', type='password')
st.write(username, ' - ', password)

st.divider()
st.subheader('st.number_input')
number = st.number_input('Insert a number')
st.write('The current number is ', number)

st.divider()
st.subheader('st.text_area')
txt = st.text_area(
    "Text to analyze",
    "It was the best of times, it was the worst of times, it was the age of "
    "wisdom, it was the age of foolishness, it was the epoch of belief, it "
    "was the epoch of incredulity, it was the season of Light, it was the "
    "season of Darkness, it was the spring of hope, it was the winter of "
    "despair, (...)",
)
st.write(f'You wrote {len(txt)} characters.')

st.divider()
st.subheader('st.date_input')
d = st.date_input("Votre date de naissance", date(1995, 1, 1))

aujourd_hui = date.today()
prochain_anniversaire = date(aujourd_hui.year, d.month, d.day)
if aujourd_hui > prochain_anniversaire:
    prochain_anniversaire = date(aujourd_hui.year + 1, d.month, d.day)
nb_jours = (prochain_anniversaire - aujourd_hui).days

st.write(f'Plus que {nb_jours} jours avant votre anniversaire !')

st.divider()
st.subheader('st.time_input')
t = st.time_input('Set an alarm for', time(8, 45))
st.write('Alarm is set for', t)

st.divider()
st.subheader('st.file_uploader')
uploaded_files = st.file_uploader("Choose a file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)

st.divider()
st.subheader('st.camera_input')
picture = st.camera_input("Take a picture")
if picture:
    st.image(picture)

st.divider()
st.subheader('st.color_picker')
color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)


########## MEDIA ELEMENTS ##########

st.header('📷:blue[MEDIA ELEMENTS]', divider="blue")
st.subheader('st.image')
st.image("https://static.actu.fr/uploads/2022/10/fepr1j0x0ausfd3.jpg", caption='Erminig et un canari', width=500)

st.divider()
st.subheader('st.audio')
sample_rate = 44100  # 44100 samples per second
seconds = 5  # Note duration of 2 seconds
frequency_la = 440  # Our played note will be 440 Hz
# Generate array with seconds*sample_rate steps, ranging between 0 and seconds
t = np.linspace(0, seconds, seconds * sample_rate, False)
# Generate a 440 Hz sine wave
note_la = np.sin(frequency_la * t * 2 * np.pi)

st.audio(note_la, sample_rate=sample_rate)

st.divider()
st.subheader('st.video')
# video_file = open('koubek.mp4', 'rb')
# video_bytes = video_file.read()
# st.video(video_bytes)


########## LAYOUTS AND CONTAINERS ##########

st.header('📦:blue[LAYOUTS AND CONTAINERS]', divider="blue")
st.subheader('st.sidebar')
with st.sidebar:
    st.title('Je suis la magnifique sidebar')

st.divider()
st.subheader('st.columns')
col1, col2, col3 = st.columns(3)
with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")
with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")
with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")

st.divider()
st.subheader('st.tabs')
tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])
with tab1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

st.divider()
st.subheader('st.expander')
with st.expander(":red[Moi, au boulot...]"):
    st.image("https://ih1.redbubble.net/image.1980770122.1726/flat,750x,075,f-pad,750x1000,f8f8f8.jpg", width=500)


########## CHAT ELEMENTS ##########

st.header('💬:blue[CHAT ELEMENTS]', divider="blue")
st.subheader('st.chat_message')
with st.chat_message("user"):
    st.write("Hello 👋")
message = st.chat_message("assistant")
message.write("Hello human")
with st.chat_message("user"):
    st.write("C'est bien chatGPT ?")

st.divider()
st.subheader('st.chat_input')
display_chat_input = st.checkbox("Afficher st.chat_input")
if display_chat_input:
    prompt = st.chat_input("Say something")
    if prompt:
        st.write(f"User has sent the following prompt: {prompt}")


########## STATUS ELEMENTS ##########

st.header('🎈:blue[STATUS ELEMENTS]', divider="blue")
st.subheader('st.progress')
if st.button('st.progress'):
    progress_text = "Operation in progress. Please wait."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        sleep(0.02)
        my_bar.progress(percent_complete + 1, text=progress_text)
    sleep(1)
    my_bar.empty()

st.divider()
st.subheader('st.spinner')
if st.button('st.spinner'):
    with st.spinner('Wait for it...'):
        sleep(5)
    st.success('Done!')

st.divider()
st.subheader('st.status')
if st.button('st.status'):
    with st.status("Downloading data...", expanded=True) as status:
        st.write("Searching for data...")
        sleep(2)
        st.write("Found URL.")
        sleep(1)
        st.write("Downloading data...")
        sleep(1)
        status.update(label="Download complete!", state="complete", expanded=False)

st.divider()
st.subheader('st.toast')
if st.button('Three cheers'):
    st.toast('Hip!')
    sleep(.5)
    st.toast('Hip!')
    sleep(.5)
    st.toast('Hooray!', icon='🎉')

st.divider()
st.subheader('st.balloons')
if st.button('st.balloons'):
    st.balloons()

st.divider()
st.subheader('st.snow')
if st.button('st.snow'):
    st.snow()

st.divider()
st.subheader('st.error')
st.error('This is an error', icon="🚨")


st.divider()
st.subheader('st.warning')
st.warning('This is a warning', icon="⚠️")


st.divider()
st.subheader('st.info')
st.info('This is a purely informational message', icon="ℹ️")


st.divider()
st.subheader('st.success')
st.success('This is a success message!', icon="✅")


st.divider()
st.subheader('st.exception')
e = RuntimeError('This is an exception of type RuntimeError')
st.exception(e)

########## CHART ELEMENTS ##########

st.header('📊:blue[CHART ELEMENTS]', divider="blue")
st.subheader('st.area_chart')
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.area_chart(chart_data, color=['#ffaa00', '#aa00ff', '#00ffaa'])

st.divider()
st.subheader('st.bar_chart')
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.bar_chart(chart_data)

st.divider()
st.subheader('st.line_chart')
st.line_chart(chart_data)

st.divider()
st.subheader('st.scatter_chart')
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["col1", "col2", "col3"])
chart_data['col4'] = np.random.choice(['A', 'B', 'C'], 20)
st.scatter_chart(
    chart_data,
    x='col1',
    y='col2',
    color='col4',
    size='col3',
)

st.divider()
st.subheader('st.pyplot')
arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)
st.pyplot(fig)

# st.divider()
# st.subheader('st.altair_chart')
# source = data.seattle_weather()
#
# scale = alt.Scale(
#     domain=["sun", "fog", "drizzle", "rain", "snow"],
#     range=["#e7ba52", "#a7a7a7", "#aec7e8", "#1f77b4", "#9467bd"],
# )
# color = alt.Color("weather:N", scale=scale)
#
# # We create two selections:
# # - a brush that is active on the top panel
# # - a multi-click that is active on the bottom panel
# brush = alt.selection_interval(encodings=["x"])
# click = alt.selection_multi(encodings=["color"])
#
# # Top panel is scatter plot of temperature vs time
# points = (
#     alt.Chart()
#     .mark_point()
#     .encode(
#         alt.X("monthdate(date):T", title="Date"),
#         alt.Y(
#             "temp_max:Q",
#             title="Maximum Daily Temperature (C)",
#             scale=alt.Scale(domain=[-5, 40]),
#         ),
#         color=alt.condition(brush, color, alt.value("lightgray")),
#         size=alt.Size("precipitation:Q", scale=alt.Scale(range=[5, 200])),
#     )
#     .properties(width=550, height=300)
#     .add_selection(brush)
#     .transform_filter(click)
# )
#
# # Bottom panel is a bar chart of weather type
# bars = (
#     alt.Chart()
#     .mark_bar()
#     .encode(
#         x="count()",
#         y="weather:N",
#         color=alt.condition(click, color, alt.value("lightgray")),
#     )
#     .transform_filter(brush)
#     .properties(
#         width=550,
#     )
#     .add_selection(click)
# )
#
# chart = alt.vconcat(points, bars, data=source, title="Seattle Weather: 2012-2015")
#
# tab1, tab2 = st.tabs(["Streamlit theme (default)", "Altair native theme"])
#
# with tab1:
#     st.altair_chart(chart, theme="streamlit", use_container_width=True)
# with tab2:
#     st.altair_chart(chart, theme=None, use_container_width=True)
#
st.divider()
st.subheader('st.plotly_chart')
df = px.data.iris()
fig = px.scatter(
    df,
    x="sepal_width",
    y="sepal_length",
    color="sepal_length",
    color_continuous_scale="reds",
)

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
with tab1:
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
with tab2:
    st.plotly_chart(fig, theme=None, use_container_width=True)

st.divider()
st.subheader('st.bokeh_chart')
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]
p = figure(
    title='simple line example',
    x_axis_label='x',
    y_axis_label='y')
p.line(x, y, legend_label='Trend', line_width=2)
st.bokeh_chart(p, use_container_width=True)

st.divider()
st.subheader('st.graphviz_chart')
st.graphviz_chart('''
    digraph {
        run -> intr
        intr -> runbl
        runbl -> run
        run -> kernel
        kernel -> zombie
        kernel -> sleep
        kernel -> runmem
        sleep -> swap
        swap -> runswap
        runswap -> new
        runswap -> runmem
        new -> runmem
        sleep -> runmem
    }
''')

st.divider()
st.subheader('st.map')
df = pd.DataFrame({
    "lat": [48.0876499, 48.1132164, 48.1066049],
    "lon": [-1.6215477, -1.6611461, -1.6936411],
    "color": ['#0044ff', '#ff44ff', '#0044ff']
})
st.map(df, color='color', size=50, zoom=11)


st.divider()
with st.expander("Code source de l'application"):
    st.code('''
    import random
    
    # import altair as alt
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    import plotly.express as px
    import streamlit as st
    from bokeh.plotting import figure
    # from vega_datasets import data
    from datetime import datetime, time, date
    from time import sleep
    
    st.set_page_config(initial_sidebar_state="collapsed")
    
    ########## TEXT ELEMENTS ##########
    
    st.header('✏️:blue[TEXT ELEMENTS]', divider="blue")
    st.subheader('st.text')
    st.write('Hello *World!* :sunglasses: This is st.write command')
    
    st.divider()
    st.subheader('st.markdown')
    st.markdown("*Streamlit* is **really** ***cool***.")
    st.markdown("Here's a bouquet &mdash;\
                :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
    
    multi = """If you end a line with two spaces,
    a soft return is used for the next line.
    
    Two (or more) newline characters in a row will result in a hard return.
    """
    st.markdown(multi)
    
    st.divider()
    st.subheader('st.title')
    st.title('_Streamlit_ is :blue[cool] :sunglasses:')
    
    st.divider()
    st.subheader('st.header')
    st.header('This is a header with a divider', divider='rainbow')
    st.header('_Streamlit_ is :blue[cool] :sunglasses:')
    
    st.divider()
    st.subheader('st.subheader')
    st.subheader('This is a subheader with a divider', divider='rainbow')
    st.subheader('_Streamlit_ is :blue[cool] :sunglasses:')
    
    st.divider()
    st.subheader('st.caption')
    st.caption('This is a string that explains something above.')
    st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')
    
    st.divider()
    st.subheader('st.code')
    code = """def hello():
        print("Hello, Streamlit!")"""
    st.code(code, language='python')
    
    st.divider()
    st.subheader('st.text')
    st.text('This is some text.')
    
    st.divider()
    st.subheader('st.latex')
    st.latex(r"""
        a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
        \sum_{k=0}^{n-1} ar^k =
        a \left(\frac{1-r^{n}}{1-r}\right)
        """)
    
    st.divider()
    st.subheader('st.divider')
    st.divider()  # 👈 Draws a horizontal rule
    st.write("This text is between the horizontal rules.")
    st.divider()  # 👈 Another horizontal rule
    
    ########### DATA ELEMENTS ##########
    
    st.header('🔢️:blue[DATA ELEMENTS]', divider="blue")
    st.subheader('st.dataframe')
    df = pd.DataFrame(
        {
            "name": ["Roadmap", "Extras", "Issues"],
            "url": ["https://roadmap.streamlit.app", "https://extras.streamlit.app", "https://issues.streamlit.app"],
            "stars": [random.randint(0, 1000) for _ in range(3)],
            "views_history": [[random.randint(0, 5000) for _ in range(30)] for _ in range(3)],
        }
    )
    st.dataframe(
        df,
        column_config={
            "name": "App name",
            "stars": st.column_config.NumberColumn(
                "Github Stars",
                help="Number of stars on GitHub",
                format="%d ⭐",
            ),
            "url": st.column_config.LinkColumn("App URL"),
            "views_history": st.column_config.LineChartColumn(
                "Views (past 30 days)", y_min=0, y_max=5000
            ),
        },
        hide_index=True,
    )
    
    st.divider()
    st.subheader('st.data_editor')
    df = pd.DataFrame(
        [
            {"command": "st.selectbox", "rating": 4, "is_widget": True},
            {"command": "st.balloons", "rating": 5, "is_widget": False},
            {"command": "st.time_input", "rating": 3, "is_widget": True},
        ]
    )
    edited_df = st.data_editor(df)
    
    favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
    st.markdown(f"Your favorite command is **{favorite_command}** 🎈")
    
    st.divider()
    st.subheader('st.table')
    df = pd.DataFrame(np.random.randn(10, 5), columns=("col %d" % i for i in range(5)))
    st.table(df)
    
    st.divider()
    st.subheader('st.metric')
    col1, col2, col3 = st.columns(3)
    col1.metric("Temperature", "70 °F", "1.2 °F")
    col2.metric("Wind", "9 mph", "-8%")
    col3.metric("Humidity", "86%", "4%")
    
    st.divider()
    st.subheader('st.json')
    st.json({
        'foo': 'bar',
        'baz': 'boz',
        'stuff': [
            'stuff 1',
            'stuff 2',
            'stuff 3',
            'stuff 4',
        ],
    })
    
    ########## INPUT WIDGETS ##########
    
    st.header('🫵:blue[INPUT WIDGETS]', divider="blue")
    st.subheader('st.button')
    if st.button('Say hello', type='primary'):
        st.write('Hello 🤟')
    else:
        st.write('😞')
    
    st.divider()
    st.subheader('st.download_button')
    text_contents = 'This is some text'
    st.download_button('Download some text', text_contents)
    
    st.divider()
    st.subheader('st.link_button')
    st.link_button("Go to gallery", "https://streamlit.io/gallery")
    
    st.divider()
    st.subheader('st.checkbox')
    agree = st.checkbox('I agree')
    if agree:
        st.write('Great!')
    
    st.divider()
    st.subheader('st.toggle')
    on = st.toggle('Activate feature')
    if on:
        st.write('Feature activated!')
    
    st.divider()
    st.subheader('st.radio')
    genre = st.radio(
        "What's your favorite movie genre",
        [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
        index=None,
    )
    st.write("You selected:", genre)
    
    st.divider()
    st.subheader('st.selectbox')
    option = st.selectbox(
        "How would you like to be contacted?",
        ("Email", "Home phone", "Mobile phone"),
        index=None,
        placeholder="Select contact method...",
    )
    st.write('You selected:', option)
    
    st.divider()
    st.subheader('st.multiselect')
    options = st.multiselect(
        'What are your favorite colors',
        ['Green', 'Yellow', 'Red', 'Blue'],
        ['Yellow', 'Red'])
    st.write('You selected:', options)
    
    st.divider()
    st.subheader('st.slider')
    age = st.slider('How old are you?', 0, 130, 28)
    st.write("I'm ", age, ' years old')
    
    values = st.slider(
        'Select a range of values',
        0.0, 100.0, (25.0, 75.0))
    st.write('Values:', values)
    
    appointment = st.slider(
        "Schedule your appointment:",
        value=(time(11, 30), time(12, 45)))
    st.write("You're scheduled for:", appointment)
    
    start_time = st.slider(
        "When do you start?",
        value=datetime(2020, 1, 1, 9, 30),
        format="MM/DD/YY - hh:mm")
    st.write("Start time:", start_time)
    
    st.divider()
    st.subheader('st.select_slider')
    color = st.select_slider(
        'Select a color of the rainbow',
        options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
    st.write('My favorite color is', color)
    
    st.divider()
    st.subheader('st.text_input')
    username = st.text_input('Username', )
    password = st.text_input('Password', type='password')
    st.write(username, ' - ', password)
    
    st.divider()
    st.subheader('st.number_input')
    number = st.number_input('Insert a number')
    st.write('The current number is ', number)
    
    st.divider()
    st.subheader('st.text_area')
    txt = st.text_area(
        "Text to analyze",
        "It was the best of times, it was the worst of times, it was the age of "
        "wisdom, it was the age of foolishness, it was the epoch of belief, it "
        "was the epoch of incredulity, it was the season of Light, it was the "
        "season of Darkness, it was the spring of hope, it was the winter of "
        "despair, (...)",
    )
    st.write(f'You wrote {len(txt)} characters.')
    
    st.divider()
    st.subheader('st.date_input')
    d = st.date_input("Votre date de naissance", date(1995, 1, 1))
    
    aujourd_hui = date.today()
    prochain_anniversaire = date(aujourd_hui.year, d.month, d.day)
    if aujourd_hui > prochain_anniversaire:
        prochain_anniversaire = date(aujourd_hui.year + 1, d.month, d.day)
    nb_jours = (prochain_anniversaire - aujourd_hui).days
    
    st.write(f'Plus que {nb_jours} jours avant votre anniversaire !')
    
    st.divider()
    st.subheader('st.time_input')
    t = st.time_input('Set an alarm for', time(8, 45))
    st.write('Alarm is set for', t)
    
    st.divider()
    st.subheader('st.file_uploader')
    uploaded_files = st.file_uploader("Choose a file", accept_multiple_files=True)
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        st.write("filename:", uploaded_file.name)
        st.write(bytes_data)
    
    st.divider()
    st.subheader('st.camera_input')
    picture = st.camera_input("Take a picture")
    if picture:
        st.image(picture)
    
    st.divider()
    st.subheader('st.color_picker')
    color = st.color_picker('Pick A Color', '#00f900')
    st.write('The current color is', color)
    
    
    ########## MEDIA ELEMENTS ##########
    
    st.header('📷:blue[MEDIA ELEMENTS]', divider="blue")
    st.subheader('st.image')
    st.image("https://static.actu.fr/uploads/2022/10/fepr1j0x0ausfd3.jpg", caption='Erminig et un canari', width=500)
    
    st.divider()
    st.subheader('st.audio')
    sample_rate = 44100  # 44100 samples per second
    seconds = 5  # Note duration of 2 seconds
    frequency_la = 440  # Our played note will be 440 Hz
    # Generate array with seconds*sample_rate steps, ranging between 0 and seconds
    t = np.linspace(0, seconds, seconds * sample_rate, False)
    # Generate a 440 Hz sine wave
    note_la = np.sin(frequency_la * t * 2 * np.pi)
    
    st.audio(note_la, sample_rate=sample_rate)
    
    st.divider()
    st.subheader('st.video')
    video_file = open('koubek.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    
    
    ########## LAYOUTS AND CONTAINERS ##########
    
    st.header('📦:blue[LAYOUTS AND CONTAINERS]', divider="blue")
    st.subheader('st.sidebar')
    with st.sidebar:
        st.title('Je suis la magnifique sidebar')
    
    st.divider()
    st.subheader('st.columns')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("A cat")
        st.image("https://static.streamlit.io/examples/cat.jpg")
    with col2:
        st.header("A dog")
        st.image("https://static.streamlit.io/examples/dog.jpg")
    with col3:
        st.header("An owl")
        st.image("https://static.streamlit.io/examples/owl.jpg")
    
    st.divider()
    st.subheader('st.tabs')
    tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])
    with tab1:
        st.header("A cat")
        st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
    with tab2:
        st.header("A dog")
        st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
    with tab3:
        st.header("An owl")
        st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
    
    st.divider()
    st.subheader('st.expander')
    with st.expander(":red[Moi, au boulot...]"):
        st.image("https://ih1.redbubble.net/image.1980770122.1726/flat,750x,075,f-pad,750x1000,f8f8f8.jpg", width=500)
    
    
    ########## CHAT ELEMENTS ##########
    
    st.header('💬:blue[CHAT ELEMENTS]', divider="blue")
    st.subheader('st.chat_message')
    with st.chat_message("user"):
        st.write("Hello 👋")
    message = st.chat_message("assistant")
    message.write("Hello human")
    with st.chat_message("user"):
        st.write("C'est bien chatGPT ?")
    
    st.divider()
    st.subheader('st.chat_input')
    display_chat_input = st.checkbox("Afficher st.chat_input")
    if display_chat_input:
        prompt = st.chat_input("Say something")
        if prompt:
            st.write(f"User has sent the following prompt: {prompt}")
    
    
    ########## STATUS ELEMENTS ##########
    
    st.header('🎈:blue[STATUS ELEMENTS]', divider="blue")
    st.subheader('st.progress')
    if st.button('st.progress'):
        progress_text = "Operation in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)
    
        for percent_complete in range(100):
            sleep(0.02)
            my_bar.progress(percent_complete + 1, text=progress_text)
        sleep(1)
        my_bar.empty()
    
    st.divider()
    st.subheader('st.spinner')
    if st.button('st.spinner'):
        with st.spinner('Wait for it...'):
            sleep(5)
        st.success('Done!')
    
    st.divider()
    st.subheader('st.status')
    if st.button('st.status'):
        with st.status("Downloading data...", expanded=True) as status:
            st.write("Searching for data...")
            sleep(2)
            st.write("Found URL.")
            sleep(1)
            st.write("Downloading data...")
            sleep(1)
            status.update(label="Download complete!", state="complete", expanded=False)
    
    st.divider()
    st.subheader('st.toast')
    if st.button('Three cheers'):
        st.toast('Hip!')
        sleep(.5)
        st.toast('Hip!')
        sleep(.5)
        st.toast('Hooray!', icon='🎉')
    
    st.divider()
    st.subheader('st.balloons')
    if st.button('st.balloons'):
        st.balloons()
    
    st.divider()
    st.subheader('st.snow')
    if st.button('st.snow'):
        st.snow()
    
    st.divider()
    st.subheader('st.error')
    st.error('This is an error', icon="🚨")
    
    
    st.divider()
    st.subheader('st.warning')
    st.warning('This is a warning', icon="⚠️")
    
    
    st.divider()
    st.subheader('st.info')
    st.info('This is a purely informational message', icon="ℹ️")
    
    
    st.divider()
    st.subheader('st.success')
    st.success('This is a success message!', icon="✅")
    
    
    st.divider()
    st.subheader('st.exception')
    e = RuntimeError('This is an exception of type RuntimeError')
    st.exception(e)
    
    ########## CHART ELEMENTS ##########
    
    st.header('📊:blue[CHART ELEMENTS]', divider="blue")
    st.subheader('st.area_chart')
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.area_chart(chart_data, color=['#ffaa00', '#aa00ff', '#00ffaa'])
    
    st.divider()
    st.subheader('st.bar_chart')
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.bar_chart(chart_data)
    
    st.divider()
    st.subheader('st.line_chart')
    st.line_chart(chart_data)
    
    st.divider()
    st.subheader('st.scatter_chart')
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["col1", "col2", "col3"])
    chart_data['col4'] = np.random.choice(['A', 'B', 'C'], 20)
    st.scatter_chart(
        chart_data,
        x='col1',
        y='col2',
        color='col4',
        size='col3',
    )
    
    st.divider()
    st.subheader('st.pyplot')
    arr = np.random.normal(1, 1, size=100)
    fig, ax = plt.subplots()
    ax.hist(arr, bins=20)
    st.pyplot(fig)
    
    # st.divider()
    # st.subheader('st.altair_chart')
    # source = data.seattle_weather()
    #
    # scale = alt.Scale(
    #     domain=["sun", "fog", "drizzle", "rain", "snow"],
    #     range=["#e7ba52", "#a7a7a7", "#aec7e8", "#1f77b4", "#9467bd"],
    # )
    # color = alt.Color("weather:N", scale=scale)
    #
    # # We create two selections:
    # # - a brush that is active on the top panel
    # # - a multi-click that is active on the bottom panel
    # brush = alt.selection_interval(encodings=["x"])
    # click = alt.selection_multi(encodings=["color"])
    #
    # # Top panel is scatter plot of temperature vs time
    # points = (
    #     alt.Chart()
    #     .mark_point()
    #     .encode(
    #         alt.X("monthdate(date):T", title="Date"),
    #         alt.Y(
    #             "temp_max:Q",
    #             title="Maximum Daily Temperature (C)",
    #             scale=alt.Scale(domain=[-5, 40]),
    #         ),
    #         color=alt.condition(brush, color, alt.value("lightgray")),
    #         size=alt.Size("precipitation:Q", scale=alt.Scale(range=[5, 200])),
    #     )
    #     .properties(width=550, height=300)
    #     .add_selection(brush)
    #     .transform_filter(click)
    # )
    #
    # # Bottom panel is a bar chart of weather type
    # bars = (
    #     alt.Chart()
    #     .mark_bar()
    #     .encode(
    #         x="count()",
    #         y="weather:N",
    #         color=alt.condition(click, color, alt.value("lightgray")),
    #     )
    #     .transform_filter(brush)
    #     .properties(
    #         width=550,
    #     )
    #     .add_selection(click)
    # )
    #
    # chart = alt.vconcat(points, bars, data=source, title="Seattle Weather: 2012-2015")
    #
    # tab1, tab2 = st.tabs(["Streamlit theme (default)", "Altair native theme"])
    #
    # with tab1:
    #     st.altair_chart(chart, theme="streamlit", use_container_width=True)
    # with tab2:
    #     st.altair_chart(chart, theme=None, use_container_width=True)
    #
    st.divider()
    st.subheader('st.plotly_chart')
    df = px.data.iris()
    fig = px.scatter(
        df,
        x="sepal_width",
        y="sepal_length",
        color="sepal_length",
        color_continuous_scale="reds",
    )
    
    tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)
    with tab2:
        st.plotly_chart(fig, theme=None, use_container_width=True)
    
    st.divider()
    st.subheader('st.bokeh_chart')
    x = [1, 2, 3, 4, 5]
    y = [6, 7, 2, 4, 5]
    p = figure(
        title='simple line example',
        x_axis_label='x',
        y_axis_label='y')
    p.line(x, y, legend_label='Trend', line_width=2)
    st.bokeh_chart(p, use_container_width=True)
    
    st.divider()
    st.subheader('st.graphviz_chart')
    st.graphviz_chart("""
        digraph {
            run -> intr
        intr -> runbl
        runbl -> run
        run -> kernel
        kernel -> zombie
        kernel -> sleep
        kernel -> runmem
        sleep -> swap
        swap -> runswap
        runswap -> new
        runswap -> runmem
        new -> runmem
        sleep -> runmem
        }
        """)
        
        st.divider()
        st.subheader('st.map')
        df = pd.DataFrame({
            "lat": [48.0876499, 48.1132164, 48.1066049],
            "lon": [-1.6215477, -1.6611461, -1.6936411],
            "color": ['#0044ff', '#ff44ff', '#0044ff']
        })
        st.map(df, color='color', size=50, zoom=11)
        
        
        st.divider()
        ''', language='python')
