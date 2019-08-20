from tkinter import *
from tkinter import font


# 合計点と平均点を求める関数
def calc():
    try:
        subject_list = [int(text_nl.get()), int(text_math.get()),
                        int(text_eng.get())]
        # subject_listの最小値が0以上の時の処理
        if min(subject_list) >= 0:
            total_points = sum(subject_list)
            average_points = total_points / 3
            error['text'] = ""
            answer_nl['text'] = "国語 : {} 点".format(int(text_nl.get()))
            answer_math['text'] = "数学 : {} 点".format(int(text_math.get()))
            answer_eng['text'] = "英語 : {} 点".format(int(text_eng.get()))
            answer_total['text'] = "合計点は : {} 点".format(total_points)
            answer_ave['text'] = "平均点は : {} 点".format(round(average_points, 1))
        # subject_listの最小値が0より小さい時の処理
        else:
            error['text'] = "0以上の数字を入力してください"
            answer_nl['text'] = ""
            answer_math['text'] = ""
            answer_eng['text'] = ""
            answer_total['text'] = ""
            answer_ave['text'] = ""
    # 整数以外が入力された時の処理
    except ValueError:
        error['text'] = "整数を入力してください。"
        answer_nl['text'] = ""
        answer_math['text'] = ""
        answer_eng['text'] = ""
        answer_total['text'] = ""
        answer_ave['text'] = ""
    finally:
        text_nl.delete(0, END)
        text_math.delete(0, END)
        text_eng.delete(0, END)


root = Tk()
root.title('テストの合計点と平均点')
root.geometry('700x800')

font_a = font.Font(size=20)
font_b = font.Font(size=16)

lavel_nl = Label(root, text='国語の点数は?', font=font_b)
lavel_nl.place(x=150, y=50)
text_nl = Entry(root, )
text_nl.place(x=400, y=50)

lavel_math = Label(root, text='数学の点数は?', font=font_b)
lavel_math.place(x=150, y=110)
text_math = Entry(root)
text_math.place(x=400, y=110)

lavel_eng = Label(root, text='英語の点数は?', font=font_b)
lavel_eng.place(x=150, y=170)
text_eng = Entry(root)
text_eng.place(x=400, y=170)

error = Label(root, text=u'', font=font_b, fg="#f00")
error.place(x=200, y=250)

answer_nl = Label(root, text=u'', font=font_b)
answer_nl.place(x=280, y=280)

answer_math = Label(root, text=u'', font=font_b)
answer_math.place(x=280, y=330)

answer_eng = Label(root, text=u'', font=font_b)
answer_eng.place(x=280, y=380)

answer_total = Label(root, text=u'', font=font_a)
answer_total.place(x=230, y=450)

answer_ave = Label(root, text=u'', font=font_a)
answer_ave.place(x=230, y=500)

calcButton = Button(root, text='計算', width=20)
calcButton['command'] = calc
calcButton.place(x=120, y=580)

quitButton = Button(root, text='終了', command=quit, width=20, fg="#f00")
quitButton.place(x=390, y=580)

root.mainloop()
