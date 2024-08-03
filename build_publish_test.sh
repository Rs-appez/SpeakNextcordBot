source venv/bin/activate
python -m build
twine upload -r testpypi dist/*