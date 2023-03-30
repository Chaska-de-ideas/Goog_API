from setuptools import setup, find_packages

setup(
    name='Goog_API',

    version='0.2',
    author           = 'Hernán A. Teszkiewicz Novick',
    author_email     = 'herni@cajadeideas.ar',
    license          =  'MIT'    ,
    url= 'https://github.com/Chaska-de-ideas/Goog_API',
    download_url     =  'https://github.com/Chaska-de-ideas/Goog_API/raw/main/Goog_API-0.1.tar.gz',
    packages=find_packages(),
    install_requires=[
        'google-api-python-client',
        'google-auth',
        'google-auth-oauthlib',
        'google-auth-httplib2',
        'requests',
    ],
    extras_require ={
    'Goog_API_Sheets_Metodos': ['pandas'],
    'Goog_API_gMail_Metodos': ['mimetypes','email','base64'],
    'Goog_API_Calendar_Metodos': ['datetime'],
    
    },
)
