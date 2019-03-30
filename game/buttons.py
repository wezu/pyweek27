from direct.interval.IntervalGlobal import *
import random

song_dict={
      5.0:'1',
      5.5:'2',
      6.2:'3',
      6.7:'4',
      9.8:'5',
      10.2:'6',
      10.7:'7',
      11.5:'8',
      26.4:'9',
      27.0:'10',
      27.6:'11',
      28.2:'12',
      31.2:'12',
      31.8:'14',
      32.3:'15',
      32.9:'16',
      47.9:'17',
      48.6:'18',
      49.1:'19',
      49.6:'20',
      52.4:'21',
      53.0:'22',
      53.5:'23',
      54.1:'24',
      69.4:'1',
      69.6:'2',
      70.0:'3',
      70.3:'4',
      70.5:'5',
      70.8:'6',
      71.3:'7',
      71.5:'8',
      71.7:'9',
      72.0:'10',
      72.3:'11',
      72.7:'12',
      72.9:'13',
      73.3:'14',
      73.6:'15',
      73.8:'16',
      74.2:'17',
      74.4:'18',
      74.7:'19',
      75.0:'20',
      75.3:'21',
      75.5:'22',
      75.8:'23',
      76.2:'24',
      }

song=[]
t=0
for time, name in song_dict.items():
    song.append((round(time-t, 1), name))
    t=time

def make_button_sequence(button, fake_button):
    s=Sequence()
    for delay, text in song:
        x=random.uniform(0.2,0.7)*random.choice([-1, 1])
        y=0.8#random.uniform(0.4,0.8)*random.choice([-1, 1])
        y1=random.uniform(0.65,0.85)
        y2=random.uniform(0.65,0.85)
        n=int(text)
        i=random.randint(1, 24)
        if n==i:
            i+=1
        i=str(i)
        s.append(Wait(delay))
        s.append(Func(button.show))
        s.append(Func(button.set_pos, (x,0,y1)))
        s.append(Func(button.setText, text))
        s.append(Func(fake_button.show))
        s.append(Func(fake_button.set_pos, (-x,0,y2)))
        s.append(Func(fake_button.setText, i))
    s.append(Wait(1.0))
    s.append(Func(button.hide))
    s.append(Func(fake_button.hide))
    return s
