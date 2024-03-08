[app]

# (str) Title of your application
title = Daily Tracker

# (str) Package name
package.name = myapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
requirements = python3.8,kivy==2.0.0,kivymd,pillow,gspread,oauth2client

# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
# requirements.source.kivy = ../../kivy

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (list) Supported orientations
# Valid options are: landscape, portrait, portrait-reverse or landscape-reverse
orientation = portrait

# Permissions
android.permissions = INTERNET

# (list) Android architectures to build for
android.archs = armeabi-v7a,arm64-v8a

# (int) Android API to use
android.api = 31

# (int) Minimum API your APK will support
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 20

# (str) Android NDK version to use
android.ndk = 25b

# (int) Android NDK API to use
android.ndk_api = 21

# (str) Application versioning (method 1)
version = 0.1

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (bool) Enable AndroidX support
android.enable_androidx = True

# (bool) Skip trying to update the Android SDK
android.skip_update = False

# (bool) Automatically accept SDK license
android.accept_sdk_license = True
