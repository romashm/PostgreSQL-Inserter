# API-Storefront-PostgreSQL
<p align="center">
  <img src="https://media.giphy.com/media/UDXM9DS5SBXCr2gsUi/giphy.gif">
</p>
<h2> 📦 Installation </h2>
<p> Before the installation this project, you should be sure that you install PostgreSQL. </p>
<h2> 🎯 Main target </h2>
<p> Create a database in the PostgreSQL, then receive an access via port. Cultivate data & illation in JSON package in the web-server. </p>
<h2> 📩 Developing </h2>
<p> First of all, Work is started when web-server is started. Create a database, then go to the proporties to see owner name, psw & etc. . I created database named Storefront 📦, then I should create a table. Inside python I created a file <code> .sql </code> and write following : </p>
<p align="center">
  <img src="https://sun9-23.userapi.com/impg/sGN9g1vpC81WnOQ1P9s9ycgHxWYcM86xY0Pr-g/7UX_G54DxPk.jpg?size=360x163&quality=96&sign=38007790c3948031a3b47b2e00ac8051&type=album">
</p>
<p> Input inside special <b>console log</b>, then check it appeared or not.  </p>
<p align="center">
<img src="https://sun9-71.userapi.com/impg/Qq4e0D_C-qawZpGHu88Dqaxn5DXCIfIsh6YbLw/eH5Xg4cZZ5A.jpg?size=604x392&quality=96&sign=e63c04e9ec0da7f73244a86202e11523&type=album">
<img src="https://sun9-20.userapi.com/impg/d84-Af97qsUTcXCL8xi0rxEvUKTs6WFM9VGZUQ/UI8yU3fb7G8.jpg?size=604x390&quality=96&sign=0b6aa61e349e7d32f0de5ac50e5d7a5f&type=album">
</p>
<p> You can abserve what kinda information you will see in the header of the table 📩. Thereafter insert new inforamation, in my case I got a JSON package to work with.  </p>
<p align="center">
  <img src="https://sun9-81.userapi.com/impg/CoKl4qdw896bXidKHnx6eWMvrP6_ZXof8igeUA/sCwnoikzdig.jpg?size=604x389&quality=96&sign=f06e9c20549cd74e551868e651f9e9d7&type=album">
</p>
<p> Lets return to the Flask, and write down our basic start <b> ( for Flask library ) </b>. Likewise, create a config.py file & write there following : <code>host = "localhost"
user = "postgres"
password = "psw"
database = "store" </code> . Therefore, import this file inside main.py, then connect it with server using command <code> psycopg2.connect </code>. Made a <i> try - except mode </i> .</p>
<p align="center">
<img src="https://sun9-55.userapi.com/impg/GsYWAqObS7T03QauV1_1od5PEm2iFPRTy4t5iA/mkWxUr1Sil4.jpg?size=604x392&quality=96&sign=59b34892228d84f10f8003f00304ef77&type=album">
</p>
<p> After work done, return it & back to the page ( reload a web-site ). You can abserve that JSON return, however without headers of the table. Next we'll create a collector for database #2. Lets install bootstrap library in our project, </p>
