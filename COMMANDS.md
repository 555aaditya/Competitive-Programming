git checkout unsolved
git pull origin unsolved

git add .
git commit -m "solve: lc xyz"

git push origin unsolved

gh pr create --base main --head unsolved --fill
gh pr merge --squash

git pull origin main
git merge main
git push origin unsolved