import os
#os.system("pip3 install spacy;pip3 install -U spacy && python3 -m spacy download en_core_web_sm;pip3 install gensim;pip3 install nltk;pip3 install tk;pip3 install BeautifulSoup4;pip3 install bs4;pip3 install urlopen;pip3 install Tokenizer;pip3 install sumy")

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import *
import tkinter.filedialog
from spacy_summarization import text_summarizer
from nltk_summarization import nltk_summarizer
from gensim.summarization import summarize

import time
timestr = time.strftime("%Y%m%d-%H%M%S")

from bs4 import BeautifulSoup
from urllib.request import urlopen

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer


def sumy_summary(docx):
	parser = PlaintextParser.from_string(docx,Tokenizer("english"))
	lex_summarizer = LexRankSummarizer()
	summary = lex_summarizer(parser.document,3)
	summary_list = [str(sentence) for sentence in summary]
	result = ' '.join(summary_list)
	return result
window = Tk()
window.title("Summarizer GUI")
window.geometry('700x500')

style = ttk.Style(window)
style.configure('lefttab.TNotebook',tabposition='wn')

tab_control = ttk.Notebook(window,style='lefttab.TNotebook')

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab5 = ttk.Frame(tab_control)


tab_control.add(tab1,text=f' {"Home":^20s}')
tab_control.add(tab2,text=f' {"File":^20s}')
tab_control.add(tab3,text=f' {"URL":^20s}')
tab_control.add(tab4,text=f' {"Compare":^20s}')
tab_control.add(tab5,text=f' {"About":^20s}')

label1 = Label(tab1,text='Summarizer',padx=5,pady=5)
label1.grid(column=0,row=0)
label1 = Label(tab2,text='File Processing',padx=5,pady=5)
label1.grid(column=0,row=0)
label1 = Label(tab3,text='URL',padx=5,pady=5)
label1.grid(column=0,row=0)
label1 = Label(tab4,text='Compare',padx=5,pady=5)
label1.grid(column=0,row=0)
label1 = Label(tab5,text='About',padx=5,pady=5)
label1.grid(column=0,row=0)

tab_control.pack(expand=1,fill='both')



def get_summary():
	raw_text = entry.get('1.0',tk.END)
	final_text = text_summarizer(raw_text)
	print(final_text)
	result = '\nSummary: {}'.format(final_text)
	tab1_display.insert(tk.END,result)

def save_summary():
	raw_text = entry.get('1.0',tk.END)
	final_text = text_summarizer(raw_text)
	file_name = 'YourSummary' + timestr + '.txt'
	with open(file_name,'w') as f :
		f.write(final_text)
	result = '\nFilename : {} \n Summary: {}'.format(file_name,final_text)
	tab1_display.insert(tk.END,result)


def clear_text():
	entry.delete('1.0',END)


def clear_display_result():
	tab1_display.delete('1.0',END)


def clear_text_file():
	displayed_file.delete('1.0',END)

def clear_text_result():
	tab2_display_text.delete('1.0',END)


def clear_url_entry():
	url_entry.delete('0',END)

def clear_url_display():
	tab3_display_text.delete('1.0',END)

def clear_compare_text():
	entry1.delete('0',END)

def clear_compare_display_result():
	tab4_display.delete('1.0',END)


l1 = Label(tab1,text='Enter text to summarize',padx=5,pady=5)
l1.grid(column=0,row=1)
entry = ScrolledText(tab1,height=10)
entry.grid(row=2,column=0,columnspan=2,pady=5,padx=5)

button1 = Button(tab1,text='Reset',command=clear_text,width=12,bg='#25d366',fg='#fff')
button1.grid(row=4,column=0,padx=10,pady=10)

button2 = Button(tab1,text='Summarize',command=get_summary,width=12,bg='#25d366',fg='#fff')
button2.grid(row=4,column=1,padx=10,pady=10)

button3 = Button(tab1,text='Clear Result',command=clear_display_result,width=12,bg='#25d366',fg='#fff')
button3.grid(row=5,column=0,padx=10,pady=10)

button4 = Button(tab1,text='Save',command=save_summary,width=12,bg='#25d366',fg='#fff')
button4.grid(row=5,column=1,padx=10,pady=10)


tab1_display = ScrolledText(tab1,height=10)
tab1_display.grid(row=7,column=0,columnspan=3,padx=5,pady=5)


#file function
def openfiles():
	file1 = tkinter.filedialog.askopenfilename(initialdir="/Documents",title="select a file",filetypes=(("txt files","*.txt"),("all files","*.*")))
	read_text = open(file1).read()
	displayed_file.insert(tk.END,read_text)



def get_file_summary():
	raw_text = displayed_file.get('1.0',tk.END)
	final_text = text_summarizer(raw_text) 
	result = '\nSummary: {}'.format(final_text)
	tab2_display_text.insert(tk.END,result)


def get_text():
	raw_text = str(url_entry.get())
	page = urlopen(raw_text)
	soup = BeautifulSoup(page,'lxml')
	fetched_text = ''.join(map(lambda p:p.text,soup.find_all('p')))
	url_display.insert(tk.END,fetched_text)

def get_url_summary():
	raw_text = url_display.get('1.0',tk.END)
	final_text = text_summarizer(raw_text) 
	result = '\nSummary: {}'.format(final_text)
	tab3_display_text.insert(tk.END,result)

