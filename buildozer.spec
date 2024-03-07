[app]
title = Daily Tracker
package.name = com.yourcompany.dailytracker
package.domain = org.yourdomain
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 1.0
requirements = kivy,gspread,oauth2client,cython,aidl
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

# Android specific settings
android.permissions = INTERNET
android.api = 27
android.ndk = 19b
android.arch = armeabi-v7a
android.sdk = 20
android.minapi = 21

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
android.ndk_path = 

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
android.sdk_path = 

# (str) python-for-android branch to use, defaults to master
p4a.branch = master

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True
