import sys
import os
from PyInstaller.utils.hooks import collect_data_files

block_cipher = None

a = Analysis(['main_cli.py'],
             pathex=['.'],
             binaries=None,
             datas=[],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None,
             excludes=None,
             cipher=block_cipher)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='VideoNote',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False)

app = BUNDLE(exe,
             name='VideoNote.app',
             icon='assets/icon.icns',
             bundle_identifier='com.github.namuan.video-note',
             info_plist={
                 'CFBundleName': 'VideoNote',
                 'CFBundleVersion': '1.0.0',
                 'CFBundleShortVersionString': '1.0.0',
                 'NSPrincipalClass': 'NSApplication',
                 'NSHighResolutionCapable': True,
                 }
              )
