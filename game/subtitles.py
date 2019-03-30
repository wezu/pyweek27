from direct.interval.IntervalGlobal import *
from game.color_palette import ColorPalette

song_dict={
      0.0:'Press the buttons as they appear!',
      2.0: 'But only with the right number!',
      5.5:'One',
      5.9:'Two',
      6.3:'Three',
      6.9:'Four',
      7.7:'Standing on my head',
      8.9:'I can kiss the floor.',
      10.0:'Five',
      11.0:'Six',
      11.5:'Seven',
      12.0:'Eight',
      13.0:'My dog eat spaghetti of my plate',
      14.6:'This is The Silly Number Song,',
      16.8:"C'mon everybody sing along!",
      19.5:'Clap your hands',
      20.2:'While stomping your feet',
      21.7:'And sing this Silly Number Sooong!',
      26.9:'Nine',
      27.6:'Ten',
      28.2:'Eleven',
      29.0:'Twelve',
      29.5:'My baby brother',
      30.5:'Looks like an elf!',
      32.0:'Thirteen',
      32.8:'Fourteen',
      33.3:'Fifteen',
      33.9:'Sixteen',
      34.4:"My sistar can't date",
      35.6:"Until she's fifty.",
      36.0:'This is The Silly Number Song,',
      38.3:"C'mon everybody sing along!",
      40.7:'Clap your hands',
      41.7:'While stamping your feet',
      42.9:'And sing this Silly Number Sooong!',
      47.9:'Seventeen',
      48.6:'Eighteen',
      49.1:'Nineteen',
      49.6:'Twenty',
      50.3:'Someone eat all my Good & Plenty',
      52.4:'Twenty-one',
      53.0:'Twenty-two',
      53.5:'Twenty-three',
      54.1:'Twenty-four',
      55.0:'My lips taste funny',
      55.8:'After kissing the floor.',
      57.5:'This is The Silly Number Song,',
      58.7:"C'mon everybody sing along!",
      62.3:'Clap your hands',
      63.1:'While stomping your feet',
      64.4:'And sing this Silly Number Sooong!',
      69.4:'One',
      69.6:'Two',
      70.0:'Three',
      70.3:'Four',
      70.5:'Five',
      70.8:'Six',
      71.3:'Seven',
      71.5:'Eight',
      71.7:'Nine',
      72.0:'Ten',
      72.3:'Eleven',
      72.7:'Twelve',
      72.9:'Thirteen',
      73.3:'Fourteen',
      73.6:'Fifteen',
      73.8:'Sixteen',
      74.2:'Seventeen',
      74.4:'Eighteen',
      74.7:'Nineteen',
      75.0:'Twenty',
      75.3:'Twenty-one',
      75.5:'Twenty-two',
      75.8:'Twenty-three',
      76.2:'Twenty-four',
      76.7:'This is The Silly Number Song.',
      79.0:'This is The Silly Number Song!',
      81.2:'This is The Silly Number Song!!'
      }

song=[]
t=0
for time, name in song_dict.items():
    song.append((round(time-t, 1), name))
    t=time


def make_song_sequence(text_node):
    colors=ColorPalette()
    s=Sequence()
    for delay, text in song:
        c=colors.new_color()
        s.append(Wait(delay))
        s.append(Func(text_node.set_text_color, c))
        s.append(Func(text_node.set_text, text))
    return s
