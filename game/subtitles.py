from direct.interval.IntervalGlobal import *
from game.color_palette import ColorPalette

song_dict={
      5.0:'One,',
      5.5:'two,',
      6.2:'three,',
      6.7:'four.',
      7.3:'Standing on my head',
      8.5:'I can kiss the floor.',
      9.8:'Five,',
      10.2:'six,',
      10.7:'seven,',
      11.5:'eight.',
      12.0:'My dog eat spaghetti of my plate',
      14.6:'This is The Silly Number Song,',
      16.8:"C'mon everybody sing along!",
      19.2:'Clap your hands',
      20.2:'while stomping your feet',
      21.4:'and sing this Silly Number Sooong!',
      26.4:'Nine,',
      27.0:'ten,',
      27.6:'eleven,',
      28.2:'twelve.',
      28.8:'My baby brother',
      30.0:'Looks like an elf!',
      31.2:'Thirteen,',
      31.8:'fourteen,',
      32.3:'fifteen,',
      32.9:'sixteen.',
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
      }

song=(
    (5.0, 'One'),
    (0.5, 'Two'),
    (0.7, 'Fhree'),
    (0.5, 'Four'),
    (0.6, 'Standing on my head'),
    (1.2, 'I can kiss the floor.'),
    (1.3, 'Five'),
    (0.4, 'Six'),
    (0.5, 'Seven'),
    (0.8, 'Eight'),
    (0.5, 'My dog eat spaghetti of my plate'),
    (2.6, 'This is The Silly Number Song,'),
    (2.2, "C'mon everybody sing along!"),
    (2.4, 'Clap your hands'),
    (1.0, 'While stomping your feet'),
    (1.2, 'And sing this Silly Number Sooong!'),
    (5.0, 'Nine'),
    (0.6, 'Ten'),
    (0.6, 'Eleven'),
    (0.6, 'Twelve'),
    (0.6, 'My baby brother'),
    (1.2, 'Looks like an elf!'),
    (1.2, 'Thirteen'),
    (0.6, 'Fourteen'),
    (0.5, 'Fifteen'),
    (0.6, 'Sixteen'),
    (0.5, "My sistar can't date"),
    (1.2, "Until she's fifty."),
    (1.4, 'This is The Silly Number Song,'),
    (2.3, "C'mon everybody sing along!"),
    (2.4, 'Clap your hands'),
    (1.0, 'While stomping your feet'),
    (1.2, 'And sing this Silly Number Sooong!'),
    (5.0, 'Seventeen'),
    (0.7, 'Eighteen'),
    (0.5, 'Nineteen'),
    (0.5, 'Twenty'),
    (0.7, 'Someone eat all my Good & Plenty'),
    (2.1, 'Twenty-one'),
    (0.6, 'Twenty-two'),
    (0.5, 'Twenty-three'),
    (0.6, 'Twenty-four'),
    (0.9, 'My lips taste funny'),
    (0.8, 'After kissing the floor.'),
    (1.7, 'This is The Silly Number Song,'),
    (1.2, "C'mon everybody sing along!"),
    (3.6, 'Clap your hands'),
    (0.8, 'While stomping your feet'),
    (1.3, 'And sing this Silly Number Sooong!'),
    (5.0, 'One'),
    (0.2, 'Two'),
    (0.4, 'Three'),
    (0.3, 'Four'),
    (0.2, 'Five'),
    (0.3, 'Six'),
    (0.5, 'Seven'),
    (0.2, 'Eight'),
    (0.2, 'Nine'),
    (0.3, 'Ten'),
    (0.3, 'Eleven'),
    (0.4, 'Twelve'),
    (0.2, 'Thirteen'),
    (0.4, 'Tourteen'),
    (0.3, 'Tifteen'),
    (0.2, 'Sixteen'),
    (0.4, 'Seventeen'),
    (0.2, 'Eighteen'),
    (0.3, 'Nineteen'),
    (0.3, 'Twenty'),
    (0.3, 'Twenty-one'),
    (0.2, 'Twenty-two'),
    (0.3, 'Twenty-three'),
    (0.4, 'Twenty-four'),
    (0.5, 'This is The Silly Number Song.'),
    (2.3, 'This is The Silly Number Song!'),
    (2.2, 'This is The Silly Number Song!!')
    )

def make_song_sequence(text_node):
    colors=ColorPalette()
    s=Sequence()
    for delay, text in song:
        c=colors.new_color()
        s.append(Wait(delay))
        s.append(Func(text_node.set_text_color, c))
        s.append(Func(text_node.set_text, text))
    return s