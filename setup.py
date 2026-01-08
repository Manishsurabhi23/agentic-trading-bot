from setuptools import setup, find_packages
setup(name = 'agentic-trading-bot',
      version = '0.1.0',
      author='manish',
      author_email = 'manishsurabhi23@gmail.com',
      packages = find_packages(),
        install_requires = ['langchain-astradb', 'langchain','tavily-python','polygon','grandalf','lancedb'],)
