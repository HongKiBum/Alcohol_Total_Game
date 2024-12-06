# -- Project information -----------------------------------------------------
project = 'Alcohol_Total_Game'
copyright = '2024, HongKiBum'
author = 'HongKiBum'
release = '0.1.5'

# -- General configuration ---------------------------------------------------
import os
import sys

# Alcohol_Total_Game의 src 폴더를 경로에 추가
sys.path.insert(0, os.path.abspath('../../'))

# 확장 기능 설정
extensions = [
    'sphinx.ext.autodoc',  # Python 코드 자동 문서화
    'sphinx.ext.napoleon', # Google/Numpy 스타일 docstring 지원
    'sphinx.ext.viewcode', # 코드 보기 기능
]

autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'show-inheritance': True,
}

# -- Options for HTML output -------------------------------------------------
html_theme = 'alabaster'
html_static_path = ['_static']
