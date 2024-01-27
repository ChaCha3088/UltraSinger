from setuptools import setup, find_packages

setup(
    name='UltraSingerCustom',
    version='1.0.1',
    description='Ultra Singer Custom',
    url='https://github.com/ChaCha3088/UltraSinger',
    author='ChaCha3088',
    author_email='cha3088@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'crepe~=0.0.13',
        'demucs~=4.0.0',
        'ffmpeg_python~=0.2.0',
        'langcodes~=3.3.0',
        'language-data~=1.1',
        'librosa~=0.9.2',
        'matplotlib~=3.7.2',
        'musicbrainzngs~=0.7.1',
        'numpy~=1.23.5',
        'Pillow~=10.0.0',
        'pretty_midi~=0.2.10',
        'pydub~=0.25.1',
        'PyHyphen~=4.0.3',
        'python_Levenshtein~=0.21.1',
        'scipy~=1.11.2',
        'tensorflow==2.13',
        'tqdm~=4.65.2',
        'whisperx~=3.1.1',
        'yt_dlp~=2023.9.24',
        'isort~=5.12',
        'black~=23.3',
        'pylint~=2.17',
        'pytest~=7.3.1',
        'protobuf==3.20.*',
        'packaging~=23.2'
    ]
)

