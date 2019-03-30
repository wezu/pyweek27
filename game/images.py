from direct.interval.IntervalGlobal import *

song_dict={
      0.0:'hit_the_button',
      3.5:'brace_yourself',
      5.5:'we_are_number_one',
      5.9:'two',
      6.3:'free',
      6.9:'fore',
      7.7:'head_1',
      8.9:'head_2',
      10.0:'hi_five',
      11.0:'six',
      11.5:'seven_of_nine',
      12.0:'pieces_of_eight',
      13.0:'dodge_pasta',
      14.6:'is_this',
      16.8:'seagull_along',
      17.9:'seagull_sing',
      19.5:'clap_hermione',
      20.2:'feet1',
      20.5:'feet2',
      20.8:'feet1',
      21.1:'feet2',
      21.7:'seagull_sing',
      26.9:'seven_of_megusta',
      27.6:'10',
      28.2:'eleven',
      29.0:'12_gauge',
      29.5:'baby',
      30.5:'baby_elf',
      32.0:'v13',
      32.8:'m14',
      33.3:'m15',
      33.9:'m16',
    }
'''
      33.4:"My sistar can't date",
      34.6:"Until she's fifty.",
      36.0:'This is The Silly Number Song,',
      38.3:"C'mon everybody sing along!",
      40.7:'Clap your hands',
      41.7:'while stomping your feet',
      42.9:'and sing this Silly Number Sooong!',
      47.9:'Seventeen,',
      48.6:'eighteen,',
      49.1:'nineteen,',
      49.6:'twenty.',
      50.3:'Someone eat all my Good & Plenty',
      52.4:'Twenty-one,',
      53.0:'twenty-two,',
      53.5:'twenty-three,',
      54.1:'twenty-four.',
      55.0:'My lips taste funny',
      55.8:'after kissing the floor.',
      57.5:'This is The Silly Number Song,',
      58.7:"C'mon everybody sing along!",
      62.3:'Clap your hands',
      63.1:'while stomping your feet',
      64.4:'and sing this Silly Number Sooong!',
      69.4:'One,',
      69.6:'two,',
      70.0:'three,',
      70.3:'four,',
      70.5:'five,',
      70.8:'six,',
      71.3:'seven,',
      71.5:'eight,',
      71.7:'nine,',
      72.0:'ten,',
      72.3:'eleven,',
      72.7:'twelve,',
      72.9:'thirteen,',
      73.3:'fourteen,',
      73.6:'fifteen,',
      73.8:'sixteen,',
      74.2:'seventeen,',
      74.4:'eighteen,',
      74.7:'nineteen,',
      75.0:'twenty,',
      75.3:'twenty-one,',
      75.5:'twenty-two,',
      75.8:'twenty-three,',
      76.2:'twenty-four.',
      76.7:'This is The Silly Number Song.',
      79.0:'This is The Silly Number Song!',
      81.2:'This is The Silly Number Song!!'
      }'''

song=[]
t=0
for time, name in song_dict.items():
    song.append((round(time-t, 1), name))
    t=time
#print(song)
'''

song=(
    (0.1, 'hit_the_button'),
    (4.9, 'we_are_number_one'),
    (0.5, 'two'),
    (0.7, 'free'),
    (0.5, 'fore'),
    (0.6, 'head_1'),
    (1.2, 'head_2'),
    (1.3, 'hi_five'),
    (0.4, 'six')
    )#'''
def make_image_sequence(image_node):
    s=Sequence()
    for delay, img_name in song:
        img=loader.load_texture('image/'+img_name+'.png')
        s.append(Wait(delay))
        s.append(Func(image_node.show))
        s.append(Func(image_node.setImage, img))
        s.append(Func(image_node.set_transparency, 1))#TransparencyAttrib.M_alpha=1
        s.append(Func(image_node.set_bin, "fixed", 10))
    return s
