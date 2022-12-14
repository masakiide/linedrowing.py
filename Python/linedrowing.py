#https://imagingsolution.net/program/python/tkinter/canvas_drawing_lines_circles_shapes/#toc3
import tkinter as tk

from pyrsistent import v

root = tk.Tk()
root.geometry("1000x1200")

import tkinter as tk

#base = tk.Tk()
#base.geometry('500x400')
#base.title('Button-set-test')
#root.title('Button-set-test')

button1 = tk.Button(root, text='ボタン1').place(x=100,y=100)
button2 = tk.Button(root, text='ボタン2').place(x=200,y=100)
button3 = tk.Button(root, text='ボタン3').place(x=300,y=100)
button4 = tk.Button(root, text='ボタン4').place(x=300,y=200)
button5 = tk.Button(root, text='ボタン5').place(x=110,y=110)

#base.mainloop()

# Canvasの作成
canvas = tk.Canvas(root, bg = "white")
# Canvasを配置
canvas.pack(fill = tk.BOTH, expand = True)

#線の描画
canvas.create_line(100, 500, 400, 500, dash=(5, 3) ) #2mライン
canvas.create_text(100, 500, text="2y", anchor=tk.NW, font=("",20))   # 基準位置左上
canvas.create_line(100, 200, 400, 200, dash=(5, 3) ) #5mライン
canvas.create_text(100, 200, text="5y", anchor=tk.NW, font=("",20))   # 基準位置左上
canvas.create_line(100, 100, 400, 100, dash=(5, 3) ) #6mライン
canvas.create_text(100, 100, text="6y", anchor=tk.NW, font=("",20))   # 基準位置左上

#コートの作成
canvas.create_line(100, 700, 400, 700 ) 
canvas.create_line(400, 700, 400, 750 ) 
canvas.create_line(400, 750, 600, 750 ) 
canvas.create_line(600, 750, 600, 700 ) 
canvas.create_line(600, 700, 900, 700 ) 

#canvas.create_line(280, 190, 10, 20, fill = "Red", width = 3)
#canvas.create_line(10, 160, 150, 180, 300, 160, 450, 180, 590, 160 ) # 折れ線

#① 200, 500
#② 400, 100
#③ 600, 100
#④ 800, 500
#⑤ 600, 500
#⑥ 400, 500
#⑦ 250, 300
#⑧ 500, 300
#⑨ 750, 300
#⓪ 500, 700

canvas.create_line(200, 500, 400, 700,tag = '1j',fill='white' )#１→j
canvas.create_line(200, 500, 500, 700,tag = '1k',fill='white' )#１→k
canvas.create_line(200, 500, 600, 700,tag = '1l',fill='white' )#１→l
canvas.create_line(200, 501, 400, 101,tag = '12p',fill='white' )#１→２ 
canvas.create_line(200, 501, 600, 101,tag = '13p',fill='white' )#１→３
canvas.create_line(200, 495, 800, 495,tag = '14p',fill='white' )#１→４
canvas.create_line(200, 505, 600, 505,tag = '15p',fill='white' )#１→５
canvas.create_line(200, 500, 400, 500,tag = '16p',fill='white' )#１→６
canvas.create_line(200, 501, 250, 301,tag = '17p',fill='white' )#１→７
canvas.create_line(200, 501, 500, 301,tag = '18p',fill='white' )#１→８
canvas.create_line(200, 501, 750, 301,tag = '19p' ,fill='white')#１→９

canvas.create_line(405, 100, 400, 700,tag = '2j',fill='white' )#２→j
canvas.create_line(400, 100, 500, 700,tag = '2k',fill='white' )#２→k
canvas.create_line(400, 100, 600, 700,tag = '2l',fill='white' )#２→l
canvas.create_line(400, 99, 200, 499,tag = '21p',fill='white' )#２→１
canvas.create_line(400, 101, 600, 101,tag = '23p',fill='white' )#２→３
canvas.create_line(400, 101, 800, 501,tag = '24p',fill='white' )#２→４
canvas.create_line(400, 101, 600, 501,tag = '25p',fill='white' )#２→５
canvas.create_line(400, 101, 400, 501,tag = '26p',fill='white' )#２→６
canvas.create_line(400, 101, 250, 301,tag = '27p',fill='white' )#２→７
canvas.create_line(400, 101, 500, 301,tag = '28p',fill='white' )#２→８
canvas.create_line(400, 101, 750, 301,tag = '29p',fill='white')#２→９


