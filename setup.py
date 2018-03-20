from distutils.core import setup, Extension

yescrypt_R32_module = Extension('yescrypt_R32',
        sources = ['yescrypt.c'],
        extra_compile_args=['-march=native', '-funroll-loops', '-fomit-frame-pointer'],
        include_dirs=['.'])

setup (name = 'yescrypt_R32',
       version = '1.0',
       description = 'Bindings for yescryptR32 proof of work used by WAVI...etc.',
       ext_modules = [yescrypt_R32_module])

