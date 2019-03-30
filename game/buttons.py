from direct.interval.IntervalGlobal import *
import random

song=(
    (5.2, '1'),
    (0.5, '2'),
    (0.7, '3'),
    (0.5, '4'),
    (3.1, '5'),
    (0.4, '6'),
    (0.5, '7'),
    (0.8, '8'),
    (14.9, '9'),
    (0.6, '10'),
    (0.6, '11'),
    (0.6, '12'),
    (3.0, '13'),
    (0.6, '14'),
    (0.5, '15'),
    (0.6, '16'),
    (15.0, '17'),
    (0.7, '18'),
    (0.5, '19'),
    (0.5, '20'),
    (2.8, '21'),
    (0.6, '22'),
    (0.5, '23'),
    (0.6, '24'),
    (15.3, '1'),
    (0.2, '2'),
    (0.4, '3'),
    (0.3, '4'),
    (0.2, '5'),
    (0.3, '6'),
    (0.5, '7'),
    (0.2, '8'),
    (0.2, '9'),
    (0.3, '10'),
    (0.3, '11'),
    (0.4, '12'),
    (0.2, '13'),
    (0.4, '14'),
    (0.3, '15'),
    (0.2, '16'),
    (0.4, '17'),
    (0.2, '18'),
    (0.3, '19'),
    (0.3, '20'),
    (0.3, '21'),
    (0.2, '22'),
    (0.3, '23'),
    (0.4, '24'),
    )

def make_button_sequence(button, fake_button):
    s=Sequence()
    for delay, text in song:
        x=random.uniform(0.15,0.5)*random.choice([-1, 1])
        y=0.8#random.uniform(0.4,0.8)*random.choice([-1, 1])
        y1=random.uniform(0.7,0.85)
        y2=random.uniform(0.7,0.85)
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
