from direct.interval.IntervalGlobal import *
from game.color_palette import ColorPalette

song_dict={
      0.0:'Press the buttons as they appear!',
      2.0: 'But only with the right number!',
      5.0:'One',
      5.5:'Two',
      6.2:'Three',
      6.7:'Four',
      7.3:'Standing on my head',
      8.5:'I can kiss the floor.',
      9.8:'Five',
      10.2:'Six',
      10.7:'Seven',
      11.5:'Eight',
      12.0:'My dog eat spaghetti of my plate',
      14.6:'This is The Silly Number Song,',
      16.8:"C'mon everybody sing along!",
      19.2:'Clap your hands',
      20.2:'While stamping your feet',
      21.4:'And sing this Silly Number Sooong!',
      26.4:'Nine',
      27.0:'Ten,',
      27.6:'Eleven,',
      28.2:'Twelve.',
      28.8:'My baby brother',
      30.0:'Looks like an elf!',
      31.2:'Thirteen',
      31.8:'Fourteen',
      32.3:'Fifteen',
      32.9:'Sixteen',
      33.4:"My sistar can't date",
      34.6:"Until she's fifty.",
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


def make_song_sequence(text_node, music):
    colors=ColorPalette()
    s=Sequence(Func(music.play))
    for delay, text in song:
        c=colors.new_color()
        s.append(Wait(delay))
        s.append(Func(text_node.set_text_color, c))
        s.append(Func(text_node.set_text, text))
    return s
