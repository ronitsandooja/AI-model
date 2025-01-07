
setup(
    name='chatbotAI',
    version=version['__version__'],
    author="",
    author_email="",
    url="https://github.com/",
    description="A chatbot AI engine is a chatbot builder platform that provides both bot intelligence and"
                " chat handler with minimal codding",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=list(package_dir.keys()),
    license='MIT',
    keywords='chatbot ai engine and chat builder platform',
    platforms=["Windows", "Linux", "Solaris", "Mac OS-X", "Unix"],
    package_dir=package_dir,
    include_package_data=True,
    package_data={"chatbot":  package_data},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Natural Language :: German',
        'Natural Language :: Portuguese (Brazilian)',
        'Natural Language :: Hebrew',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Communications :: Chat',
    ],
    install_requires=[
          'requests',
      ]
)
