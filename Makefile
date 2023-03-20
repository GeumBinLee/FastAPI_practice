commit :
	git add .pre-commit-config.yaml
	git add .
	pre-commit run
	git commit -m "Commit with convetion libraries"
	git push origin main