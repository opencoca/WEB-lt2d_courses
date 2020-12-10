# Django-Studio
Django-Studio is an open source virtual video studio built on Django, with a strong community and commercial support. It's focused on user experience, and offers precise control for designers and developers. 

### Features

* Fullscreen mode for the best viewing experience.
* Video previewer so you can see what it will look like before making any changes.
* Record audio and video directly to disk or stream to the internet. 
* Export to webm file ~~or use the built-in DAW~~.
* ~~Playback controls include panning, volume, mute and solo.~~
* ~~Multiple audio tracks (MP3/AIFF) for different soundtracks or narration.~~
* ~~A wide range of plugins to help you create your videos: effects, transitions, music, titles...~~
* ~~Audio and subtitle track selection in the video editor.~~
* ~~A wide range of effects including reverb, delay, chorus, flanger, phaser and more.~~
* ~~Automation features allow you to create complex sequences that can be used in your music software.~~
* ~~Mixer with up to 4 channels (2 stereo).~~

##### Note: Features ~~Striked through~~ are not finalized 

Django Studio has been designed with ease of use as its main goal, so it's easy to get started right away! You'll find everything you need to start making music in minutes:

## Installation & Configuration The installation process is very simple: 

1. pip install django-studio
2. add the following to your project urls.py file
```
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
3. add the following to your projects settings installed apps 
```
    'studio.apps.StudioConfig',
```