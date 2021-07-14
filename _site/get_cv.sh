cd assets
grep "phone\|address" -v  /Users/rosecers/Dropbox/Professional/Resumes-CVs/Cersonsky2021.tex > Cersonsky.tex
cp /Users/rosecers/Dropbox/Professional/Resumes-CVs/*bib .
cp /Users/rosecers/Dropbox/Professional/Resumes-CVs/awards.tex .
pdflatex Cersonsky.tex 
bibtex Cersonsky
pdflatex Cersonsky.tex
cd -
git add assets
git commit -m "Changes to CV $(echo $(date))"
git push
