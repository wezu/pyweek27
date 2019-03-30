from direct.interval.IntervalGlobal import *

song_dict={
      0.0:'hit_the_button',
      4.0: 'brace_yourself',
      5.0:'we_are_number_one',
      5.5:'two',
      6.2:'free',
      6.7:'fore',
      7.3:'head_1',
      8.5:'head_2',
      9.8:'hi_five',
      10.2:'six',
      10.7:'seven_of_nine',
      11.5:'pieces_of_eight',
      12.0:'dodge_pasta',
      14.6:'is_this',
      16.8:'seagull_along',
      18.2:'seagull_sing',
      19.2:'clap_hermione',
      20.2:'feet1',
      20.5:'feet2',
      20.8:'feet1',
      21.1:'feet2',
      21.7:'seagull_along',
      23.5:'seagull_sing',
      26.4:'seven_of_megusta',
      27.0:'10',
      27.6:'eleven',
      28.2:'12_gauge',
      28.8:'baby',
      30.0:'baby_elf',
      31.2:'v13',
      31.8:'m14',
      32.3:'m15',
      32.9:'m16',
      33.4:'no_date',
      34.6:'no_date_50',
      36.0:'is_this',
      38.3:'seagull_along',
      39.7:'seagull_sing',
      40.7:'kim_clap',
      41.7:'army_stomp',
      42.9:'seagull_along',
      45.1:'seagull_sing',
      47.9:'a17',
      48.6:'a18',
      49.1:'xix',
      49.6:'20-20',
      50.3:'doge2',
      52.4:'21',
      53.0:'22',
      53.5:'23',
      54.1:'24',
      55.0:'funny',
      55.8:'kissing',
      56.5:'taste',
      57.5:'is_this',
      58.7:'seagull_along',
      60.3:'seagull_sing',
      62.3:'kim_clap',
      63.1:'feet1',
      63.4:'feet2',
      63.7:'feet1',
      64.0:'feet2',
      64.4:'seagull_along',
      67.3:'seagull_sing',
      69.4:'troll',
      71.5:'please',
      73.3:'lol',
      76.7:'is_this',
      }

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
