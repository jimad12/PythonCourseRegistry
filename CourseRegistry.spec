# -*- mode: python -*-
a = Analysis(['CourseRegistry.py'],
             pathex=['/Users/jimad12/Desktop/AI/begPy/chap12/pythonCourseRegistry'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='CourseRegistry',
          debug=False,
          strip=None,
          upx=True,
          console=False , icon='app.ico')
app = BUNDLE(exe,
             name='CourseRegistry.app',
             icon='app.ico')
