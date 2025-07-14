# settings.py (located at LibraryProject/LibraryProject/settings.py)

import os # <--- ENSURE THIS IS AT THE TOP OF THE FILE

# ... other existing settings ...

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # <--- This is the line to modify
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ... rest of your settings ...
