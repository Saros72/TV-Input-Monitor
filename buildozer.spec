[app]

title = TV Input Monitor
package.name = tvinputmonitor
package.domain = org.saros

version = 0.1.0

# --- SOURCE ---
source.dir = .
source.include_exts = py,png,jpg,kv,json,txt

# --- MINIMUM REQUIREMENTS ---
requirements = python3,kivy,pyjnius

# --- UI ---
orientation = landscape
fullscreen = 1

# --- ANDROID SDK ---
android.api = 31
android.minapi = 21
android.target = 31

# --- PERMISSIONS ---
android.permissions = INTERNET

# --- ARCH ---
#android.archs = arm64-v8a,armeabi-v7a
android.archs = armeabi-v7a

# --- ICON ---
icon.filename = %(source.dir)s/res/icon.png

# --- SPLASH ---

presplash.filename = %(source.dir)s/res/presplash.png
android.presplash_color = #FFFFFF

# --- RESOURCES ---
android.add_resources = %(source.dir)s/res


# --- HOOK/BOOTSTRAP ---
p4a.hook = p4a/hook.py
p4a.bootstrap = sdl2

# --- DEBUG ---
log_level = 2

android.allow_backup = False