def use_spacy():
	raw_text = entry1.get('1.0',tk.END)
	final_text = text_summarizer(raw_text)
	print(final_text)
	result = '\nSummary: {}'.format(final_text)
	tab4_display.insert(tk.END,result)

def use_nltk():
	raw_text = entry1.get('1.0',tk.END)
	final_text = nltk_summarizer(raw_text)
	print(final_text)
	result = '\nSummary: {}'.format(final_text)
	tab4_display.insert(tk.END,result)

def use_gensim() :
	raw_text = entry1.get('1.0',tk.END)
	final_text = summarize(raw_text)
	print(final_text)
	result = '\nSummary: {}'.format(final_text)
	tab4_display.insert(tk.END,result)

def use_sumy():
	raw_text = str(entry1.get('1.0',tk.END))
	final_text = sumy_summary(raw_text)
	print(final_text)
	result = '\nSummary: {}'.format(final_text)
	tab4_display.insert(tk.END,result)





#file processing
l1 = Label(tab2,text='Enter text to summarize',padx=5,pady=5)
l1.grid(column=1,row=1)
displayed_file = ScrolledText(tab2,height=10)
displayed_file.grid(row=2,column=0,columnspan=3,pady=5,padx=5)

b0 = Button(tab2,text='OPen File',command=openfiles,width=12,bg='#25d366',fg='#fff')
b0.grid(row=3,column=0,padx=10,pady=10)

b1 = Button(tab2,text='Reset',command=clear_text_file,width=12,bg='#25d366',fg='#fff')
b1.grid(row=3,column=1,padx=10,pady=10)

b2 = Button(tab2,text='Summarize Result',command=get_file_summary,width=12,bg='#25d366',fg='#fff')
b2.grid(row=3,column=2,padx=10,pady=10)

b3 = Button(tab2,text='Clear Result',command=clear_text_result,width=12,bg='#25d366',fg='#fff')
b3.grid(row=5,column=1,padx=10,pady=10)

b4 = Button(tab2,text='Close',command=window.destroy)
b4.grid(row=5,column=2,padx=10,pady=10)



tab2_display_text = ScrolledText(tab2,height=10)
tab2_display_text.grid(row=7,column=0,columnspan=3,padx=5,pady=5)

tab2_display_text.config(state=NORMAL)




#url
l1 = Label(tab3,text='Enter URL to summarize')
l1.grid(column=0,row=1)

raw_entry=StringVar()
url_entry = Entry(tab3,textvariable=raw_entry,width=50)
url_entry.grid(row=1,column=1)

button1 = Button(tab3,text='Reset',command=clear_url_entry,width=12,bg='#25d366',fg='#fff')
button1.grid(row=4,column=0,padx=10,pady=10)

button2 = Button(tab3,text='Get Text',command=get_text,width=12,bg='purple',fg='#fff')
button2.grid(row=4,column=1,padx=10,pady=10)

button3 = Button(tab3,text='Clear Result',command=clear_url_display,width=12,bg='#02A8F4',fg='#fff')
button3.grid(row=5,column=0,padx=10,pady=10)

button4 = Button(tab3,text='Summarize',command=get_url_summary,width=12,bg='#03A9F4',fg='#fff')
button4.grid(row=5,column=1,padx=10,pady=10)


url_display = ScrolledText(tab3,height=10)
url_display.grid(row=7,column=0,columnspan=3,padx=5,pady=5)


tab3_display_text = ScrolledText(tab3,height=10)
tab3_display_text.grid(row=10,column=0,columnspan=3,padx=5,pady=5)


#comparer
l1 = Label(tab4,text='Enter Text to summarize')
l1.grid(column=0,row=1)

entry1 = ScrolledText(tab4,height=10)
entry1.grid(row=2,column=0,columnspan=3,padx=5,pady=3)


button1 = Button(tab4,text='Reset',command=clear_compare_text,width=12,bg='#25D366',fg='#fff')
button1.grid(row=4,column=0,padx=10,pady=10)

button2 = Button(tab4,text='Spacy',command=use_spacy,width=12,bg='#cd201f',fg='#fff')
button2.grid(row=4,column=1,padx=10,pady=10)

button3 = Button(tab4,text='Clear Result',command=clear_compare_display_result,width=12,bg='#03A9F4',fg='#fff')
button3.grid(row=5,column=0,padx=10,pady=10)

button4 = Button(tab4,text='NLTK',command=use_nltk,width=12,bg='blue',fg='#fff')
button4.grid(row=4,column=2,padx=10,pady=10)

button4 = Button(tab4,text='Gensim',command=use_gensim,width=12,bg='purple',fg='#fff')
button4.grid(row=5,column=1,padx=10,pady=10)

button4 = Button(tab4,text='Sumy',command=use_sumy,width=12,bg='#03A9F4',fg='#fff')
button4.grid(row=5,column=2,padx=10,pady=10)

url_display = ScrolledText(tab3,height=10)
url_display.grid(row=7,column=0,columnspan=3,padx=5,pady=5)


tab4_display = ScrolledText(tab4,height=15)
tab4_display.grid(row=7,column=0,columnspan=3,padx=5,pady=5)

window.mainloop()
