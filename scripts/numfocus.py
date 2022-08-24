from github import Github
from dotenv import load_dotenv
import os

load_dotenv()


def get_open_issues(g: Github, repo:str = "numfocus/YouTubeVideoTimestamps"):
    repo = g.get_repo("numfocus/YouTubeVideoTimestamps")
    return repo.get_issues(state='open')


def main(batch_size):
    # Get the open issues for the repo
    g = Github(os.getenv("GITHUB_ACCESS_TOKEN"))
    open_issues = get_open_issues(g)


    # Get list of yotube video ids and titles


    # In batches
        # Filter out the ones with already open issues
        # Check each video description for timestamps
        # If video does not have timestamps, create an issue and download transcript
        # Run autochapters on the transcript
        # Upload chapters to Github issue

if __name__ == "__main__":
    main()