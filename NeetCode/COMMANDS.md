gh pr create \
--base main \
--head unsolved \
--title "DSA Progress Update" \
--body "Solved additional LeetCode problems"

gh pr create --base main --head unsolved --fill
gh pr merge --squash

git pull origin main
git merge main
git push origin unsolved