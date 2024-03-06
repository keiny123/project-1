[app]
# (str) Title of your application
title = YourAppTitle

# (str) Package name
package.name = your.packagename

# (str) Package domain (needed for android/ios packaging)
package.domain = org.yourdomain

# (str) Source code where the main.py live
source.dir = .

# (list) List of source files
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
source.include_patterns = assets/*,images/*.png

# (list) List of exclusions using pattern matching
source.exclude_patterns = tests,venv,__pycache__

# (str) Application versioning (method 1)
version = 0.1

# (str) Application versioning (method 2)
version.regex = __version__ = ['"](.*)['"]
version.filename = %(source.dir)s/main.py

# (str) Application versioning (method 3)
version.major = 0
version.minor = 1

# (str) Icon of the application
icon.filename = icon.png

# (list) Application requirements
requirements = kivy==2.0.0, kivymd==0.104.1

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (str) Android logcat filters to use
android.logcat_filters = *:S python:D

# (int) Android API to use
android.api = 27

# (int) Minimum API required
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 27

# (int) Android NDK version to use
android.ndk = 21

# (int) Android NDK API to use. This is the minimum API your code will support, it should usually match android.minapi.
android.ndk_api = 21
