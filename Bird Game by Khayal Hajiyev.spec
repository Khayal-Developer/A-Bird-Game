# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['bird_game.py'],
    pathex=[],
    binaries=[],
    datas=[('bird.py', '.'), ('button.py', '.'), ('feather.py', '.'), ('game_stats.py', '.'), ('monster.py', '.'), ('settings.py', '.'), ('star.py', '.'), ('images', 'images')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Bird Game by Khayal Hajiyev',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
