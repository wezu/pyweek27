from setuptools import setup

setup(
    name="silly_song",
    options = {
        'build_apps': {
            'include_patterns': [
                '**/*.png',
                '**/*.ttf',
                '**/*.bam',
                '**/*.egg',
                '**/*.glsl',
                '**/*.ico',
                '**/*.dds',
                '**/*.prc',
                '**/*.ogg',
                '**/*.ini',
                '**/*.cur',
                '**/*.ptf',
                '*.ini',
                '*.cur',
            ],
            'log_filename': '$USER_APPDATA/silly_song.log',
            'log_append': False,
            'gui_apps': {
                'silly_song': 'main.py',
            },
            'plugins': [
                'pandagl',
                'p3openal_audio',
            ],
            'platforms': [
                'manylinux1_x86_64',
                'macosx_10_6_x86_64',
                'win_amd64',
                'win32',
            ],
        }
    }
)
