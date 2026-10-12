# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_all, collect_submodules

datas = [('files', 'files'), ('plugins', 'plugins')]
binaries = []
hiddenimports = ['tqdm', 'lightgbm']
tmp_ret = collect_all('hyperglot')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]

hiddenimports += collect_submodules('tqdm')

from PyInstaller.utils.hooks import collect_dynamic_libs

# Collect LightGBM's compiled libraries
binaries += collect_dynamic_libs('lightgbm')

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='LivingPath',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='LivingPath',
)

app = BUNDLE(
    coll,
    name='LivingPath.app',
    icon=None,
    bundle_identifier='com.yourname.livingpath',
)
