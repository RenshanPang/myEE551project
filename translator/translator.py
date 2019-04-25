import requests
import tkinter as tk
def translateCtoE():
    url = 'https://fanyi.baidu.com/transapi'
    data={
        'from':	'zh',
        'to': 'en',
        'query': t1.get(0.0, 'end'),
        'transtype': 'realtime',
        'simple_means_flag': '3',
        'sign': '338183.117302',
        'token': 'd376ab8d9c4598d446a3d6adf3d6c72a'
    }
    response = requests.post(url, data= data).json()
    r = response['data'][0]['dst']
    print(response)
    t1.delete(0.0, 'end')
    t1.insert('end', r)

def translateEtoC():
    url = 'https://fanyi.baidu.com/transapi'
    data={
        'from':	'en',
        'to': 'zh',
        'query': t1.get(0.0, 'end'),
        'transtype': 'realtime',
        'simple_means_flag': '3',
        'sign': '338183.117302',
        'token': 'd376ab8d9c4598d446a3d6adf3d6c72a'
    }
    response = requests.post(url, data= data).json()
    r = response['data'][0]['dst']
    t1.delete(0.0, 'end')
    t1.insert('end', r)

def clear():
    t1.delete(0.0, 'end')

root = tk.Tk()
root.title('Translation Aplication')
root.geometry('400x200')
l1 = tk.Label(root, text = 'Please input messages: ')
l1.grid()
t1 = tk.Text(root, width = 56, height = 5)
t1.grid()
b1 = tk.Button(root, text = 'Translating from Chinese to English', width = 32, command = translateCtoE)
b1.grid(row = 2, column = 0)
b2 = tk.Button(root, text = 'Translating from English to Chinese', width = 32, command = translateEtoC)
b2.grid(row = 3, column = 0)
b3 = tk.Button(root, text = 'Clear', width = 32, command = clear)
b3.grid(row = 4, column = 0)
root.mainloop()