canvas.create_line(600, 100, 400, 700,tag = '3j',fill='white' )#３→０1
canvas.create_line(600, 100, 500, 700,tag = '3k',fill='white' )#３→０2
canvas.create_line(595, 100, 600, 700,tag = '3l',fill='white' )#３→０3
canvas.create_line(600, 99, 200, 499,tag = '31p',fill='white' )#３→１
canvas.create_line(600, 99, 400, 99,tag = '32p',fill='white' )#３→２
canvas.create_line(600, 101, 800, 499,tag = '34p',fill='white' )#３→４
canvas.create_line(600, 101, 600, 501,tag = '35p',fill='white' )#３→５
canvas.create_line(600, 101, 400, 501,tag = '36p',fill='white' )#３→６
canvas.create_line(600, 101, 250, 301,tag = '37p',fill='white' )#３→７
canvas.create_line(600, 101, 500, 301,tag = '38p',fill='white' )#３→８
canvas.create_line(600, 101, 750, 301,tag = '39p',fill='white' )#３→９


canvas.create_line(800, 500, 400, 700,tag = '4j',fill='white' )#４→０1
canvas.create_line(800, 500, 500, 700,tag = '4k',fill='white' )#４→０2
canvas.create_line(800, 500, 600, 700,tag = '4l',fill='white' )#４→０3
canvas.create_line(800, 492, 200, 492,tag = '41p',fill='white' )#４→１
canvas.create_line(800, 499, 400, 99,tag = '42p',fill='white' )#４→２
canvas.create_line(800, 499, 600, 99,tag = '43p',fill='white' )#４→３
canvas.create_line(800, 505, 600, 505,tag = '45p',fill='white' )#４→５
canvas.create_line(800, 500, 400, 500,tag = '46p',fill='white' )#４→６
canvas.create_line(800, 501, 250, 301,tag = '47p',fill='white' )#４→７
canvas.create_line(800, 501, 500, 301,tag = '48p',fill='white' )#４→８
canvas.create_line(800, 501, 750, 301,tag = '49p',fill='white' )#４→９


canvas.create_line(600, 500, 400, 700,tag = '5j',fill='white' )#５→０1
canvas.create_line(600, 500, 500, 700,tag = '5k',fill='white' )#５→０2
canvas.create_line(600, 500, 600, 700,tag = '5l',fill='white' )#５→０3
canvas.create_line(600, 502, 200, 502,tag = '51p',fill='white' )#５→１
canvas.create_line(600, 499, 400, 99,tag = '52p',fill='white' )#５→２
canvas.create_line(600, 499, 600, 99,tag = '53p',fill='white' )#５→３
canvas.create_line(600, 502, 600, 502,tag = '54p',fill='white' )#５→４
canvas.create_line(600, 501, 400, 501,tag = '56p',fill='white' )#５→６
canvas.create_line(600, 501, 250, 301,tag = '57p',fill='white' )#５→７
canvas.create_line(600, 501, 500, 301,tag = '58p',fill='white' )#５→８
canvas.create_line(600, 501, 750, 301,tag = '59p',fill='white' )#５→９


canvas.create_line(400, 500, 400, 700,tag = '6j',fill='white' )#６→０1
canvas.create_line(400, 500, 500, 700,tag = '6k',fill='white' )#６→０2
canvas.create_line(400, 500, 600, 700,tag = '6l',fill='white' )#６→０3
canvas.create_line(400, 498, 200, 498,tag = '61p',fill='white' )#６→１
canvas.create_line(400, 499, 400, 99,tag = '62p',fill='white' )#６→２
canvas.create_line(400, 499, 600, 99,tag = '63p',fill='white' )#６→３
canvas.create_line(400, 498, 800, 498,tag = '64p',fill='white' )#６→４
canvas.create_line(400, 499, 600, 499,tag = '65p',fill='white' )#６→５
canvas.create_line(400, 501, 250, 301,tag = '67p',fill='white' )#６→７
canvas.create_line(400, 501, 500, 301,tag = '68p',fill='white' )#６→８
canvas.create_line(400, 501, 750, 301,tag = '69p',fill='white' )#６→９

