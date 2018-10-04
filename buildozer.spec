[app]

# (str) Title of your application
title = Two button

# (str) Package name
package.name = twobutton

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,ttf

# (list) List of exclusions using pattern matching
source.exclude_patterns = buildozer.spec

# (str) Application versioning (method 1)
version = 0.1

# (str) Application versioning (method 2)
#version.regex = __version__ = ['\"]([^'\"]*)['\"]
#version.filename = %(source.dir)s/../../kivymd/__init__.py

# (list) Application requirements
# comma seperated e.g. requirements = sqlite3,kivy
requirements = kivy==1.10.1,android,python3crystax

# (str) Presplash of the application
presplash.filename = %(source.dir)s/assets/presplash.png
android.presplash_color = #FFFFFF

# (str) Icon of the application
#icon.filename = %(source.dir)s/../../kivymd/images/kivymd_logo.png

# (str) Supported orientation (one of landscape, portrait or all)
orientation = portrait

# change the major version of python used by the app
osx.python_version = 3

# Kivy version to use
osx.kivy_version = 1.9.1

# (int) Android API to use
# android.api = 19

# (int) Android SDK version to use
# android.sdk = 23

# (bool) Use --private data storage (True) or --dir public storage (False)
private = False

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
android.ndk_path = /home/user/.buildozer/crystax-ndk-10.3.1

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Permissions
android.permissions = INTERNET
android.arch = armeabi-v7a

# (str) python-for-android git clone directory (if empty, it will be automatically cloned from github)
#p4a.source_dir = /home/kivy/Repos/python-for-android/

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86
android.arch = armeabi


[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

