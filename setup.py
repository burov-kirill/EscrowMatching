from cx_Freeze import setup, Executable

executables = [Executable('EscrowMatching.py')]
setup(name='CRMandBIT',
      version='1.0.1',
      description='Сверка',
      executables=executables
      )
