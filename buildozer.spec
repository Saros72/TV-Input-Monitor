[app]

title = TV Input Monitor
package.name = tvinputmonitor
package.domain = org.saros

version = 0.1.0

# --- SOURCE ---
source.dir = .
source.include_exts = py,png,jpg,kv,json,txt

# --- MINIMUM REQUIREMENTS ---
requirements = python3,kivy

# --- UI ---
orientation = all
fullscreen = 0

# --- ANDROID SDK ---
android.api = 31
android.minapi = 21
android.target = 31

# --- PERMISSIONS ---
# žádné nejsou potřeba
android.permissions =

# --- ARCH ---
android.archs = arm64-v8a,armeabi-v7a

icon.filename = assets/icon.png
presplash.filename = assets/presplash.png
android.presplash_color = #000000
#android.add_resources = assets/

# --- BOOTSTRAP ---
p4a.bootstrap = sdl2

# --- DEBUG ---
log_level = 2

android.allow_backup = False