# Introduction to Git/GitHub
This is the repository used for conducting the introductory Git/GitHub session. You can use this repository
to make your first open-source contribution. 

## How to contribute
You need to add a file called `yourname.md` in the [`teamList`](teamList) folder. There is already a [`template.md`](teamList/template.md) 
file in the teamList which you can use. All you need to do to make your first contribution is to fill in your
details in the [`template.md`](teamList/template.md), save it as `yourname.md` and create a PR. 

## Get started
1. Fork this repository and clone the forked repo to your local machine.
2. Create a new branch and name it anything you like. 
```markdown
$ git checkout -b branch-name
```
3. Now, fill in the template and save it as a copy using the naming convention as mentioned above.
4. Commit and push to your forked repository.
```markdown
$ git add .
$ git commit -m "added yourname's details"
$ git push origin branch-name
```
5. Go to your forked repository on GitHub, create a PR from `forked-repo:branch-name` to `main-repo:master`
6. Wait for your PR to get approved and merged by the repository maintainers. It is important that you regularly check
the comments/discussions under your PR. In real life scenarios, your PR would not get merged instantly a majority number of times. Maintainers
would suggest many changes to your contribution before it is finally merged to the code base.