canvas.create_line(250, 300, 400, 700,tag = '7j',fill='white' )#７→０1
canvas.create_line(250, 300, 500, 700,tag = '7k',fill='white' )#７→０2
canvas.create_line(250, 300, 600, 700,tag = '7l',fill='white' )#７→０3
canvas.create_line(250, 299, 200, 499,tag = '71p',fill='white' )#７→１
canvas.create_line(250, 299, 400, 99,tag = '72p',fill='white' )#７→２
canvas.create_line(250, 299, 600, 99,tag = '73p',fill='white' )#７→３
canvas.create_line(250, 299, 800, 499,tag = '74p',fill='white' )#７→４
canvas.create_line(250, 299, 600, 499,tag = '75p',fill='white' )#７→５
canvas.create_line(250, 299, 400, 499,tag = '76p',fill='white' )#７→６
canvas.create_line(250, 301, 500, 301,tag = '78p',fill='white' )#７→８
canvas.create_line(250, 301, 750, 301,tag = '79p',fill='white' )#７→９


canvas.create_line(500, 300, 400, 700,tag = '8j',fill='white' )#８→j
canvas.create_line(500, 300, 500, 700,tag = '8k',fill='white' )#８→k
canvas.create_line(500, 300, 600, 700,tag = '8l',fill='white' )#８→l
canvas.create_line(500, 299, 200, 499,tag = '81p',fill='white' )#８→１
canvas.create_line(500, 299, 400, 99,tag = '82p',fill='white' )#８→２
canvas.create_line(500, 299, 600, 99,tag = '83p',fill='white' )#８→３
canvas.create_line(500, 299, 800, 499,tag = '84p',fill='white' )#８→４
canvas.create_line(500, 299, 600, 499,tag = '85p',fill='white' )#８→５
canvas.create_line(500, 299, 400, 499,tag = '86p',fill='white' )#８→６
canvas.create_line(500, 299, 250, 299,tag = '87p',fill='white' )#８→７
canvas.create_line(500, 301, 750, 301,tag = '89p',fill='white' )#８→９


canvas.create_line(750, 300, 400, 700,tag = '9j',fill='white' )#９→j
canvas.create_line(750, 300, 500, 700,tag = '9k',fill='white' )#９→k
canvas.create_line(750, 300, 600, 700,tag = '9l',fill='white' )#９→l
canvas.create_line(750, 299, 200, 499,tag = '91p',fill='white' )#９→１
canvas.create_line(750, 299, 400, 99,tag = '92p',fill='white' )#９→２
canvas.create_line(750, 299, 600, 99,tag = '93p',fill='white' )#９→３
canvas.create_line(750, 299, 800, 499,tag = '94p',fill='white' )#９→４
canvas.create_line(750, 299, 600, 299,tag = '95p',fill='white' )#９→５
canvas.create_line(750, 299, 400, 499,tag = '96p',fill='white' )#９→６
canvas.create_line(750, 299, 250, 299,tag = '97p',fill='white' )#９→７
canvas.create_line(750, 299, 500, 299,tag = '98p',fill='white' )#９→８

#何セット目か記録
#a = 5
#https://www.youtube.com/watch?v=Po_Ao9LFfUo

#ゴールならg、シュートならs、カットされたらc  

canvas.create_text(100, 0, text= "blue  10セット目.s", anchor=tk.NW, font=("",50))   # 基準位置左上
#パス回しを記録→→'   'に"何番から何番にボールが出たのか"＋"パスならp"/"ゴールならg"を入力

canvas.itemconfigure('12p', fill='black')
canvas.itemconfigure('23p', fill='black')
canvas.itemconfigure('34p', fill='black')
canvas.itemconfigure('41p', fill='black')
canvas.itemconfigure('12p', fill='black')
canvas.itemconfigure('24p', fill='black')
canvas.itemconfigure('43p', fill='black')
canvas.itemconfigure('3k', fill='black')
canvas.itemconfigure('', fill='black')
canvas.itemconfigure('', fill='black')
canvas.itemconfigure('', fill='black')
canvas.itemconfigure('', fill='black')
canvas.itemconfigure('', fill='black')
canvas.itemconfigure('', fill='black')
canvas.itemconfigure('', fill='black')
canvas.itemconfigure('', fill='black')



root.mainloop()