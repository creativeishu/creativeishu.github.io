.PHONY = build

build: 
	bundle exec jekyll build
	git add *
	git commit -am "Builded"
	git push