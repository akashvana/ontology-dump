from git import Repo

PATH_OF_GIT_REPO = r'.'
COMMIT_MESSAGE = "lastest commit 1"
def git_push():
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(all=True)
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('Some error occured while pushing the code')    

git_push()
