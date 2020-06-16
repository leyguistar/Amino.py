git add -A
git commit -am "Release 1.0.3"
git push amino master
python setup.py sdist bdist_wheel
python -m twine upload --repository pypi dist/*
pause